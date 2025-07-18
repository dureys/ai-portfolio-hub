﻿Write-Host "$(Get-Date): Auto-saving AI portfolio progress..."
Set-Location "C:\Projects\ai-portfolio-hub"
git add .
$timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
git commit -m "Auto-save: $timestamp"
git push
Write-Host "$(Get-Date): Progress saved to GitHub"
