@echo off
echo ================================
echo    ?? GIT SUMMARY AGENT
echo ================================
echo.
echo Analyzing recent commits...
python ai-assistants\git-summary-agent\git_summary_agent.py
echo.
echo ================================
echo Review the changes above.
echo.
echo To APPROVE: git commit -m "Ready"
echo To CANCEL:  git reset
echo ================================
pause
