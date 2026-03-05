# Waste Directory V2 - Data Expansion Research Summary

**Research Date:** March 5, 2026
**Brave Search API:** Active and operational

---

## State-by-State Data Source Assessment

### ✅ VERMONT (Gold Standard - Existing)
- **Haulers:** 341 VT-based (from 536 total permits)
- **Facilities:** 212 certified facilities (CSV downloaded)
- **Source:** VT DEC Solid Waste Program
- **Data Quality:** Complete with geocoding (312 address-level)
- **Download:** `vt_facilities.csv` - 212 facilities with coordinates, services, contact info

### 🔄 MAINE (In Progress)
- **Haulers:** Need to extract from PDF
- **Source:** Maine DEP
- **Files Downloaded:**
  - `me_hazardous_transporters.pdf` - Active hazardous waste transporters
- **Missing:** Non-hazardous waste transporter list (mentioned on website)
- **Contact:** Jane LaPierre (207-441-8450) for manifest forms

### 🔄 CONNECTICUT (In Progress)
- **Haulers:** PDF list available
- **Source:** CT DEEP
- **URL:** `deep-waste-transporter-list.pdf`
- **Status:** Need to download and parse

### 🔄 RHODE ISLAND (In Progress)
- **Haulers:** PDF list downloaded
- **Source:** RI Resource Recovery Corporation
- **File:** `ri_hauler_list.pdf` (updated 8/2024)
- **Note:** DEM doesn't license solid waste haulers - RIRRC maintains the list

### 🔄 NEW HAMPSHIRE (Research Needed)
- **Haulers:** 49 cross-referenced from VT permits
- **Source:** NH DES
- **Registration:** Required but list not yet located
- **Contact:** solidwasteinfo@des.nh.gov

### 🔄 MASSACHUSETTS (Research Needed)
- **Haulers:** 53 cross-referenced from VT permits
- **Source:** MassDEP
- **Status:** Hazardous waste transporter list available
- **Missing:** Solid waste hauler database

### 🔄 NEW YORK (Research Needed)
- **Source:** NYSDEC Part 364 Waste Transporter Permits
- **URL:** dec.ny.gov/waste-management/waste-transporters
- **Status:** Need to locate downloadable list

### 🔄 NEW JERSEY (Research Needed)
- **Source:** NJDEP A-901 Licensed Solid Waste Transporters
- **URL:** dep.nj.gov/wastedecals/
- **Status:** Need to locate downloadable list

---

## Vermont Facilities Data (CSV Downloaded)

**Fields Available:**
- ID, SWID, Name, Type
- Services: Recycling, Trash, EWaste, HHW, FoodScraps, CD, CleanWood, LeafYardDebris
- Address, Town, State, Zip, County
- Mailing Address info
- Telephone, Email, Website
- Active status, LastVisitDate
- Latitude, Longitude (geocoded!)

**Facility Types:**
- Transfer Station
- Recycling Center
- Food Scraps Management Facility
- Compost Facility
- Landfill
- Hazardous Waste (HHW) facilities

**Count:** 212 certified facilities

---

## Data Expansion Plan

### Phase A: New England Completion
1. ✅ Vermont facilities (CSV downloaded)
2. 🔄 Process Maine hazardous transporters PDF
3. 🔄 Process Rhode Island hauler list PDF
4. 🔄 Download & process Connecticut transporter list
5. ⏳ Research New Hampshire hauler registration list

### Phase B: Deepen Existing States
1. ⏳ Research NYSDEC Part 364 transporter database
2. ⏳ Research NJDEP A-901 licensed transporters
3. ⏳ Geocode remaining 224 VT addresses
4. ⏳ Research NH/MA state permits for cross-referenced haulers

### Phase C: Data Enrichment
1. ⏳ Crawl website patterns for all haulers
2. ⏳ Add hours, services, reviews
3. ⏳ Verify business information

---

## Next Actions

1. Parse PDFs (ME, RI) to extract structured data
2. Download CT transporter list
3. Research NY/NJ state databases
4. Merge new data into master dataset
5. Geocode remaining addresses
6. Enrich with web data

---

## Key Contacts for Follow-up

| State | Agency | Contact | Purpose |
|-------|--------|---------|---------|
| Maine | DEP | Jane LaPierre (207-441-8450) | Non-haz transporter list |
| NH | DES | solidwasteinfo@des.nh.gov | Hauler registration list |
| CT | DEEP | (website) | Transporter permits |
| RI | RIRRC | commercial@rirrc.org | Hauler list updates |
