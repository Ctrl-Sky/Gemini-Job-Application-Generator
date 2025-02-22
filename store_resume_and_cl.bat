@echo off

set COMPANY_NAME=%1
set JOB_TITLE=%2

:: DO ALL THIS TO GET MONTH-DATE IN THIS FORMAT %b-%Y
for /f "tokens=2 delims=/- " %%a in ('date /t') do set MONTH=%%a
for /f "tokens=1 delims=/- " %%b in ('date /t') do set YEAR=%%b

:: Map the month number to the full month name
if "%MONTH%"=="01" set MONTH_NAME=Jan
if "%MONTH%"=="02" set MONTH_NAME=Feb
if "%MONTH%"=="03" set MONTH_NAME=Mar
if "%MONTH%"=="04" set MONTH_NAME=Apr
if "%MONTH%"=="05" set MONTH_NAME=May
if "%MONTH%"=="06" set MONTH_NAME=Jun
if "%MONTH%"=="07" set MONTH_NAME=Jul
if "%MONTH%"=="08" set MONTH_NAME=Aug
if "%MONTH%"=="09" set MONTH_NAME=Sep
if "%MONTH%"=="10" set MONTH_NAME=Oct
if "%MONTH%"=="11" set MONTH_NAME=Nov
if "%MONTH%"=="12" set MONTH_NAME=Dec

:: Format the date as Month-YYYY
set MONTH_DATE=%MONTH_NAME%-%YEAR%

set DIR_PATH=outputs\%MONTH_DATE%\%COMPANY_NAME%-%JOB_TITLE%
set INITIALS=%COMPANY_NAME:~0,1%%JOB_TITLE:~0,1%

:: If dir does not exist, create it
if not exist "%DIR_PATH%" (
    echo Creating Directory
    mkdir "%DIR_PATH%"
)

:: Copy Job Description to path
echo Moving job description
copy inputs\job_description.txt "%DIR_PATH%"

:: Rename and move cover letter
echo Moving resume
ren cover_letter.docx "Sky_Quan_Cover_Letter_%INITIALS%.docx"
move "Sky_Quan_Cover_Letter_%INITIALS%.docx" "%DIR_PATH%"

:: Rename and move resume
echo Moving cover letter
ren resume.docx "Sky_Quan_Resume_%INITIALS%.docx"
move "Sky_Quan_Resume_%INITIALS%.docx" "%DIR_PATH%"

echo Script completed Successfully