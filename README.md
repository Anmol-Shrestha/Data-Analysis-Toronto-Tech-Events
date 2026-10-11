# Toronto Tech Events Analysis 📊

A data analysis project for Toronto tech/AI events with **two purpose-built deployments**: an interactive Streamlit dashboard for exploration and an executive report for storytelling.

## 🎯 Two Deployments, Two Audiences

| 📱 **Streamlit Dashboard** | 📄 **Executive Report** |
|---------------------------|------------------------|
| **For:** Team, analysts, explorers | **For:** Managers, executives, storytellers |
| Real-time filtering | Key findings highlighted |
| Live data exploration | Business impact metrics |
| CSV downloads | Actionable recommendations |
| Multi-tab interface | Professional narrative |
| **[Deploy here →](DEPLOYMENT_GUIDE.md#part-1-deploy-to-streamlit-cloud-)** | **[Deploy here →](DEPLOYMENT_GUIDE.md#part-2-deploy-executive-report-to-github-pages-)** |

## 📋 Key Finding

**Tech events in Toronto peak on Wednesday and Friday from 6:00 PM to 8:00 PM.**

Nearly **50% of all events (73 of 150)** occur on just these two days, creating a concentrated networking opportunity.

---

## 🚀 Quick Start

### Prerequisites
```bash
pip install pandas matplotlib seaborn plotly streamlit
```

### Deployment Options

**Option 1: Deploy Streamlit Dashboard to Cloud**
```bash
streamlit run dashboard.py  # Run locally first to test
```
Then deploy to [Streamlit Cloud](https://share.streamlit.io/) for your team.

**Option 2: Deploy Executive Report to GitHub Pages**
Push to GitHub and enable Pages in Settings. The report auto-generates on every data update.

**Option 3: Local Command-Line Analysis**
```bash
python analyze_events.py
```
Generates console statistics + PNG visualizations.

---

## 📁 Project Structure

```
.
├── data/
│   └── toronto_tech_events_synthetic.csv     # Event dataset
├── dashboard.py                              # Streamlit app (interactive)
├── generate_executive_report.py              # Report generator
├── analyze_events.py                         # CLI analysis script
├── index.html                                # Executive report (auto-generated)
├── CLAUDE.md                                 # Code architecture
├── DEPLOYMENT_GUIDE.md                       # Step-by-step deployment
├── QUICK_START.md                            # 10-minute guide
├── README.md                                 # This file
└── .github/workflows/
    └── generate-dashboard.yml                # Auto-generate report on push
```

---

## 📊 What Each Does

### Streamlit Dashboard (`dashboard.py`)
Interactive exploration tool deployed to Streamlit Cloud:
- 🔄 Real-time filtering by day & category
- 📑 4 tabs: Day Distribution, Time Windows, Categories, Data Table
- 💾 CSV download button
- 🎯 Custom sorting & searching
- 📊 Live metric cards

**Best for:** Team collaboration, data exploration, Q&A sessions

### Executive Report (`index.html`)
Narrative-driven report deployed to GitHub Pages:
- 🎯 Executive summary (the story)
- 📈 Key findings with supporting charts
- 💼 Business impact metrics
- ✅ 4 actionable recommendations
- 🎨 Professional styling

**Best for:** Presentations, decision-making, stakeholder communication

### Analysis Script (`analyze_events.py`)
Reproducible analysis for technical deep-dives:
- 🐍 Modular EventAnalyzer class
- 📋 Console statistics
- 🖼️ PNG chart exports

**Best for:** Reproducibility, automation, technical documentation

---

## 🌐 Deployment

### Streamlit Cloud (Interactive Dashboard)

1. Push to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io/)
3. Click "New app" → Select `dashboard.py`
4. Deploy ✅

**Live at:** `https://your-custom-name.streamlit.app/`

### GitHub Pages (Executive Report)

1. Push to GitHub
2. Settings → Pages → Deploy from `main` branch
3. Save ✅

**Live at:** `https://YOUR_USERNAME.github.io/data_analysis/`

**Auto-updates:** GitHub Actions regenerates the report whenever you push data changes.

---

## 🔄 Updating Data

Both deployments auto-update:

```bash
# Update your CSV
cp new_events.csv data/toronto_tech_events_synthetic.csv

# Push to GitHub
git add data/
git commit -m "Update event data"
git push

# ✅ Both platforms regenerate automatically in 1-3 minutes
```

---

## 📈 Data Format

Required CSV columns:
- `event_id` — Unique identifier
- `event_name` — Event name
- `category` — Category (AI, Cloud & DevOps, etc.)
- `date` — Event date (YYYY-MM-DD)
- `day_of_week` — Day name (Monday-Sunday)
- `start_time` — Start time (HH:MM)
- `end_time` — End time (HH:MM)
- `venue` — Location

---

## 🔧 Customization

**Change Executive Report Colors:**
Edit `generate_executive_report.py`:
```python
colors = ['#FF6B6B', '#95E1D3', ...]  # Your brand colors
```

**Change Streamlit Dashboard Colors:**
Edit `dashboard.py` chart functions.

**Update Analysis Logic:**
Modify `analyze_events.py` EventAnalyzer methods.

---

## 📚 Documentation

- **Quick Deployment:** `QUICK_START.md` (10 minutes)
- **Detailed Instructions:** `DEPLOYMENT_GUIDE.md`
- **Code Architecture:** `CLAUDE.md`
- **CLI Usage:** `analyze_events.py --help`

---

## 🎯 Use Cases

| Need | Use This |
|------|----------|
| Show your boss key findings | Executive Report |
| Let team explore data live | Streamlit Dashboard |
| Create automated reports | CLI Script |
| Reproduce analysis | analyze_events.py |
| Share insights quickly | GitHub Pages URL |

---

## 🚀 Next Steps

1. **Quick:** Read `QUICK_START.md` (5 min read)
2. **Deploy:** Follow `DEPLOYMENT_GUIDE.md` (10 min setup)
3. **Share:** Send both URLs to your team
4. **Iterate:** Update data → both platforms auto-regenerate

---

## 📞 Support

**Streamlit Issues:** [docs.streamlit.io](https://docs.streamlit.io/)  
**GitHub Pages Issues:** [docs.github.com/pages](https://docs.github.com/en/pages)  
**Python/Data Issues:** Check `CLAUDE.md` for code architecture

---

**Data:** 150 Toronto Tech Events | **Analysis:** October 2026 | **Purpose:** Strategic networking insights
