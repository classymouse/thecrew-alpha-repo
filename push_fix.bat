@echo off
cd /d "D:\Development\github\classymouse.github.io"
git config core.editor "echo"
git fetch origin
git reset --hard origin/main
git add addons.xml addons.xml.md5
git commit -m "Fix version mismatch - update addons.xml to v1.0.6" || echo Already committed
git push
pause
