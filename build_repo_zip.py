#!/usr/bin/env python3
"""
Build repository.thecrew.alpha zip file with correct structure.

This script creates a properly formatted repository addon zip file where
all files are inside a repository.thecrew.alpha/ directory within the zip.

Usage:
    python build_repo_zip.py [--version VERSION]
"""

import argparse
import shutil
import sys
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path


def get_version_from_addon_xml(addon_xml_path):
    """Extract version from addon.xml file."""
    try:
        tree = ET.parse(addon_xml_path)
        root = tree.getroot()
        return root.get('version')
    except Exception as e:
        print(f"Error reading version from addon.xml: {e}")
        return None


def create_repository_zip(repo_dir, output_dir=None, version=None):
    """
    Create repository addon zip with correct structure.
    
    Args:
        repo_dir: Path to repository.thecrew.alpha source directory
        output_dir: Directory to save zip file (defaults to repo_dir)
        version: Version string (auto-detected from addon.xml if not provided)
    
    Returns:
        Path to created zip file or None if failed
    """
    repo_path = Path(repo_dir)
    addon_xml = repo_path / 'addon.xml'
    
    if not addon_xml.exists():
        print(f"Error: addon.xml not found in {repo_path}")
        return None
    
    # Get repository ID and version
    try:
        tree = ET.parse(addon_xml)
        root = tree.getroot()
        repo_id = root.get('id')
        detected_version = root.get('version')
        
        if not repo_id:
            print("Error: No id found in addon.xml")
            return None
        
        # Use provided version or detected version
        if version:
            final_version = version
        elif detected_version:
            final_version = detected_version
        else:
            print("Error: No version found")
            return None
            
    except Exception as e:
        print(f"Error parsing addon.xml: {e}")
        return None
    
    # Set output directory
    if output_dir:
        output_path = Path(output_dir)
    else:
        output_path = repo_path
    
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Create zip filename
    zip_filename = f"{repo_id}-{final_version}.zip"
    zip_path = output_path / zip_filename
    
    print("="*70)
    print("Repository Addon Zip Creator")
    print("="*70)
    print(f"Repository ID: {repo_id}")
    print(f"Version: {final_version}")
    print(f"Source: {repo_path}")
    print(f"Output: {zip_path}")
    print()
    
    # Create the zip file
    print("Creating zip file...")
    try:
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            # Get all files in repo directory
            for item in repo_path.rglob('*'):
                if item.is_file():
                    # Skip certain files
                    if item.name.endswith('.zip') or item.name.startswith('.'):
                        continue
                    
                    # Skip temp_repo_build directory
                    if 'temp_repo_build' in item.parts:
                        continue
                    
                    # Calculate relative path from repo_path
                    rel_path = item.relative_to(repo_path)
                    
                    # Create archive name with repo_id as base directory
                    arcname = Path(repo_id) / rel_path
                    
                    zipf.write(item, arcname)
                    print(f"  Added: {arcname}")
        
        # Get zip size
        zip_size_kb = zip_path.stat().st_size // 1024
        
        print()
        print("="*70)
        print(f"✓ Successfully created: {zip_filename}")
        print(f"  Size: {zip_size_kb} KB")
        print(f"  Path: {zip_path}")
        print("="*70)
        print()
        print("IMPORTANT: All files are correctly nested inside")
        print(f"           {repo_id}/ directory within the zip")
        print()
        
        return zip_path
        
    except Exception as e:
        print(f"Error creating zip file: {e}")
        import traceback
        traceback.print_exc()
        return None


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Build repository.thecrew.alpha zip file with correct structure'
    )
    parser.add_argument(
        '--repo-dir',
        default='repository.thecrew.alpha',
        help='Repository source directory (default: repository.thecrew.alpha)'
    )
    parser.add_argument(
        '--output-dir',
        help='Output directory for zip file (defaults to repo-dir)'
    )
    parser.add_argument(
        '--version',
        help='Version string (auto-detected from addon.xml if not provided)'
    )
    
    args = parser.parse_args()
    
    # Check if repo directory exists
    repo_path = Path(args.repo_dir)
    if not repo_path.exists():
        print(f"Error: Repository directory not found: {repo_path}")
        print()
        print("Make sure you're running this from the classymouse.github.io directory")
        return 1
    
    # Create the zip
    result = create_repository_zip(
        repo_dir=args.repo_dir,
        output_dir=args.output_dir,
        version=args.version
    )
    
    if result:
        print("✓ Zip file created successfully!")
        print()
        print("Next steps:")
        print("  1. Test the zip file by installing it in Kodi")
        print("  2. If it works, commit and push to GitHub:")
        print(f"     git add {result.name}")
        print(f'     git commit -m "Update repository zip to v{args.version or "X.X.X"}"')
        print("     git push")
        return 0
    else:
        print("✗ Failed to create zip file")
        return 1


if __name__ == '__main__':
    sys.exit(main())
