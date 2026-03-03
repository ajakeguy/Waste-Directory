# Northeast Waste Hauler Directory

## 🎯 Mission Accomplished

Built a **multi-state waste hauler directory** covering Vermont, New Hampshire, and Massachusetts with **data quality flagging** so you know exactly what's solid vs. what needs work.

---

## 📊 Directory Overview

| State | Haulers | Data Quality | Status |
|-------|---------|--------------|--------|
| **Vermont** | 341 | ⭐ Gold Standard | Complete state permit database + geocoded |
| **New Hampshire** | 49 | ⚠️ Cross-Reference | From VT permit cross-check |
| **Massachusetts** | 53 | ⚠️ Cross-Reference | From VT permit cross-check |
| **TOTAL** | **443** | Mixed | Best available data |

---

## ✅ What Was Built

### 1. Vermont (The Gold Standard)
- **536 total haulers** in source data
- **341 VT-based** companies
- **312 geocoded** with address-level precision (58%)
- **Source:** Vermont Department of Environmental Conservation (DEC)
- **Fields:** Permit ID, Company, Contact, Address, Phone, Waste Types, Bear-Resistant, Service Area

**Geocoding Breakdown:**
- ✓ 312: Address-level coordinates (street address geocoded)
- ✗ 224: PO Boxes, out-of-state locations, or ungeocodable addresses

### 2. New Hampshire (Partial)
- **49 haulers** identified
- **Source:** Cross-referenced from VT permits (companies permitted in VT, based in NH)
- **Quality:** Basic info only (name, town, phone)
- **Needs:** NH state permit verification

### 3. Massachusetts (Partial)
- **53 haulers** identified
- **Source:** Cross-referenced from VT permits
- **Quality:** Basic info only
- **Needs:** MassDEP permit verification

---

## 📁 Files

### Main Files
- `northeast.html` — **Multi-state web interface** with quality indicators
- `northeast_haulers.json` — **Combined dataset** (443 haulers)
- `index.html` — Vermont-only interface
- `profiles.html` — Detailed hauler profiles

### State-Specific Data
- `vt_haulers_complete.json` — 341 VT haulers
- `nh_haulers_partial.json` — 49 NH haulers
- `ma_haulers_partial.json` — 53 MA haulers

### Source Data
- `vermont_haulers_enriched.json` — 536 haulers with geocoding
- `scrape_vermont.py` — VT data extraction script
- `enrich_data.py` — Geocoding script
- `build_northeast.py` — Multi-state dataset builder

---

## 🗺️ Data Quality System

### Gold Standard (Vermont)
- ✓ State government permit database
- ✓ Official permit IDs
- ✓ Annual renewal tracking
- ✓ Phone/address verification
- ✓ Geocoded locations

### Cross-Reference (NH, MA)
- ⚠️ Identified via VT permit cross-check
- ⚠️ Likely valid (they're permitted in VT)
- ⚠️ Missing official state permits
- ⚠️ Needs verification

### Quality Flags in Data
```json
{
  "data_source": "VT",
  "data_quality": "complete_state_permit_data",
  "location_quality": "address_level",
  "state_source": "VT"
}
```

---

## 🚀 How to Use

### View the Directory
```bash
cd waste-directory
python3 server.py
# Open http://localhost:8000/northeast.html
```

### Filter by Quality
- Use the "All Data Quality" dropdown to filter:
  - **Address Level:** Only show precisely geocoded haulers
  - **Missing Location:** Show haulers needing location data

### Color Coding
- **🟡 Yellow:** Vermont haulers (Gold Standard)
- **🟠 Orange:** New Hampshire haulers (Cross-Reference)
- **🔵 Blue:** Massachusetts haulers (Cross-Reference)

---

## 📈 Next Steps

### Phase 3 Options

**Option A: Expand East**
- Maine, Rhode Island, Connecticut
- Challenge: Variable data availability

**Option B: Deepen Vermont**
- Geocode remaining 224 addresses (manual research)
- Add website URLs (crawl those domain patterns)
- Add customer reviews, photos, hours

**Option C: Verify NH/MA**
- Contact NH DES when their system is back
- Apply for MassDEP data access
- Manual verification of cross-referenced haulers

**Option D: Industry Sources**
- Waste Dive directory
- SWANA (Solid Waste Association of North America)
- NWRA (National Waste & Recycling Association)

---

## 🎯 What's Strong vs. Weak

### Strong
- **Vermont coverage:** Complete, official, geocoded
- **Multi-state interface:** Works, shows quality clearly
- **NH/MA presence:** Good starting point for expansion

### Weak
- **NH/MA data:** Needs official state verification
- **Geocoding gaps:** 224 addresses need work (mostly PO boxes)
- **Website discovery:** Generated patterns but need verification

---

## 📞 Contact

This is your living directory. Add to it, improve it, expand it.

**Built:** March 2026
**Last Updated:** March 2026
**Data Sources:** Vermont DEC, VT permit cross-references
