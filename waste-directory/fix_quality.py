#!/usr/bin/env python3
"""
Fix quality flags on existing data
"""

import json

with open('vermont_haulers_enriched.json', 'r') as f:
    vt_data = json.load(f)

# Properly categorize geocode quality
for h in vt_data:
    if h.get('lat') and h.get('lng'):
        if h.get('geocode_confidence') == 'high':
            h['location_quality'] = 'precise'
        elif 'geocoded_address' in h:
            h['location_quality'] = 'address_level'
        else:
            h['location_quality'] = 'approximate'
    else:
        h['location_quality'] = 'missing'

# Save corrected data
with open('vermont_haulers_enriched.json', 'w') as f:
    json.dump(vt_data, f, indent=2)

# Report
with_location = sum(1 for h in vt_data if h.get('lat'))
precise = sum(1 for h in vt_data if h.get('location_quality') == 'precise')
address = sum(1 for h in vt_data if h.get('location_quality') == 'address_level')
approx = sum(1 for h in vt_data if h.get('location_quality') == 'approximate')
missing = sum(1 for h in vt_data if h.get('location_quality') == 'missing')

print("Vermont Geocoding Quality Fixed:")
print(f"  Total: {len(vt_data)}")
print(f"  Precise: {precise}")
print(f"  Address level: {address}")
print(f"  Approximate: {approx}")
print(f"  Missing: {missing}")
print(f"  Total with location: {with_location} ({with_location/len(vt_data)*100:.1f}%)")
