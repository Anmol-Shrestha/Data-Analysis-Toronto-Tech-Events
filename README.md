# Toronto Tech Events Analysis 📊

Analysis of Toronto tech and AI events to identify networking patterns and optimal attendance strategies.

## 🎯 Goal

Analyze event data to discover actionable insights about when and where tech networking happens in Toronto.

**Key Finding:** 49% of events occur on Wednesday and Friday from 6:00 PM - 8:00 PM.

## 🛠️ Technologies Used

- **Python** — Data processing and analysis
- **Pandas** — Data manipulation
- **Plotly** — Interactive visualizations
- **Streamlit** — Interactive web dashboard
- **GitHub Actions** — Automated report generation

## 📊 Results

| Resource | Purpose |
|----------|---------|
| **[Executive Report](https://anmol-shrestha.github.io/Data-Analysis-Toronto-Tech-Events/)** | Narrative findings with business recommendations and key metrics |
| **[Interactive Dashboard](https://data-analysis-toronto-tech-events.streamlit.app/)** | Explore data with filters, charts, and custom sorting |

---

## 📁 Project Structure

```
.
├── dashboard.py                      # Streamlit interactive dashboard
├── generate_executive_report.py      # Report generator
├── analyze_events.py                 # CLI analysis script
├── index.html                        # Generated executive report
├── CLAUDE.md                         # Code architecture
├── DEPLOYMENT_GUIDE.md               # Deployment instructions
├── README.md                         # This file
├── requirements.txt                  # Dependencies
├── data/
│   └── toronto_tech_events_synthetic.csv
└── .github/workflows/
    └── generate-dashboard.yml        # Auto-generates report on push
```

## 📈 Data Format

**Source:** Synthetically generated dataset (150 events)

CSV columns:
- `event_id` — Unique identifier
- `event_name` — Event name
- `category` — Category (AI, Cloud & DevOps, Software Development, Data Engineering)
- `date` — Event date (YYYY-MM-DD)
- `day_of_week` — Day name
- `start_time` — Start time (HH:MM)
- `end_time` — End time (HH:MM)
- `venue` — Location

## 🔄 Updating Data

Replace the CSV and push to GitHub:

```bash
cp new_events.csv data/toronto_tech_events_synthetic.csv
git add data/
git commit -m "Update event data"
git push
```

Both dashboard and report auto-update in 1-3 minutes.

## 📚 Documentation

- **Code Architecture:** `CLAUDE.md`
- **Deployment:** `DEPLOYMENT_GUIDE.md`

## 🆘 Support

**Streamlit Issues:** [docs.streamlit.io](https://docs.streamlit.io/)  
**GitHub Pages Issues:** [docs.github.com/pages](https://docs.github.com/en/pages)

---

**Dataset:** 150 Toronto Tech Events (Synthetic)  
**Analysis Date:** October 2026