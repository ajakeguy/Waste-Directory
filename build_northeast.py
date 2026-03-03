#!/usr/bin/env python3
"""
Northeast Waste Hauler Directory Builder
Combines VT (complete), NH (partial), MA (partial) with quality flags
"""

import json
import urllib.request
import urllib.parse
import ssl
import time

ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

def geocode_town_only(town, state):
    """Fallback: Geocode just the town center"""
    try:
        query = f"{town}, {state}"
        params = urllib.parse.urlencode({'q': query, 'format': 'json', 'limit': 1})
        url = f"https://nominatim.openstreetmap.org/search?{params}"
        
        req = urllib.request.Request(url, headers={'User-Agent': 'VermontWasteDirectory/1.0'})
        with urllib.request.urlopen(req, context=ssl_context, timeout=10) as response:
            data = json.loads(response.read().decode('utf-8'))
            if data:
                return {'lat': float(data[0]['lat']), 'lng': float(data[0]['lon'])}
    except:
        pass
    return None

def load_data():
    """Load all state data"""
    with open('vermont_haulers_enriched.json', 'r') as f:
        vt_haulers = json.load(f)
    
    # NH and MA from VT cross-reference
    nh_haulers = [h for h in vt_haulers if h['state'] == 'NH']
    ma_haulers = [h for h in vt_haulers if h['state'] == 'MA']
    
    # VT-only haulers
    vt_only = [h for h in vt_haulers if h['state'] == 'VT']
    
    return vt_only, nh_haulers, ma_haulers

def add_quality_flags(haulers, state_code, data_quality):
    """Add data quality metadata to each hauler"""
    for h in haulers:
        h['data_source'] = state_code
        h['data_quality'] = data_quality
        h['state_source'] = state_code
        
        # Determine geocode quality
        if h.get('lat') and h.get('lng'):
            if h.get('geocode_confidence') == 'high':
                h['location_quality'] = 'precise'
            else:
                h['location_quality'] = 'approximate'
        else:
            h['location_quality'] = 'missing'
    
    return haulers

def try_fallback_geocoding(haulers):
    """Try town-level geocoding for failures"""
    improved = 0
    for h in haulers:
        if not h.get('lat') and not h.get('geocode_failed'):
            # Try town-only geocoding
            result = geocode_town_only(h['town'], h['state'])
            if result:
                h['lat'] = result['lat']
                h['lng'] = result['lng']
                h['location_quality'] = 'town_center'
                h['geocode_method'] = 'town_fallback'
                improved += 1
            time.sleep(0.5)  # Rate limiting
    
    return improved

def build_northeast_directory():
    print("🗺️  Building Northeast Waste Hauler Directory")
    print("=" * 60)
    
    vt_haulers, nh_haulers, ma_haulers = load_data()
    
    print(f"\nInitial counts from VT cross-reference:")
    print(f"  Vermont:     {len(vt_haulers)} haulers")
    print(f"  New Hampshire: {len(nh_haulers)} haulers")
    print(f"  Massachusetts: {len(ma_haulers)} haulers")
    
    # Add quality flags
    vt_haulers = add_quality_flags(vt_haulers, 'VT', 'complete_state_permit_data')
    nh_haulers = add_quality_flags(nh_haulers, 'NH', 'cross_reference_only')
    ma_haulers = add_quality_flags(ma_haulers, 'MA', 'cross_reference_only')
    
    # Try fallback geocoding for missing locations
    print("\n📍 Attempting fallback geocoding (town centers)...")
    
    vt_improved = try_fallback_geocoding(vt_haulers)
    nh_improved = try_fallback_geocoding(nh_haulers)
    ma_improved = try_fallback_geocoding(ma_haulers)
    
    print(f"  VT: {vt_improved} additional locations")
    print(f"  NH: {nh_improved} additional locations")
    print(f"  MA: {ma_improved} additional locations")
    
    # Combine all haulers
    all_haulers = vt_haulers + nh_haulers + ma_haulers
    
    # Add unique IDs
    for i, h in enumerate(all_haulers, 1):
        h['northeast_id'] = f"NE-{i:04d}"
    
    # Calculate stats
    total = len(all_haulers)
    with_location = sum(1 for h in all_haulers if h.get('lat'))
    
    print(f"\n📊 Northeast Directory Summary:")
    print(f"  Total haulers: {total}")
    print(f"  With coordinates: {with_location} ({with_location/total*100:.1f}%)")
    print(f"  Missing locations: {total - with_location}")
    
    # Save combined dataset
    with open('northeast_haulers.json', 'w') as f:
        json.dump(all_haulers, f, indent=2)
    
    # Save by state
    with open('vt_haulers_complete.json', 'w') as f:
        json.dump(vt_haulers, f, indent=2)
    
    with open('nh_haulers_partial.json', 'w') as f:
        json.dump(nh_haulers, f, indent=2)
    
    with open('ma_haulers_partial.json', 'w') as f:
        json.dump(ma_haulers, f, indent=2)
    
    print("\n💾 Files saved:")
    print("  - northeast_haulers.json (combined)")
    print("  - vt_haulers_complete.json")
    print("  - nh_haulers_partial.json")
    print("  - ma_haulers_partial.json")
    
    # Create data quality report
    print("\n" + "=" * 60)
    print("DATA QUALITY BY STATE")
    print("=" * 60)
    
    for state, haulers in [('VT', vt_haulers), ('NH', nh_haulers), ('MA', ma_haulers)]:
        total = len(haulers)
        precise = sum(1 for h in haulers if h.get('location_quality') == 'precise')
        approximate = sum(1 for h in haulers if h.get('location_quality') == 'approximate')
        town_center = sum(1 for h in haulers if h.get('location_quality') == 'town_center')
        missing = sum(1 for h in haulers if h.get('location_quality') == 'missing')
        
        print(f"\n{state}:")
        print(f"  Total haulers: {total}")
        print(f"  Precise location: {precise} ({precise/total*100:.1f}%)")
        print(f"  Approximate location: {approximate} ({approximate/total*100:.1f}%)")
        print(f"  Town center only: {town_center} ({town_center/total*100:.1f}%)")
        print(f"  Missing location: {missing} ({missing/total*100:.1f}%)")
        
        if state == 'VT':
            print(f"  ⭐ Quality: GOLD STANDARD - State permit database + geocoded")
        else:
            print(f"  ⚠️  Quality: PARTIAL - Cross-reference only, needs state verification")
    
    return all_haulers

if __name__ == "__main__":
    build_northeast_directory()
