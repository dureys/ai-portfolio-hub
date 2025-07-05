@echo off
echo ================================
echo  AI DEVELOPMENT ENVIRONMENT
echo ================================
echo Starting Ollama service...
ollama serve
echo.
echo Environment ready!
echo - Session logging: ACTIVE
echo - Auto-save: Available (run auto_save.bat)
echo - GPU acceleration: ENABLED
echo - Repository: %cd%
echo.
echo Happy coding! ??
pause
