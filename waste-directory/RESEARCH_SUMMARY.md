# Waste Directory V2 - Data Expansion Research

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
*Generated: 2026-03-05*
