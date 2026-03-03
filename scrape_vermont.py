#!/usr/bin/env python3
"""
Vermont Waste Hauler Scraper (using urllib)
Extracts all permitted haulers from VT DEC database
"""

import urllib.request
import urllib.parse
import re
import json
import csv
import ssl

BASE_URL = "https://anrweb.vermont.gov/DEC/_DEC/SolidWasteTransporters.aspx"

# Create SSL context that doesn't verify certs (sometimes needed for older systems)
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
}

def fetch_url(url, data=None):
    """Fetch URL with proper headers"""
    req = urllib.request.Request(url, data=data, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, context=ssl_context, timeout=30) as response:
            return response.read().decode('utf-8', errors='ignore')
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

def extract_haulers_simple(html):
    """Extract hauler data using simple pattern matching"""
    haulers = []
    
    # Look for table rows with hauler data
    # The pattern: ID number followed by company name, address, etc.
    # Looking for sequences like: ID | Company | Contact | Address | Town | State | Phone | Year | Types | Bear | Service
    
    # Try to find all table data cells
    td_pattern = r'<td[^>]*>(.*?)</td>'
    all_tds = re.findall(td_pattern, html, re.DOTALL | re.IGNORECASE)
    
    # Clean HTML tags
    clean_tds = []
    for td in all_tds:
        # Remove HTML tags
        clean = re.sub(r'<[^>]+>', '', td)
        # Normalize whitespace
        clean = ' '.join(clean.split())
        clean_tds.append(clean)
    
    # Look for sequences that match hauler pattern (ID number followed by company name)
    i = 0
    while i < len(clean_tds) - 10:
        # Check if this looks like a hauler row start (numeric ID)
        if clean_tds[i].strip().isdigit():
            permit_id = clean_tds[i].strip()
            company = clean_tds[i+1].strip() if i+1 < len(clean_tds) else ""
            contact = clean_tds[i+2].strip() if i+2 < len(clean_tds) else ""
            address = clean_tds[i+3].strip() if i+3 < len(clean_tds) else ""
            town = clean_tds[i+4].strip() if i+4 < len(clean_tds) else ""
            state = clean_tds[i+5].strip() if i+5 < len(clean_tds) else ""
            phone = clean_tds[i+6].strip() if i+6 < len(clean_tds) else ""
            year = clean_tds[i+7].strip() if i+7 < len(clean_tds) else ""
            waste_types = clean_tds[i+8].strip() if i+8 < len(clean_tds) else ""
            bear = clean_tds[i+9].strip() if i+9 < len(clean_tds) else ""
            service = clean_tds[i+10].strip() if i+10 < len(clean_tds) else ""
            
            # Validate: should have a company name and valid state
            if company and len(state) == 2 and state.isupper():
                haulers.append({
                    "permit_id": permit_id,
                    "company": company,
                    "contact": contact,
                    "address": address,
                    "town": town,
                    "state": state,
                    "phone": phone,
                    "permit_year": year,
                    "waste_types": waste_types,
                    "bear_resistant": bear,
                    "service_area": service
                })
                i += 11  # Skip past this row
                continue
        i += 1
    
    return haulers

def fetch_all_haulers():
    """Fetch all haulers"""
    all_haulers = []
    
    print("Fetching Vermont DEC Waste Transporter Database...")
    print("=" * 60)
    
    # Fetch main page
    html = fetch_url(BASE_URL)
    if not html:
        print("Failed to fetch main page")
        return []
    
    print("✓ Fetched main page")
    
    # Extract haulers
    haulers = extract_haulers_simple(html)
    print(f"✓ Found {len(haulers)} haulers")
    all_haulers.extend(haulers)
    
    # Look for pagination
    page_count = len(re.findall(r'Page\$\d+', html))
    if page_count > 0:
        print(f"✓ Detected {page_count} pages of results")
        print("  (Note: ASP.NET pagination requires viewstate simulation)")
        print("  For full scrape, would need to simulate postbacks")
    
    return all_haulers

def save_data(haulers):
    """Save haulers to JSON and CSV"""
    if not haulers:
        print("No haulers to save")
        return
    
    # JSON
    with open("vermont_haulers.json", "w") as f:
        json.dump(haulers, f, indent=2)
    
    # CSV
    with open("vermont_haulers.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=haulers[0].keys())
        writer.writeheader()
        writer.writerows(haulers)
    
    print(f"\n✓ Saved {len(haulers)} haulers to:")
    print("  - vermont_haulers.json")
    print("  - vermont_haulers.csv")

def show_stats(haulers):
    """Show statistics about the haulers"""
    if not haulers:
        return
    
    print("\n" + "=" * 60)
    print("STATISTICS")
    print("=" * 60)
    
    # By state
    states = {}
    for h in haulers:
        states[h["state"]] = states.get(h["state"], 0) + 1
    print(f"\nBy State:")
    for state, count in sorted(states.items()):
        print(f"  {state}: {count}")
    
    # By waste type
    print(f"\nWaste Types (S=Solid, H=Hazardous, R=Recyclable, M=Medical):")
    types = {"S": 0, "H": 0, "R": 0, "M": 0}
    for h in haulers:
        for t in h["waste_types"]:
            if t in types:
                types[t] += 1
    for t, count in sorted(types.items()):
        print(f"  {t}: {count}")
    
    # Bear resistant
    bear_count = sum(1 for h in haulers if h["bear_resistant"].lower() in ["yes", "y"])
    print(f"\nBear-resistant containers: {bear_count} ({bear_count/len(haulers)*100:.1f}%)")

if __name__ == "__main__":
    haulers = fetch_all_haulers()
    
    if haulers:
        save_data(haulers)
        show_stats(haulers)
        
        print("\n" + "=" * 60)
        print("SAMPLE ENTRIES")
        print("=" * 60)
        for h in haulers[:5]:
            print(f"\n{h['company']}")
            print(f"  Location: {h['town']}, {h['state']}")
            print(f"  Phone: {h['phone']}")
            print(f"  Types: {h['waste_types']}")
    else:
        print("\n✗ No haulers found")
        print("  The page may require JavaScript or has changed structure")
