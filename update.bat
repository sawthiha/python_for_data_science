@echo off
echo Pulling latest changes from the repository...
git pull

REM Check if the git pull command succeeded
if %errorlevel% neq 0 (
    echo Error: Failed to pull the latest changes.
    pause
    exit /b %errorlevel%
) else (
    echo Successfully pulled the latest changes.
)
pause
