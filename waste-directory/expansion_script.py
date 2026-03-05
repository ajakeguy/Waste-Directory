#!/usr/bin/env python3
"""
Waste Directory V2 - Data Expansion Script
Automated research and data enrichment for 8-state waste hauler directory
"""

import json
import csv
import os
from datetime import datetime

class WasteDirectoryExpander:
    def __init__(self, workspace_dir="."):
        self.workspace = workspace_dir
        self.data = {
            'haulers': [],
            'facilities': [],
            'sources': {},
            'metadata': {
                'created': datetime.now().isoformat(),
                'version': '2.0'
            }
        }
        
    def load_existing_data(self):
        """Load the existing 5-state hauler dataset"""
        with open(os.path.join(self.workspace, 'five_state_haulers.json'), 'r') as f:
            self.data['haulers'] = json.load(f)
        
        with open(os.path.join(self.workspace, 'vt_facilities.json'), 'r') as f:
            self.data['facilities'] = json.load(f)
            
        print(f"Loaded {len(self.data['haulers'])} haulers")
        print(f"Loaded {len(self.data['facilities'])} VT facilities")
        
    def analyze_coverage(self):
        """Analyze current state coverage"""
        states = {}
        for h in self.data['haulers']:
            state = h.get('state', 'Unknown')
            states[state] = states.get(state, 0) + 1
        
        analysis = {
            'total_haulers': len(self.data['haulers']),
            'total_facilities': len(self.data['facilities']),
            'by_state': states,
            'new_england_states': ['VT', 'NH', 'MA', 'ME', 'CT', 'RI'],
            'mid_atlantic_states': ['NY', 'NJ'],
            'complete_coverage': ['VT'],
            'partial_coverage': ['NH', 'MA', 'NY', 'NJ'],
            'missing_coverage': ['ME', 'CT', 'RI']
        }
        
        return analysis
    
    def create_expansion_plan(self):
        """Create systematic expansion plan"""
        plan = {
            'phase_a_new_england': {
                'description': 'Complete New England coverage (VT, NH, MA, ME, CT, RI)',
                'states': {
                    'VT': {
                        'status': 'complete',
                        'haulers': 341,
                        'facilities': 212,
                        'data_source': 'VT DEC Solid Waste Program',
                        'quality': 'gold_standard'
                    },
                    'NH': {
                        'status': 'partial',
                        'haulers': 49,
                        'data_source': 'Cross-reference from VT permits',
                        'quality': 'cross_reference',
                        'action': 'Research NH DES registered hauler list'
                    },
                    'MA': {
                        'status': 'partial',
                        'haulers': 53,
                        'data_source': 'Cross-reference from VT permits',
                        'quality': 'cross_reference',
                        'action': 'Research MassDEP solid waste transporter database'
                    },
                    'ME': {
                        'status': 'research_in_progress',
                        'haulers': 0,
                        'data_source': 'Maine DEP',
                        'files': ['me_hazardous_transporters.pdf'],
                        'action': 'Parse PDFs, request non-hazardous transporter list'
                    },
                    'CT': {
                        'status': 'research_in_progress',
                        'haulers': 0,
                        'data_source': 'CT DEEP',
                        'files': ['deep-waste-transporter-list.pdf'],
                        'action': 'Download and parse transporter list PDF'
                    },
                    'RI': {
                        'status': 'research_in_progress',
                        'haulers': 0,
                        'data_source': 'RI Resource Recovery Corporation',
                        'files': ['ri_hauler_list.pdf'],
                        'action': 'Parse PDF (updated 8/2024)'
                    }
                }
            },
            'phase_b_data_enrichment': {
                'description': 'Deepen existing state data',
                'tasks': [
                    'Research NYSDEC Part 364 waste transporter permits',
                    'Research NJDEP A-901 licensed transporters',
                    'Geocode remaining 224 VT addresses',
                    'Verify NH/MA cross-referenced haulers with state permits'
                ]
            },
            'phase_c_website_enrichment': {
                'description': 'Crawl and verify website data',
                'tasks': [
                    'Verify generated website patterns for all 476 haulers',
                    'Extract hours, services, contact info from websites',
                    'Add customer review aggregation',
                    'Validate business information'
                ]
            }
        }
        
        return plan
    
    def save_expansion_plan(self, plan, analysis):
        """Save the expansion plan and analysis"""
        output = {
            'analysis': analysis,
            'plan': plan,
            'metadata': {
                'created': datetime.now().isoformat(),
                'version': '2.0'
            }
        }
        
        with open(os.path.join(self.workspace, 'expansion_plan.json'), 'w') as f:
            json.dump(output, f, indent=2)
        
        print(f"✅ Saved expansion_plan.json")
        
    def generate_research_summary(self):
        """Generate markdown research summary"""
        summary = """# Waste Directory V2 - Data Expansion Research

## Executive Summary

**Current State:** 476 haulers across 5 states (VT, NH, MA, NY, NJ)  
**Target State:** 8-state coverage with complete New England + Mid-Atlantic  
**New Data Sources Identified:** 6 state databases, 3 PDFs downloaded  
**Estimated Additional Haulers:** 200-400 (based on state populations and VT ratios)

## Data Source Inventory

### ✅ Complete (Gold Standard)
| State | Source | Records | Format |
|-------|--------|---------|--------|
| VT | DEC Solid Waste Program | 341 haulers + 212 facilities | JSON/CSV |

### 🔄 In Progress
| State | Source | Status | Files |
|-------|--------|--------|-------|
| ME | DEP | PDF downloaded | me_hazardous_transporters.pdf |
| RI | RIRRC | PDF downloaded | ri_hauler_list.pdf (8/2024) |
| CT | DEEP | Located | deep-waste-transporter-list.pdf |
| NH | DES | Research needed | - |
| MA | MassDEP | Research needed | Hazardous waste list only |

### ⏳ Research Needed
| State | Source | Contact |
|-------|--------|---------|
| NY | NYSDEC Part 364 | transport@dec.ny.gov |
| NJ | NJDEP A-901 | wastedecals.nj.gov |

## Key Contacts

| State | Agency | Contact | Phone | Email |
|-------|--------|---------|-------|-------|
| ME | DEP | Jane LaPierre | 207-441-8450 | jane.m.lapierre@maine.gov |
| NH | DES | - | - | solidwasteinfo@des.nh.gov |
| CT | DEEP | - | 860-424-3023 | - |
| RI | RIRRC | - | - | commercial@rirrc.org |

## Next Actions

1. **Immediate:** Parse downloaded PDFs (RI, ME)
2. **This Week:** Download CT transporter list, research NH/MA databases
3. **This Month:** Research NY/NJ databases, geocode remaining addresses
4. **Ongoing:** Website verification and enrichment

## Technical Notes

- VT facilities CSV has 212 certified facilities with full coordinates
- All VT haulers have geocoded addresses (312 at address-level precision)
- PDF parsing requires external tools or manual extraction
- Brave Search API operational for real-time research

---
*Generated: {date}*
""".format(date=datetime.now().strftime('%Y-%m-%d'))
        
        with open(os.path.join(self.workspace, 'RESEARCH_SUMMARY.md'), 'w') as f:
            f.write(summary)
        
        print(f"✅ Saved RESEARCH_SUMMARY.md")

def main():
    expander = WasteDirectoryExpander('/root/.openclaw/workspace/waste-directory')
    expander.load_existing_data()
    analysis = expander.analyze_coverage()
    plan = expander.create_expansion_plan()
    expander.save_expansion_plan(plan, analysis)
    expander.generate_research_summary()
    
    print("\n" + "="*60)
    print("DATA EXPANSION FRAMEWORK COMPLETE")
    print("="*60)
    print(f"\nCurrent Coverage:")
    print(f"  - Total Haulers: {analysis['total_haulers']}")
    print(f"  - Total Facilities: {analysis['total_facilities']}")
    print(f"  - States Covered: {len(analysis['by_state'])}")
    print(f"\nExpansion Targets:")
    print(f"  - New England Completion: ME, CT, RI")
    print(f"  - Data Deepening: NH, MA, NY, NJ")
    print(f"  - Website Enrichment: All 476+ haulers")
    
if __name__ == '__main__':
    main()
