#!/usr/bin/env python3
"""
5-State Northeast Waste Hauler Directory
VT + NH + MA + NY + NJ
"""

import json

# Load Vermont enriched data
with open('vermont_haulers_enriched.json', 'r') as f:
    vt_data = json.load(f)

# Filter by state
vt_haulers = [h for h in vt_data if h['state'] == 'VT']
nh_haulers = [h for h in vt_data if h['state'] == 'NH']
ma_haulers = [h for h in vt_data if h['state'] == 'MA']
ny_haulers = [h for h in vt_data if h['state'] == 'NY']
nj_haulers = [h for h in vt_data if h['state'] == 'NJ']

# Add quality flags
def flag_haulers(haulers, state, quality_level, note):
    for h in haulers:
        h['directory_state'] = state
        h['data_quality_level'] = quality_level
        h['data_quality_note'] = note
        h['northeast_region'] = True
    return haulers

vt_haulers = flag_haulers(vt_haulers, 'VT', 'gold', 'Complete state permit database + geocoded')
nh_haulers = flag_haulers(nh_haulers, 'NH', 'cross_reference', 'From VT permit cross-reference')
ma_haulers = flag_haulers(ma_haulers, 'MA', 'cross_reference', 'From VT permit cross-reference')
ny_haulers = flag_haulers(ny_haulers, 'NY', 'cross_reference', 'From VT permit cross-reference')
nj_haulers = flag_haulers(nj_haulers, 'NJ', 'cross_reference', 'From VT permit cross-reference')

# Combine all
all_haulers = vt_haulers + nh_haulers + ma_haulers + ny_haulers + nj_haulers

# Add unique IDs
for i, h in enumerate(all_haulers, 1):
    h['five_state_id'] = f"NE5-{i:04d}"

# Save combined dataset
with open('five_state_haulers.json', 'w') as f:
    json.dump(all_haulers, f, indent=2)

# Stats by state
states = [
    ('Vermont', vt_haulers, 'gold'),
    ('New Hampshire', nh_haulers, 'cross_reference'),
    ('Massachusetts', ma_haulers, 'cross_reference'),
    ('New York', ny_haulers, 'cross_reference'),
    ('New Jersey', nj_haulers, 'cross_reference')
]

print("🗺️ 5-State Northeast Waste Hauler Directory")
print("=" * 60)
print()
print("State Breakdown:")
print()

total = 0
for state_name, haulers, quality in states:
    count = len(haulers)
    total += count
    geocoded = sum(1 for h in haulers if h.get('lat'))
    
    icon = "⭐" if quality == 'gold' else "⚠️"
    print(f"{icon} {state_name:20s} {count:4d} haulers  ({geocoded} geocoded)")

print()
print("=" * 60)
print(f"TOTAL: {total} haulers across 5 states")
print("=" * 60)
print()
print("Quality Levels:")
print("  ⭐ Gold: Complete state permit database (VT only)")
print("  ⚠️ Cross-Reference: From VT permit cross-check (NH, MA, NY, NJ)")
print()
print("Files saved:")
print("  - five_state_haulers.json")
print()
print("Next: Disposal facilities (landfills, transfer stations, etc.)")
print("      These are more heavily regulated = better data availability")
