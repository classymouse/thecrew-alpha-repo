# The Crew Alpha Release - Quick Deployment Guide

## 📊 What You Have

Your alpha repository is ready at:
```
C:\Users\fvanb\AppData\Roaming\Kodi\addons\thecrew-alpha-repo\
```

Contains:
- ✅ **script.module.thecrew v2.2.0** (with all 5 alpha fixes)
- ✅ **plugin.video.thecrew v2.1.0**
- ✅ **script.thecrew.artwork v2.1.0**
- ✅ **repository.thecrew.alpha v1.0.0** (installer for Kodi)
- ✅ **addons.xml** and **addons.xml.md5** (repository catalog)

## 🚀 Quick Deploy (5 Minutes)

### Option 1: GitHub Releases (Easiest for testers)

1. **Tag and push your alpha branch:**
   ```powershell
   cd "C:\Users\fvanb\AppData\Roaming\Kodi\addons\script.module.thecrew"
   git tag -a v2.2.0-alpha -m "Alpha release 2.2.0"
   git push origin release/alpha-2.2.0
   git push origin v2.2.0-alpha
   ```

2. **Create GitHub Release:**
   - Go to: https://github.com/classymouse/script.module.thecrew/releases/new
   - Choose tag: `v2.2.0-alpha`
   - Title: `The Crew v2.2.0-alpha`
   - Description: Copy from `thecrew-alpha-repo\README.md`
   - Check "This is a pre-release"

3. **Upload repository files:**
   Drag and drop from `thecrew-alpha-repo/` to the release:
   ```
   addons.xml
   addons.xml.md5
   script.module.thecrew/script.module.thecrew-2.2.0.zip
   plugin.video.thecrew/plugin.video.thecrew-2.1.0.zip
   script.thecrew.artwork/script.thecrew.artwork-2.1.0.zip
   repository.thecrew.alpha/repository.thecrew.alpha-1.0.0.zip
   ```

4. **Publish release** ✅

5. **Share install link with testers:**
   ```
   https://github.com/classymouse/script.module.thecrew/releases/download/v2.2.0-alpha/repository.thecrew.alpha/repository.thecrew.alpha-1.0.0.zip
   ```

### Option 2: Separate Repository (Better long-term)

1. **Create new GitHub repository:**
   - Name: `thecrew-alpha-repo`
   - Public
   - No README/license (we'll add from local)

2. **Initialize and push:**
   ```powershell
   cd "..\thecrew-alpha-repo"
   git init
   git add .
   git commit -m "Initial alpha repository"
   git branch -M main
   git remote add origin https://github.com/classymouse/thecrew-alpha-repo.git
   git push -u origin main
   ```

3. **Enable GitHub Pages:**
   - Repo Settings > Pages
   - Source: `main` branch
   - Save

4. **Update repository addon URLs:**
   Edit `repository.thecrew.alpha/addon.xml`:
   ```xml
   <info compressed="false">https://raw.githubusercontent.com/classymouse/thecrew-alpha-repo/main/addons.xml</info>
   <checksum>https://raw.githubusercontent.com/classymouse/thecrew-alpha-repo/main/addons.xml.md5</checksum>
   <datadir zip="true">https://raw.githubusercontent.com/classymouse/thecrew-alpha-repo/main/</datadir>
   ```

5. **Rebuild and push:**
   ```powershell
   cd "..\script.module.thecrew"
   python tools\build_repo.py --output-dir ..\thecrew-alpha-repo --addons script.module.thecrew plugin.video.thecrew script.thecrew.artwork repository.thecrew.alpha
   cd "..\thecrew-alpha-repo"
   git add .
   git commit -m "Update repository.thecrew.alpha URLs"
   git push
   ```

6. **Share install link:**
   ```
   https://raw.githubusercontent.com/classymouse/thecrew-alpha-repo/main/repository.thecrew.alpha/repository.thecrew.alpha-1.0.0.zip
   ```

## 📥 Installation Instructions (Share with testers)

1. **Download repository installer:**
   - [Get repository.thecrew.alpha-1.0.0.zip](LINK_FROM_ABOVE)

2. **In Kodi:**
   - Settings → Add-ons → Install from zip file
   - Navigate to downloaded zip
   - Install
   - Wait for notification: "The Crew Alpha Repository Add-on installed"

3. **Install The Crew:**
   - Settings → Add-ons → Install from repository
   - Select "The Crew Alpha Repository"
   - Video add-ons → The Crew → Install
   - Dependencies will install automatically

4. **Verify version:**
   - Settings → Add-ons → My add-ons → Video add-ons → The Crew
   - Check version shows **2.2.0**

## ✅ Alpha Features to Test

### 1. Performance (Phase 1A)
- Open a TV show with 3+ seasons
- Browse through episodes
- **Expected:** Much faster loading, smoother navigation

### 2. Viperscrapers (Phase 1C)
- Search for a popular movie (e.g., "Deadpool")
- Check source list
- **Expected:** See [Viper] sources (13 new scrapers)

### 3. Scraping UX (Phase 1E)
- Start any search
- Watch progress dialog
- **Expected:** Smooth updates, shows "X/Y complete"

### 4. Library Auto-Update (Phase 1B)
- Add a continuing TV show to library
- Check back after 7 days OR clear last_season_check in database
- **Expected:** New seasons detected automatically

### 5. Metadata Rendering (Phase 1D)
- Browse TV shows
- Check watched counts
- **Expected:** No errors, accurate watch tracking

## 🐛 Collecting Feedback

Request testers provide:
- Kodi version + OS
- Issue description
- Steps to reproduce
- Kodi.log (with Debug logging enabled)

GitHub Issues: https://github.com/classymouse/script.module.thecrew/issues
(Tag with `alpha-2.2.0`)

## 📋 Alpha Commits

All fixes on `release/alpha-2.2.0` branch:
```
a6c3019 fix: improve list item rendering and metadata handling
2d00270 feat: add season tracking for library continuing shows
cb0c981 perf: optimize BGDialog progress updates during scraping
f35f555 feat: integrate viperscrapers external scraper pack
e558e1a perf(episodes): add show-level caching to eliminate repeated API calls
b78fe71 chore: remove backup files and broken scraper folders
```

## 🎯 Next Steps After Alpha

Once alpha testing confirms stability (1-2 weeks):

1. Merge to main:
   ```powershell
   git checkout main
   git merge release/alpha-2.2.0
   git push origin main
   ```

2. Create official release v2.2.0

3. Update main repository

4. Announce release

---

## 🔧 Troubleshooting

**Issue:** Can't install repository zip in Kodi
- **Fix:** Enable "Unknown sources" in Settings → System → Add-ons

**Issue:** Dependencies fail to install
- **Fix:** Install manually in order: script.module.thecrew → script.thecrew.artwork → plugin.video.thecrew

**Issue:** "Failed to install from repository"
- **Fix:** Check repository URLs are accessible (test in browser)
- Verify GitHub Pages is enabled (Option 2)
- Or verify release files are uploaded (Option 1)

**Issue:** Shows wrong version number
- **Fix:** Uninstall all The Crew addons, clear addon cache, reinstall

---

**Ready to deploy!** Choose Option 1 (GitHub Releases) for fastest deployment. 🚀
