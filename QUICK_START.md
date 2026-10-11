# ⚡ Quick Start Guide

Deploy both your Streamlit dashboard and executive report in 10 minutes!

---

## 🚀 30-Second Overview

You have **two separate deployments**:

```
1️⃣  Streamlit Cloud (Interactive Dashboard)
    → For: Live data exploration & team collaboration
    → Deploy: 3 minutes

2️⃣  GitHub Pages (Executive Report)
    → For: Executive presentations & storytelling
    → Deploy: 2 minutes
```

---

## ✅ Prerequisites

- GitHub account (free)
- Git installed locally
- This repository

---

## 📱 Deploy Streamlit Dashboard (3 min)

### Step 1: Push to GitHub
```bash
cd data_analysis
git init
git add .
git commit -m "Add Streamlit dashboard"
git remote add origin https://github.com/YOUR_USERNAME/data_analysis.git
git branch -M main
git push -u origin main
```

### Step 2: Deploy on Streamlit Cloud
1. Go to [share.streamlit.io](https://share.streamlit.io/)
2. Click "New app"
3. Select:
   - **Repo:** `YOUR_USERNAME/data_analysis`
   - **Main file:** `dashboard.py`
4. Click "Deploy" ✅

**Live at:** `https://your-custom-name.streamlit.app/`

---

## 📄 Deploy Executive Report (2 min)

### Step 1: Enable GitHub Pages
1. Go to GitHub → Settings → Pages
2. Select:
   - **Source:** Deploy from a branch
   - **Branch:** main
   - **Directory:** /(root)
3. Save ✅

**Live at:** `https://YOUR_USERNAME.github.io/data_analysis/`

Auto-updates when you push data changes!

---

## 📊 What You Get

### Streamlit Dashboard
✨ Interactive features:
- Real-time filtering by day & category
- Custom data table with sorting
- CSV download button
- Responsive design
- Live metric updates

### Executive Report
✨ Narrative features:
- Executive summary
- Key findings highlighted
- Business impact metrics
- Actionable recommendations
- Professional styling
- Mobile-friendly

---

## 🔄 Update Your Data

Both platforms update together:

```bash
# 1. Update your CSV
cp new_events.csv data/toronto_tech_events_synthetic.csv

# 2. Push to GitHub
git add data/
git commit -m "Update event data"
git push

# ✅ Both platforms auto-update in 1-3 minutes!
```

---

## 🎯 Share Your Work

### For Interactive Exploration
```
https://your-custom-name.streamlit.app/
```

### For Executive Presentations
```
https://YOUR_USERNAME.github.io/data_analysis/
```

### For Quick Sharing
```
Email/Slack:
📊 Dashboard: https://your-custom-name.streamlit.app/
📄 Report: https://YOUR_USERNAME.github.io/data_analysis/
```

---

## 🆘 Need Help?

**Streamlit Cloud not deploying?**
- Check `requirements.txt` exists
- Verify `dashboard.py` in root directory
- Check build logs in Streamlit Cloud

**GitHub Pages not showing?**
- Ensure Pages is enabled in Settings
- Hard refresh: `Ctrl+Shift+R`
- Wait 2-3 minutes for GitHub to build

**Data not updating?**
- Push all changes: `git push`
- Wait 1-3 minutes for auto-regeneration
- Check GitHub Actions log for errors

---

## 📚 Full Documentation

- **Detailed Deployment:** See `DEPLOYMENT_GUIDE.md`
- **Architecture Details:** See `CLAUDE.md`
- **Code Documentation:** See inline comments in scripts

---

## ✨ You're Done!

Both platforms are live and will auto-update when you push changes. 🎉

**Next Step:** Share the links with your manager!

```
Hi [Manager],

I've analyzed Toronto tech events and created interactive 
tools for exploration:

📊 Interactive Dashboard: https://your-custom-name.streamlit.app/
📄 Executive Report: https://YOUR_USERNAME.github.io/data_analysis/

Key insight: Tech events peak on Wednesday & Friday, 
6-8 PM — 49% of all events! 

Let's discuss how we can leverage this for networking.
```

---

**Estimated total setup time:** 10 minutes  
**Auto-update time:** 1-3 minutes  
**Time to presentation-ready:** Now! 🚀