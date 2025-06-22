@echo off
title Universal Decoder/Encoder Setup
color 0A

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
echo   4. Exit
echo.

set /p choice=Choose an option [1-4]: 

if "%choice%"=="1" goto install_and_run
if "%choice%"=="2" goto install_only
if "%choice%"=="3" goto run_tool
if "%choice%"=="4" exit
if "%choice%"=="5" start https://www.youtube.com/watch?v=dQw4w9WgXcQ&autoplay=1&loop=1
goto menu

:install_and_run
cls
echo Installing dependencies and running tool...
echo.
pip install pyperclip >nul 2>&1
if errorlevel 1 (
    echo ❌ Oh No! Something Bad Happened: Failed to install pyperclip
    pause
    goto menu
)
REM zlib, base64, and binascii are built-in, skip install but "simulate"
echo Built-in packages ready: zlib, base64, binascii
echo ✅ Dependencies Successfully Installed! Running The Tool....
echo.
timeout /t 2 >nul
start python main.py
exit

:install_only
cls
echo Installing dependencies...
echo.
pip install pyperclip >nul 2>&1
if errorlevel 1 (
    echo ❌ Oh No! Something Bad Happened: Failed to install pyperclip
    pause
    goto menu
)
echo Built-in packages ready: zlib, base64, binascii
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
