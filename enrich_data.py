#!/usr/bin/env python3
"""
Vermont Hauler Data Enrichment Script
Phase 1: Geocoding addresses to precise coordinates
Phase 2: Website discovery via search patterns
Phase 3: Additional contact information
"""

import json
import urllib.request
import urllib.parse
import ssl
import re
import time
from urllib.error import HTTPError

# Create SSL context
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

# Free geocoding options (with rate limits)
# Using Nominatim (OpenStreetMap) - requires 1 sec delay between requests
NOMINATIM_URL = "https://nominatim.openstreetmap.org/search"

def geocode_address(company, address, town, state):
    """Geocode an address using Nominatim (OpenStreetMap)"""
    
    # Build search query
    query = f"{address}, {town}, {state}"
    
    params = urllib.parse.urlencode({
        'q': query,
        'format': 'json',
        'limit': 1,
        'addressdetails': 1
    })
    
    url = f"{NOMINATIM_URL}?{params}"
    
    headers = {
        'User-Agent': 'VermontWasteDirectory/1.0 (research project)'
    }
    
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, context=ssl_context, timeout=10) as response:
            data = json.loads(response.read().decode('utf-8'))
            
            if data and len(data) > 0:
                result = data[0]
                return {
                    'lat': float(result['lat']),
                    'lng': float(result['lon']),
                    'display_name': result.get('display_name', ''),
                    'osm_id': result.get('osm_id', ''),
                    'confidence': 'high' if result.get('importance', 0) > 0.5 else 'medium'
                }
    except Exception as e:
        print(f"  Geocoding error for {company}: {e}")
    
    return None

def search_for_website(company_name, town, state):
    """Attempt to find company website via simple pattern matching"""
    # This would require search API - for now, we'll create likely URLs
    # In production, this would use Google Custom Search API or similar
    
    # Clean company name for URL guessing
    clean_name = re.sub(r'[^\w\s]', '', company_name.lower())
    clean_name = clean_name.replace('llc', '').replace('inc', '').replace('dba', '').strip()
    clean_name = clean_name.replace(' ', '')
    
    # Common patterns
    possible_domains = [
        f"{clean_name}.com",
        f"{clean_name}vt.com",
        f"{clean_name}vermont.com"
    ]
    
    # For now, return placeholder - would validate with HTTP requests
    return {
        'possible_domains': possible_domains,
        'verified': False,
        'method': 'pattern_guess'
    }

def format_phone(phone):
    """Standardize phone format"""
    if not phone:
        return None
    
    # Remove non-digits
    digits = re.sub(r'\D', '', phone)
    
    if len(digits) == 10:
        return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
    elif len(digits) == 11 and digits[0] == '1':
        return f"({digits[1:4]}) {digits[4:7]}-{digits[7:]}"
    
    return phone

def load_haulers():
    """Load existing hauler data"""
    with open('vermont_haulers.json', 'r') as f:
        return json.load(f)

def save_haulers(haulers, filename):
    """Save enriched hauler data"""
    with open(filename, 'w') as f:
        json.dump(haulers, f, indent=2)

def enrich_haulers():
    """Main enrichment process"""
    print("🗑️  Vermont Waste Hauler Data Enrichment")
    print("=" * 60)
    
    haulers = load_haulers()
    total = len(haulers)
    
    print(f"Loaded {total} haulers")
    print()
    
    # Statistics
    geocoded = 0
    failed_geocode = 0
    
    # Process each hauler
    for i, hauler in enumerate(haulers, 1):
        company = hauler['company']
        
        print(f"[{i}/{total}] {company[:50]}...")
        
        # Skip if already geocoded
        if 'lat' in hauler and 'lng' in hauler:
            print(f"  ✓ Already geocoded: ({hauler['lat']:.4f}, {hauler['lng']:.4f})")
            geocoded += 1
            continue
        
        # Geocode address
        address = f"{hauler['address']}, {hauler['town']}"
        state = hauler['state']
        
        result = geocode_address(company, address, hauler['town'], state)
        
        if result:
            hauler['lat'] = result['lat']
            hauler['lng'] = result['lng']
            hauler['geocoded_address'] = result['display_name']
            hauler['geocode_confidence'] = result['confidence']
            print(f"  ✓ Geocoded: ({result['lat']:.4f}, {result['lng']:.4f}) [{result['confidence']}]")
            geocoded += 1
        else:
            print(f"  ✗ Failed to geocode")
            hauler['geocode_failed'] = True
            failed_geocode += 1
        
        # Format phone nicely
        if 'phone_formatted' not in hauler:
            hauler['phone_formatted'] = format_phone(hauler['phone'])
        
        # Add waste type descriptions
        waste_descriptions = []
        waste_type_map = {
            'S': 'Solid Waste',
            'H': 'Hazardous Waste', 
            'R': 'Recyclables',
            'M': 'Medical Waste'
        }
        for wt in hauler['waste_types']:
            if wt in waste_type_map:
                waste_descriptions.append(waste_type_map[wt])
        hauler['waste_types_description'] = waste_descriptions
        
        # Website discovery (placeholder for now)
        if 'website_data' not in hauler:
            hauler['website_data'] = search_for_website(company, hauler['town'], state)
        
        # Rate limiting - Nominatim requires 1 second between requests
        if i < total:
            time.sleep(1)
        
        # Save progress every 10 records
        if i % 10 == 0:
            save_haulers(haulers, 'vermont_haulers_enriched_partial.json')
            print(f"  💾 Saved progress ({i}/{total})")
    
    # Final save
    save_haulers(haulers, 'vermont_haulers_enriched.json')
    
    print()
    print("=" * 60)
    print("ENRICHMENT COMPLETE")
    print("=" * 60)
    print(f"Total haulers: {total}")
    print(f"Successfully geocoded: {geocoded} ({geocoded/total*100:.1f}%)")
    print(f"Failed to geocode: {failed_geocode} ({failed_geocode/total*100:.1f}%)")
    print()
    print("Files saved:")
    print("  - vermont_haulers_enriched.json (full enriched dataset)")
    print("  - vermont_haulers_enriched_partial.json (backup)")
    
    return haulers

if __name__ == "__main__":
    # Check if user wants to run
    import sys
    
    print("This will geocode 536 addresses using Nominatim (OpenStreetMap).")
    print("Rate limit: 1 request per second = ~9 minutes total.")
    print()
    print("Note: Free geocoding services have limits. For production,")
    print("consider Mapbox ($5/1000) or Google Maps API.")
    print()
    
    # For automation, just run it
    enrich_haulers()
