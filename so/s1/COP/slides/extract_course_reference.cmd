@echo off
setlocal EnableDelayedExpansion

title COP 3330 OOP Master Course Reference Extractor

echo ===============================================================================
echo   COP 3330: Object-Oriented Programming - Course Reference Extractor
echo ===============================================================================
echo.

cd /d "%~dp0"

set "TARGET_PDF=COP3330_OOP_Complete_Course_Reference.pdf"
set "PART1=COP3330_OOP_Course_Reference.7z.001"
set "COMBINED_TEMP=_temp_combined_archive.7z"

if not exist "%PART1%" (
    echo [ERROR] Archive volume 1 missing: %PART1%
    echo Please make sure all archive parts (.7z.001 through .7z.005) are in this folder.
    goto :FAIL
)

if exist "%TARGET_PDF%" (
    echo [INFO] Target deliverable already exists:
    echo        %TARGET_PDF%
    echo.
    set /p "OVERWRITE=Do you want to re-extract and overwrite it? (y/N): "
    if /i not "!OVERWRITE!"=="y" (
        echo [INFO] Extraction cancelled by user.
        goto :END
    )
    echo.
)

:: Step 1: Check for 7-Zip installation
set "SEVENZIP_CMD="

where 7z.exe >nul 2>&1
if !errorlevel! equ 0 set "SEVENZIP_CMD=7z.exe"

if not defined SEVENZIP_CMD (
    where 7za.exe >nul 2>&1
    if !errorlevel! equ 0 set "SEVENZIP_CMD=7za.exe"
)

if not defined SEVENZIP_CMD (
    if exist "%ProgramFiles%\7-Zip\7z.exe" (
        set "SEVENZIP_CMD=%ProgramFiles%\7-Zip\7z.exe"
    ) else if exist "%ProgramFiles(x86)%\7-Zip\7z.exe" (
        set "SEVENZIP_CMD=%ProgramFiles(x86)%\7-Zip\7z.exe"
    ) else if exist "%LocalAppData%\Programs\7-Zip\7z.exe" (
        set "SEVENZIP_CMD=%LocalAppData%\Programs\7-Zip\7z.exe"
    ) else if exist "%ProgramData%\chocolatey\bin\7z.exe" (
        set "SEVENZIP_CMD=%ProgramData%\chocolatey\bin\7z.exe"
    )
)

if defined SEVENZIP_CMD (
    echo [INFO] Detected 7-Zip engine: "!SEVENZIP_CMD!"
    echo [INFO] Extracting master PDF compendium...
    "!SEVENZIP_CMD!" x -y "%PART1%"
    if !errorlevel! equ 0 (
        goto :SUCCESS
    ) else (
        echo [WARN] 7-Zip extraction encountered an issue. Falling back to native tools...
    )
)

:: Step 2: Native Windows fallback (built-in copy /b + Windows tar.exe)
echo [INFO] 7-Zip not found in standard paths. Attempting native Windows tools...

where tar.exe >nul 2>&1
if !errorlevel! equ 0 (
    echo [INFO] Detected Windows built-in tar utility (libarchive).
    echo [INFO] Step 1 of 2: Recombining multi-part volumes...
    copy /b COP3330_OOP_Course_Reference.7z.* "%COMBINED_TEMP%" >nul
    if !errorlevel! neq 0 (
        echo [ERROR] Failed to concatenate archive parts.
        if exist "%COMBINED_TEMP%" del /f /q "%COMBINED_TEMP%"
        goto :FAIL
    )

    echo [INFO] Step 2 of 2: Extracting PDF deliverable...
    tar.exe -xf "%COMBINED_TEMP%"
    set "TAR_EXIT=!errorlevel!"
    if exist "%COMBINED_TEMP%" del /f /q "%COMBINED_TEMP%"

    if !TAR_EXIT! equ 0 (
        goto :SUCCESS
    ) else (
        echo [WARN] tar extraction failed. Trying Python fallback...
    )
)

:: Step 3: Python fallback if available
where python.exe >nul 2>&1
if !errorlevel! equ 0 (
    echo [INFO] Detected Python interpreter. Running extraction script...
    python.exe extract_course_reference.py
    if !errorlevel! equ 0 goto :SUCCESS
)

echo.
echo [ERROR] No suitable extraction utility found!
echo To extract this archive on Windows, please install 7-Zip:
echo     1. Download from: https://www.7-zip.org/
echo     2. Or run: winget install 7zip.7zip
goto :FAIL

:SUCCESS
echo.
echo ===============================================================================
echo [PASS] Extraction complete!
echo Master Deliverable: %TARGET_PDF% (776 pages, ~395 MB)
echo ===============================================================================
goto :END

:FAIL
echo.
echo ===============================================================================
echo [FAIL] Extraction could not be completed.
echo ===============================================================================

:END
echo.
echo Press any key to exit...
pause >nul
