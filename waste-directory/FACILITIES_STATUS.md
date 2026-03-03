# Vermont Disposal Facilities — Status Report

## ✅ What We Have (Seed Data)

### Confirmed Facilities (10)
| Facility | Town | Type | Source |
|----------|------|------|--------|
| Chittenden Solid Waste District | South Burlington | Transfer/Recycling/HHW | Hauler cross-ref |
| Central Vermont Solid Waste Management District | Montpelier | Transfer/Recycling/HHW | Hauler cross-ref |
| Southern Windsor/Windham SWMD | Ascutney | Transfer/Recycling/HHW | Hauler cross-ref |
| Northeast Kingdom WMD | Derby | Transfer/Recycling | Hauler cross-ref |
| Northwest Vermont SWD | Stowe | Transfer/Recycling | Hauler cross-ref |
| Addison County SWMD | Middlebury | Transfer/Recycling | Hauler cross-ref |
| Rutland County SWD | Rutland | Transfer/Recycling/HHW | Hauler cross-ref |
| Windham SWMD | Brattleboro | Transfer/Recycling/HHW | Hauler cross-ref |
| Lamoille Regional SWMD | Morristown | Transfer/Recycling | Hauler cross-ref |
| New England Waste Services (Coventry Landfill) | Coventry | Landfill | VT DEC reference |

### Estimated Universe (210 total)
| Category | Est. Count | Status |
|----------|-----------|--------|
| Transfer Stations | 80 | ❌ Need to identify |
| Recycling Centers | 50 | ❌ Need to identify |
| Composting Facilities | 25 | ❌ Need to identify |
| Landfills | 5 | ⚠️ Partial (1 confirmed) |
| C&D Processors | 20 | ❌ Need to identify |
| HHW Collection | 30 | ⚠️ Partial (district HHW) |

---

## 🔍 What We Know Exists (From VT DEC)
- **210 certified facilities** in Vermont
- **Universal Recycling Materials Management Map** at `anrmaps.vermont.gov`
- **Facility certification database** (inaccessible via web)

---

## 🚧 What We Tried (All Blocked)
| Source | Result |
|--------|--------|
| EPA ECHO | Locked down |
| VT DEC MapServer | 404 |
| VT DEC Facility DB | 404 |
| RCRAInfo | 404 |
| Local district websites | Incomplete (download behind paywalls) |
| FOIA/Records request | Not yet attempted |

---

## 🎯 Next Step Options

### Option A: Manual Research (2-3 days, guaranteed results)
- Research each town website one-by-one
- Document transfer stations, town dumps, recycling centers
- Castle proper names, addresses, hours, materials accepted
- Tedious but you get the data.

### Option B: VT DEC Data Request (1-4 weeks)
- Official public records request for facility database export
- Free but government timeline.
- Result: Certified 210-facility list with permit details.

### Option C: ArcGIS Web Scrape (technical)
- VT's Materials Management Map is an ArcGIS web app
- Can potentially scrape the underlying REST endpoints
- Requires URL pattern discovery.

### Option D: Trade Association Purchase ($)
- NWRA or SWANA member directories
- Instant comprehensive data
- Costs unknown but commercial.

---

## 💡 Recommendation

**Immediate:** Proceed with **Option A** — manual research of top 20-30 facilities (major towns + all districts). Gets you a solid foundation fast.

**Parallel:** Submit **Option B** — VT DEC records request for full 210-facility list. Takes weeks but gets official complete data.

**Result:** Working facility directory in days, complete official data in weeks.

---

## 📁 Files
- `vt_facilities_seed.json` — 10 confirmed facilities + research roadmap

Want me to start manual research on the major facilities?
