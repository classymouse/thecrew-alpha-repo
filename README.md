# The Crew Alpha Repository

This is the alpha testing repository for The Crew Kodi addons.

## 📦 What's Included

- **script.module.thecrew v2.2.0-alpha** - Core module with alpha fixes
- **plugin.video.thecrew v2.1.0** - Main video addon
- **script.thecrew.artwork v2.1.0** - Artwork and UI module
- **repository.thecrew.alpha** - Repository installer

## 🔥 Alpha Features (v2.2.0)

### Performance Improvements
- **50-70% faster episode browsing** - Added show-level caching to eliminate ~69 redundant API calls per season
- **83% fewer progress dialog updates** - Batched scraping progress updates from every 0.5s to every 2.5s
- **Optimized list rendering** - Fixed metadata validation and property setting

### New Features
- **Viperscrapers integration** - 13 new torrent scrapers (aiostreams, comet, kickass2, mediafusion, nyaa, piratebay, rutor, torrentdownload, torrentgalaxy, torrentio, torrentsdb, torz, zilean)
- **Library auto-updates** - Detects new seasons for continuing shows every 7 days
- **Progress context** - Shows "X/Y scrapers complete" during searches

### Bug Fixes
- Fixed library not detecting new seasons for ongoing shows
- Fixed watched-count calculation errors
- Standardized metadata value handling (None vs '0' vs '')
- Improved artwork fallback chains
- Added validation before setting Kodi properties

## 🌐 Hosting on GitHub

### Option 1: GitHub Releases (Recommended)

1. **Create GitHub Release:**
   ```bash
   # Tag the release
   cd script.module.thecrew
   git checkout release/alpha-2.2.0
   git tag v2.2.0-alpha
   git push origin v2.2.0-alpha
   ```

2. **Upload repository files to release:**
   - Go to https://github.com/classymouse/script.module.thecrew/releases/new
   - Create release from tag `v2.2.0-alpha`
   - Upload all files from `thecrew-alpha-repo/` directory:
     - `addons.xml`
     - `addons.xml.md5`
     - `script.module.thecrew/script.module.thecrew-2.2.0.zip`
     - `plugin.video.thecrew/plugin.video.thecrew-2.1.0.zip`
     - `script.thecrew.artwork/script.thecrew.artwork-2.1.0.zip`
     - `repository.thecrew.alpha/repository.thecrew.alpha-1.0.0.zip`

3. **Repository URL will be:**
   ```
   https://github.com/classymouse/script.module.thecrew/releases/download/v2.2.0-alpha/
   ```

### Option 2: GitHub Pages

1. **Create gh-pages branch:**
   ```bash
   git checkout --orphan gh-pages
   git rm -rf .
   ```

2. **Copy repository files:**
   ```bash
   cp -r ../thecrew-alpha-repo/* .
   git add .
   git commit -m "Initial alpha repository"
   git push origin gh-pages
   ```

3. **Enable GitHub Pages:**
   - Go to repository Settings > Pages
   - Select `gh-pages` branch
   - Save

4. **Repository URL will be:**
   ```
   https://classymouse.github.io/script.module.thecrew/
   ```

## 📥 Installation Instructions for Users

### Method 1: Install from Repository URL

1. Download repository installer:
   - [repository.thecrew.alpha-1.0.0.zip](https://github.com/classymouse/script.module.thecrew/releases/download/v2.2.0-alpha/repository.thecrew.alpha/repository.thecrew.alpha-1.0.0.zip)

2. In Kodi:
   - Go to: `Settings > Add-ons > Install from zip file`
   - Navigate to downloaded file
   - Install `repository.thecrew.alpha-1.0.0.zip`

3. Wait for "The Crew Alpha Repository Add-on installed" notification

4. Go to: `Settings > Add-ons > Install from repository > The Crew Alpha Repository`

5. Install addons:
   - **Video add-ons > The Crew** (requires dependencies to install automatically)
   - Or manually install dependencies first:
     - **Program add-ons > The Crew Artwork**
     - **Program add-ons > The Crew Module**

### Method 2: Direct Install (Advanced)

1. Download all addon zips from release

2. Install in order:
   - `script.module.thecrew-2.2.0.zip` (dependencies first)
   - `script.thecrew.artwork-2.1.0.zip`
   - `plugin.video.thecrew-2.1.0.zip` (main addon)

3. Restart Kodi

## 🧪 Testing Checklist

Please test these specific improvements:

### Performance (Phase 1A)
- [ ] Browse TV show episodes - should load significantly faster
- [ ] Navigate through multiple seasons - check reduced API calls in log

### UI/UX (Phase 1E)
- [ ] Start a movie/episode search
- [ ] Check progress dialog updates smoothly (not spammy)
- [ ] Verify "X/Y complete" counter shows

### Viperscrapers (Phase 1C)
- [ ] Search for a popular movie
- [ ] Verify [Viper] sources appear
- [ ] Settings > Scrapers > check viperscrapers toggle works

### Library (Phase 1B)
- [ ] Add a continuing TV show to library
- [ ] Wait 7 days OR manually test by clearing last_season_check
- [ ] Verify new seasons are detected and added

### Metadata (Phase 1D)
- [ ] Check watched counts display correctly
- [ ] Verify no property setting errors in log
- [ ] Check artwork displays properly (fallbacks work)

## 📝 Reporting Issues

Report alpha issues to:
- GitHub: https://github.com/classymouse/script.module.thecrew/issues
- Tag with `alpha-2.2.0` label

Include:
- Kodi version
- Operating system
- Steps to reproduce
- Kodi.log excerpt (Debug logging enabled)

## 🔄 Version History

### v2.2.0-alpha (2026-02-09)
- Initial alpha release
- 6 major improvements across 5 phases
- See commit history on `release/alpha-2.2.0` branch

---

**Note:** This is alpha software. Backup your Kodi databases before testing.
