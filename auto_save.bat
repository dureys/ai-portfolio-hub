@echo off
echo [%date% %time%] Auto-saving AI portfolio progress...
cd /d "C:\Projects\ai-portfolio-hub"
git add .
git commit -m "Auto-save: %date% %time%"
git push
echo [%date% %time%] Progress saved to GitHub
echo.
echo Press any key to continue...
pause >nul
