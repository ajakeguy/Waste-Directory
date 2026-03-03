# Data Enrichment Specification
## Vermont Waste Hauler Directory

### Current Data Captured (Phase 1 - Complete ✅)

From Vermont DEC Database:
- ✅ **Permit ID** — Unique identifier (e.g., "2491")
- ✅ **Company Name** — Legal/DBA name (e.g., "802 Clean Out Services LLC")
- ✅ **Contact Person** — Primary contact name
- ✅ **Street Address** — Physical address
- ✅ **Town/City** — Municipality
- ✅ **State** — VT, NH, MA, NY, QC, etc.
- ✅ **Phone Number** — Contact phone
- ✅ **Permit Year** — Current permit year (e.g., "2025")
- ✅ **Waste Types** — S (Solid), H (Hazardous), R (Recyclable), M (Medical)
- ✅ **Bear Resistant** — Yes/No flag
- ✅ **Service Area** — Geographical coverage notes

---

### Phase 2: Enrichable Data Fields

#### 🏢 Company Profile
| Field | Data Source | Method | Priority |
|-------|-------------|--------|----------|
| **Website URL** | Company website, Google search | Web scraping, manual verification | High |
| **Email Address** | Website contact forms | Scraping, outreach | High |
| **Year Established** | Business registries, Secretary of State | State database lookup | Medium |
| **Business Structure** | LLC, Corp, Sole Prop | Secretary of State | Low |
| **Employee Count** | LinkedIn, company info | Scraping, estimate | Medium |
| **Annual Revenue** | Industry estimates | External databases | Low |

#### 📞 Extended Contact
| Field | Data Source | Method | Priority |
|-------|-------------|--------|----------|
| **Secondary Phone** | Website, listings | Scraping | Low |
| **Toll-Free Number** | Company website | Scraping | Low |
| **Fax Number** | Company info | Scraping | Low |
| **Emergency Contact** | 24/7 line | Direct inquiry | Medium |
| **Dispatch Number** | Operations | Direct inquiry | Medium |

#### 🗑️ Service Details
| Field | Data Source | Method | Priority |
|-------|-------------|--------|----------|
| **Container Sizes** | Website, brochures | Scraping, documents | High |
| **Pickup Frequencies** | Service listings | Scraping | Medium |
| **Accepted Materials** (Detailed) | Website, regulations | Content extraction | High |
| **Specialized Services** | Electronics, tires, etc. | Scraping, inquiry | Medium |
| **Equipment Types** | Roll-off, front-load, rear-load | Visual identification | Medium |
| **Fleet Size** | Industry reports, estimates | Research | Low |
| **Route Info** | Coverage areas | Geospatial analysis | Medium |

#### 🗺️ Geographic Data
| Field | Data Source | Method | Priority |
|-------|-------------|--------|----------|
| **Precise Geocoding** | Google Maps API, Mapbox | API geocoding | High |
| **Counties Served** | Service area mapping | Geospatial analysis | Medium |
| **Service Radius** | Operational data | Calculation | Low |
| **Zone Coverage** | Municipal contracts | Research | Medium |
| **Route Density** | Stop frequency | Data aggregation | Low |

#### 🛡️ Certifications & Compliance
| Field | Data Source | Method | Priority |
|-------|-------------|--------|----------|
| **OSHA Certified** | OSHA database | Lookup | Medium |
| **Hazmat Endorsement** | DOT records | Federal database | Medium |
| **ISO Certification** | ISO registry | Lookup | Low |
| **EPA ID Number** | EPA database | Lookup | Medium |
| **USDOT Number** | FMCSA database | Federal lookup | Medium |
| **MC Authority** | FMCSA | Federal lookup | Medium |
| **Insurance Coverage** | COI documents | Direct inquiry | Medium |
| **Safety Rating** | FMCSA SMS | Federal database | Medium |

#### 🕒 Operations
| Field | Data Source | Method | Priority |
|-------|-------------|--------|----------|
| **Hours of Operation** | Website, listings | Scraping | High |
| **Emergency Hours** | 24/7 availability | Scraping, inquiry | Medium |
| **Languages Spoken** | Company info | Scraping | Low |
| **Payment Methods** | Website | Scraping | Low |
| **Billing Terms** | Net 30, etc. | Direct inquiry | Low |
| **Contract Required** | Terms of service | Scraping | Low |

#### ⭐ Reputation & Reviews
| Field | Data Source | Method | Priority |
|-------|-------------|--------|----------|
| **Google Rating** | Google Business API | API integration | High |
| **Google Review Count** | Google Business | API integration | High |
| **Yelp Rating** | Yelp API | API integration | Medium |
| **BBB Rating** | Better Business Bureau | Scraping | Medium |
| **Facebook Rating** | Facebook API | API integration | Low |
| **Customer Testimonials** | Website | Scraping | Low |

#### 📸 Media
| Field | Data Source | Method | Priority |
|-------|-------------|--------|----------|
| **Company Logo** | Website | Image scraping | Medium |
| **Fleet Photos** | Website, social media | Image scraping | Low |
| **Facility Photos** | Website, Google Maps | Image scraping | Low |
| **Equipment Gallery** | Website | Image scraping | Low |

#### 🔗 Digital Presence
| Field | Data Source | Method | Priority |
|-------|-------------|--------|----------|
| **LinkedIn Profile** | LinkedIn search | Scraping | Medium |
| **Facebook Page** | Social search | Scraping | Medium |
| **Twitter/X Handle** | Social search | Scraping | Low |
| **Instagram Handle** | Social search | Scraping | Low |
| **YouTube Channel** | Social search | Scraping | Low |

#### 💰 Pricing Intelligence
| Field | Data Source | Method | Priority |
|-------|-------------|--------|----------|
| **Service Rates** | Quotes, websites | Mystery shopping | Low |
| **Competitive Position** | Market analysis | Data aggregation | Low |
| **Discount Programs** | Website | Scraping | Low |

---

### Data Enrichment Methods

#### 1. **Automated Web Scraping** (High Scale, Medium Quality)
- Company websites
- Business directories (Yelp, BBB, Angi)
- Social media profiles
- State/federal databases (where API access available)

#### 2. **API Integrations** (Medium Scale, High Quality)
- Google Places API (ratings, hours, photos)
- Mapbox/MapQuest (geocoding)
- FMCSA Portal (USDOT, safety ratings)
- EPA databases (hazmat permits)

#### 3. **Direct Outreach** (Low Scale, Highest Quality)
- Email campaigns to haulers
- Phone verification calls
- Survey forms
- Data contribution incentives

#### 4. **Crowdsourcing** (Medium Scale, Variable Quality)
- User submissions
- Community verification
- Review aggregation

---

### Implementation Priority

**Phase 2A (Immediate - Low-Hanging Fruit):**
1. Geocoding all addresses (Mapbox/Google)
2. Website discovery (Google search scraping)
3. Phone format standardization
4. Basic web presence check

**Phase 2B (Short-term):**
1. Google Business profile linking
2. Hours of operation scraping
3. Service details from websites
4. Social media profile discovery

**Phase 2C (Medium-term):**
1. FMCSA/USDOT verification
2. Insurance certificate collection
3. Safety rating lookups
4. Fleet/equipment details

**Phase 2D (Long-term):**
1. Full website content extraction
2. Customer review monitoring
3. Pricing intelligence
4. Competitive benchmarking

---

### Data Quality Standards

| Field Type | Validation | Confidence Score |
|------------|------------|------------------|
| **Direct from State** | Primary source | 100% |
| **API Verified** | Google/official | 90-95% |
| **Web Scraped** | Company website | 70-85% |
| **User Submitted** | Community | 50-65% |
| **Estimated** | Algorithmic | 30-50% |

---

### Estimated Enrichment Coverage

| Data Category | Current | Potential | Method |
|--------------|---------|-----------|--------|
| **Basic Contact** | 100% | 100% | Primary data |
| **Geocoding** | 0% | 95% | API |
| **Website** | 0% | 60% | Scraping |
| **Hours** | 0% | 40% | Scraping |
| **Rating** | 0% | 35% | API |
| **Certifications** | 0% | 25% | Federal DB |
| **Fleet Details** | 0% | 15% | Direct inquiry |

---

### User Value of Enrichment

**High Value to Users:**
1. ✅ Service types accepted
2. ✅ Hours of operation
3. ✅ Contact methods (email/web form)
4. ✅ Service area map
5. ✅ Customer ratings
6. ✅ Pricing transparency

**Medium Value:**
1. Equipment/container options
2. Certifications/licenses
3. Years in business
4. Fleet size
5. Insurance verification

**Lower Value (Nice to Have):**
1. Social media links
2. Company history
3. Employee count
4. Photo galleries

---

*This document serves as the roadmap for progressively enriching hauler profiles beyond the baseline state permit data.*
