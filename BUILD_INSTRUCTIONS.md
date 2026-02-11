# Repository Build Instructions

## Creating the Repository Addon Zip

The `build_repo_zip.py` script automates creating the repository addon zip file with the correct structure.

### Why This Script?

Kodi requires repository addon zip files to have all files nested inside a directory matching the addon ID. For example:

```
repository.thecrew.alpha-1.0.5.zip
└── repository.thecrew.alpha/
    ├── addon.xml
    ├── fanart.jpg
    └── icon.png
```

**NOT** like this (incorrect):
```
repository.thecrew.alpha-1.0.5.zip
├── addon.xml
├── fanart.jpg
└── icon.png
```

### Usage

1. Make sure you're in the `classymouse.github.io` directory
2. Update the version in `repository.thecrew.alpha/addon.xml`
3. Run the script:

```bash
python build_repo_zip.py
```

This will:
- Auto-detect the version from `addon.xml`
- Create a properly structured zip file
- Place it in the `repository.thecrew.alpha/` directory

### Options

```bash
# Specify a different version
python build_repo_zip.py --version 1.0.6

# Specify output directory
python build_repo_zip.py --output-dir ./output

# Specify repo directory (if not in default location)
python build_repo_zip.py --repo-dir path/to/repository.thecrew.alpha
```

### After Creating the Zip

1. **Test it first!** Install the zip in Kodi to make sure it works
2. If successful, commit and push:
   ```bash
   git add repository.thecrew.alpha/repository.thecrew.alpha-X.X.X.zip
   git commit -m "Update repository to vX.X.X"
   git push
   ```

## Common Issues

### Zip files at root level
If you manually create a zip and files are at the root (not in a subdirectory), Kodi won't be able to install it. Always use this script or ensure files are nested correctly.

### Old zip files
You can safely delete old version zip files after testing the new one.

### Verifying Zip Structure

To check if a zip has the correct structure:

**Windows PowerShell:**
```powershell
Add-Type -AssemblyName System.IO.Compression.FileSystem
$zip = [System.IO.Compression.ZipFile]::OpenRead("repository.thecrew.alpha/repository.thecrew.alpha-1.0.5.zip")
$zip.Entries | Select-Object FullName
$zip.Dispose()
```

**Linux/Mac:**
```bash
unzip -l repository.thecrew.alpha/repository.thecrew.alpha-1.0.5.zip
```

The first entry should be a directory like `repository.thecrew.alpha/`.
