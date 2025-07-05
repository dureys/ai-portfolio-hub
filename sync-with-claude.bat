@echo off
echo ================================
echo   CLAUDE COLLABORATION SYNC
echo ================================
echo.
echo Syncing current state with GitHub...
git add .
set /p message=Enter commit message (or press Enter for auto): 
if "%message%"=="" set message=?? SYNC: Current development state for Claude review
git commit -m "%message%"
git push
echo.
echo ================================
echo Repository synced!
echo Share this with Claude:
echo.
echo Please read my repository to see current status:
echo https://github.com/dureys/ai-portfolio-hub
echo ================================
pause
