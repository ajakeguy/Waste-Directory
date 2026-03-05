#!/usr/bin/env python3
"""
Extract hauler data from VT DEC database browser snapshots
This script parses the HTML table data from browser snapshots
"""

import re
import json
import csv
from datetime import datetime

def parse_hauler_rows(snapshot_text):
    """
    Parse hauler data from browser snapshot text
    Extracts rows with ID, Company, Contact, Address, Town, State, Phone, etc.
    """
    haulers = []
    
    # Pattern to match row definitions with hauler data
    # Looking for patterns like: row "2195 128 Holdings, LLC dba Grunts Move Junk Bart Newhouse..."
    row_pattern = r'row "(\d+)\s+([^"]+)" \[ref=e\d+\]:'
    
    # Pattern to match cells within rows
    cell_pattern = r'cell "([^"]*)" \[ref=e\d+\]'
    
    # Find all row definitions
    rows = re.findall(row_pattern, snapshot_text)
    
    # Also extract all cells
    all_cells = re.findall(cell_pattern, snapshot_text)
    
    # Process in chunks of 11 (ID, Company, Contact, Address, Town, State, Phone, PermitYear, Waste Type, Bear Resistant, Service Area)
    chunk_size = 11
    for i in range(0, len(all_cells) - chunk_size + 1, chunk_size):
        chunk = all_cells[i:i + chunk_size]
        
        # Check if first element looks like an ID (numeric)
        if chunk[0].isdigit():
            hauler = {
                'id': chunk[0],
                'company': chunk[1],
                'contact': chunk[2],
                'address': chunk[3],
                'town': chunk[4],
                'state': chunk[5],
                'phone': chunk[6],
                'permit_year': chunk[7],
                'waste_type': chunk[8],
                'bear_resistant': chunk[9] if len(chunk) > 9 else '',
                'service_area': chunk[10] if len(chunk) > 10 else '',
                'data_source': 'VT_DEC',
                'data_quality': 'gold_standard',
                'extracted_date': datetime.now().isoformat()
            }
            haulers.append(hauler)
    
    return haulers

def save_haulers_json(haulers, filename='vt_dec_haulers.json'):
    """Save haulers to JSON file"""
    with open(filename, 'w') as f:
        json.dump(haulers, f, indent=2)
    print(f"✅ Saved {len(haulers)} haulers to {filename}")

def save_haulers_csv(haulers, filename='vt_dec_haulers.csv'):
    """Save haulers to CSV file"""
    if not haulers:
        print("No haulers to save")
        return
    
    fieldnames = ['id', 'company', 'contact', 'address', 'town', 'state', 
                  'phone', 'permit_year', 'waste_type', 'bear_resistant', 
                  'service_area', 'data_source', 'data_quality']
    
    with open(filename, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for h in haulers:
            row = {k: h.get(k, '') for k in fieldnames}
            writer.writerow(row)
    
    print(f"✅ Saved {len(haulers)} haulers to {filename}")

def analyze_haulers(haulers):
    """Analyze hauler data by state and waste type"""
    by_state = {}
    by_waste_type = {}
    
    for h in haulers:
        state = h.get('state', 'Unknown')
        waste_type = h.get('waste_type', 'Unknown')
        
        by_state[state] = by_state.get(state, 0) + 1
        by_waste_type[waste_type] = by_waste_type.get(waste_type, 0) + 1
    
    print("\n📊 Hauler Statistics:")
    print(f"Total haulers: {len(haulers)}")
    
    print("\nBy State:")
    for state, count in sorted(by_state.items(), key=lambda x: -x[1]):
        print(f"  {state}: {count}")
    
    print("\nBy Waste Type:")
    for wt, count in sorted(by_waste_type.items(), key=lambda x: -x[1]):
        print(f"  {wt}: {count}")
    
    return {
        'total': len(haulers),
        'by_state': by_state,
        'by_waste_type': by_waste_type
    }

if __name__ == '__main__':
    # Example usage - will be populated with actual snapshot data
    print("VT DEC Hauler Extraction Tool")
    print("=" * 50)
    print("\nTo use:")
    print("1. Copy browser snapshot text")
    print("2. Call parse_hauler_rows(snapshot_text)")
    print("3. Data will be extracted and saved")
