# Waste Directory - Vercel Deployment Guide

## 🎯 What You're Deploying

A **5-state waste hauler directory** with interactive maps:
- 476 haulers across VT, NH, MA, NY, NJ
- 10 confirmed disposal facilities
- Quality-flagged data (gold standard vs cross-reference)
- Interactive map with search and filter

## 📦 Step 1: Get the Files

1. Download `waste-directory-deploy.tar.gz` (attached or provided)
2. Extract to your computer:
   ```bash
   # Mac/Linux:
   tar -xzf waste-directory-deploy.tar.gz
   
   # Windows: Use 7-Zip or WinRAR
   ```

## 🔧 Step 2: Create GitHub Repo

1. Go to [github.com](https://github.com)
2. Sign in (or create free account)
3. Click green **"New"** button
4. Name it: `waste-directory`
5. Make it **Public**
6. Click **Create repository**

## 📤 Step 3: Upload Files to GitHub

**Easy way (GitHub web interface):**

1. In your new repo, click **"uploading an existing file"**
2. Drag entire `waste-directory/` folder into the upload area
3. Commit message: `Initial upload`
4. Click **Commit changes**

**OR Command line way:**
```bash
cd waste-directory
git init
git add .
git commit -m "Initial upload"
git remote add origin https://github.com/YOUR_USERNAME/waste-directory.git
git push -u origin main
```

## 🚀 Step 4: Deploy to Vercel

1. Go to [vercel.com](https://vercel.com)
2. Click **"Sign Up"** → Choose **"Continue with GitHub"**
3. Authorize Vercel to access your repos
4. Click **"Add New Project"**
5. Find `waste-directory` in the list
6. Click **"Import"**
7. Leave all settings as default
8. Click **"Deploy"**
9. Wait ~1 minute

## ✅ Step 5: Your Site is Live

- Vercel gives you a URL like: `https://waste-directory-abc123.vercel.app`
- Click it — your directory loads immediately
- **Free forever** (Vercel hobby plan)

## 📍 What You'll See

**Pages:**
- `/overview.html` — Dashboard with stats
- `/northeast.html` — 5-state hauler map
- `/index.html` — Vermont gold standard
- `/profiles.html` — Individual hauler profiles

**Colors on the map:**
- 🟡 Yellow = Vermont (gold standard)
- 🟠 Orange = New Hampshire
- 🔵 Blue = Massachusetts, NY, NJ

## 🔄 Updates

To update later:
1. Make changes locally
2. `git add .`
3. `git commit -m "Your update"`
4. `git push`
5. Vercel auto-deploys in seconds

## 🆘 Troubleshooting

**"Project not found":**
- Make sure GitHub repo is Public

**"Build failed":**
- This is static HTML, no build needed — check you uploaded the right folder

**Blank page:**
- Make sure you're opening `overview.html` or `northeast.html`

## 📞 Questions?

The data files are:
- `five_state_haulers.json` — All 476 haulers
- `vt_facilities_seed.json` — 10 confirmed facilities

Everything else is the web interface.

**Done! You now have a live waste industry directory.**
