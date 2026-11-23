@echo off
title MedBank Studio - Direct Instagram Reel Server
cd /d "%~dp0"
echo Starting MedBank Studio Server on http://127.0.0.1:8080 ...
start "" "http://127.0.0.1:8080"
python server.py --port 8080
pause
