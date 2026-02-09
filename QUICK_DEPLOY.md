# Quick Deploy Guide for Alpha Repository

## Current Situation
- ✅ All repository files exist locally
- ❌ Not yet published to GitHub
- ❌ Repository addon configured for separate repo that doesn't exist

## Option A: Separate Repository (RECOMMENDED - EASIEST)

### 1. Create New GitHub Repository
```
Go to: https://github.com/new
Repository name: thecrew-alpha-repo
Description: The Crew Alpha Testing Repository
Public: ✓ (must be public for Kodi to access)
Initialize: NO (we have files already)
```

### 2. Push Repository Files
```powershell
cd C:\Users\fvanb\AppData\Roaming\Kodi\addons\thecrew-alpha-repo

# Initialize git
git init
git add .
git commit -m "Initial alpha repository setup"

# Add remote and push
git remote add origin https://github.com/classymouse/thecrew-alpha-repo.git
git branch -M main
git push -u origin main
```

### 3. Share with Testers
**Installation URL:**
```
https://github.com/classymouse/thecrew-alpha-repo/raw/main/repository.thecrew.alpha/repository.thecrew.alpha-1.0.0.zip
```

**Installation Steps:**
1. Download repository.thecrew.alpha-1.0.0.zip
2. In Kodi: Settings → Add-ons → Install from zip file
3. Select the downloaded zip
4. Wait for "The Crew Alpha Repository enabled" notification
5. All alpha addons now available in Kodi!

---

## Option B: GitHub Releases (Alternative)

If you want to use the script.module.thecrew repository instead:

### 1. Update repository addon URLs

Edit `repository.thecrew.alpha\addon.xml` to use GitHub Releases:
```xml
<info compressed="false">https://raw.githubusercontent.com/classymouse/script.module.thecrew/alpha-release/addons.xml</info>
<checksum>https://raw.githubusercontent.com/classymouse/script.module.thecrew/alpha-release/addons.xml.md5</checksum>
<datadir zip="true">https://raw.githubusercontent.com/classymouse/script.module.thecrew/alpha-release/</datadir>
```

### 2. Create alpha-release branch
```powershell
cd C:\Users\fvanb\AppData\Roaming\Kodi\addons\script.module.thecrew

# Create new orphan branch for repository files only
git checkout --orphan alpha-release
git rm -rf .
git clean -fdx

# Copy repository files
Copy-Item -Path ..\thecrew-alpha-repo\* -Destination . -Recurse -Force

# Commit and push
git add .
git commit -m "Alpha repository files"
git push -u origin alpha-release
```

---

## Testing the Repository

After deployment, test by:
1. Download: `repository.thecrew.alpha-1.0.0.zip`
2. Install in Kodi as zip
3. Check Kodi log for connection errors
4. Install script.module.thecrew v2.2.0 from repository
5. Verify no IndentationError!

---

## Current Alpha Features
- ✅ 50-70% faster episode browsing (show-level caching)
- ✅ 13 Viperscrapers torrent sources
- ✅ Library auto-updates for new seasons
- ✅ Optimized scraping UI (83% fewer updates)
- ✅ Metadata rendering fixes
- ✅ IndentationError fixed

---

## Need Help?
- Check kodi.log for error messages
- Verify GitHub URLs are accessible in browser
- Ensure repository is PUBLIC on GitHub
