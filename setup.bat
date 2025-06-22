@echo off
title Universal Decoder/Encoder Setup
color 0A

set "AUTOUPDATE_FILE=.autoupdate"

:menu
cls
echo.
echo ============================================
echo         Universal Decoder/Encoder Setup
echo ============================================
echo.
echo   1. Install Dependencies And Run Tool
echo   2. Install Dependencies
echo   3. Run The Tool
echo   4. Settings
echo   5. Exit

set /p choice=Choose an option [1-5]: 

if "%choice%"=="1" goto install_and_run
if "%choice%"=="2" goto install_only
if "%choice%"=="3" goto run_tool
if "%choice%"=="4" goto settings
if "%choice%"=="5" exit
if "%choice%"=="6" start https://www.youtube.com/watch?v=dQw4w9WgXcQ&autoplay=1&loop=1
goto menu

:install_and_run
cls
echo Installing dependencies and running tool...
echo.
pip install pyperclip pyfiglet >nul 2>&1
if errorlevel 1 (
    echo ❌ Oh No! Something Bad Happened: Failed to install required dependencies.
    pause
    goto menu
)
echo Built-in packages ready: zlib, base64, binascii, os, subprocess, codecs, html
echo ✅ Dependencies Successfully Installed!

REM Check for auto-update flag
if exist "%AUTOUPDATE_FILE%" (
    for /f %%a in (%AUTOUPDATE_FILE%) do (
        if /i "%%a"=="true" (
            echo 🔄 Auto-Update is enabled. Checking for updates...
            start /wait python update.py
        )
    )
)

echo Running The Tool...
timeout /t 2 >nul
start python main.py
exit

:install_only
cls
echo Installing dependencies...
echo.
pip install pyperclip pyfiglet >nul 2>&1
if errorlevel 1 (
    echo ❌ Oh No! Something Bad Happened: Failed to install required dependencies.
    pause
    goto menu
)
echo Built-in packages ready: zlib, base64, binascii, os, subprocess, codecs, html
echo ✅ Dependencies Successfully Installed!
echo.
echo What next?
echo 1. Return to Menu
echo 2. Exit
set /p next=Choose: 
if "%next%"=="1" goto menu
if "%next%"=="2" exit
goto menu

:run_tool
cls
echo Running The Tool...
timeout /t 1 >nul
start python main.py
exit

:settings
cls
echo ========== SETTINGS ==========
echo Type ON to enable Auto-Update
echo Type OFF to disable Auto-Update
echo Type MENU to return to Main Menu
echo ==============================
echo.

if exist "%AUTOUPDATE_FILE%" (
    set /p currentUpdate=<%AUTOUPDATE_FILE%
) else (
    set currentUpdate=OFF
)

echo Current Auto-Update setting: %currentUpdate%
echo.

set /p settingInput=Set Auto-Update: 

if /i "%settingInput%"=="ON" (
    echo true > %AUTOUPDATE_FILE%
    echo ✅ Auto-Update Enabled.
    timeout /t 2 >nul
    goto settings
)
if /i "%settingInput%"=="OFF" (
    echo false > %AUTOUPDATE_FILE%
    echo ❌ Auto-Update Disabled.
    timeout /t 2 >nul
    goto settings
)
if /i "%settingInput%"=="MENU" goto menu

echo Invalid input! Please type ON, OFF, or MENU.
timeout /t 2 >nul
goto settings

