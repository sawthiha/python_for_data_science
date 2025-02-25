@echo off
REM Check if Python is installed
python --version >nul 2>&1
if %ERRORLEVEL% neq 0 (
    echo Python is not installed or not added to PATH.
    pause
    exit /b 1
)

REM Check if virtual environment "python-course" exists
if not exist "python-course-env\Scripts\activate.bat" (
    echo Creating virtual environment "python-course-env"...
    python -m venv python-course-env
    if %ERRORLEVEL% neq 0 (
        echo Failed to create the virtual environment.
        pause
        exit /b %ERRORLEVEL%
    )
) else (
    echo Virtual environment "python-course-env" already exists.
)

REM Activate the virtual environment
call python-course-env\Scripts\activate.bat

REM Install packages from requirements.txt if it exists
if exist requirements.txt (
    echo Installing required packages...
    pip install -r requirements.txt
) else (
    echo requirements.txt not found, skipping installation.
)

REM Start the Jupyter Notebook server
echo Starting Jupyter Notebook...
jupyter lab

REM Optionally, pause the script if you want to keep the window open after the command
pause
