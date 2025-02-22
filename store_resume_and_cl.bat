@echo off

set COMPANY_NAME=%1
set JOB_TITLE=%2

rem Get the current month and year
for /f "tokens=2 delims==" %%I in ('"wmic path win32_localtime get month^,year /value"') do set currentDate=%%I

rem Format the month and year
set MONTH_DATE=%currentDate:~4,2%-%currentDate:~0,4%

rem Define the directory path
set DIR_PATH=outputs\%MONTH_DATE%\%COMPANY_NAME%-%JOB_TITLE%

rem Get initials from company and job title
set INITIALS=%COMPANY_NAME:~0,1%%JOB_TITLE:~0,1%

rem If the directory does not exist, create it
if not exist "%DIR_PATH%" (
    mkdir "%DIR_PATH%"
)

rem Copy Job Description to path
copy inputs\job_description.txt "%DIR_PATH%"

rem Rename and move cover letter
rename cover_letter.docx Sky_Quan_Cover_Letter_%INITIALS%.docx
move Sky_Quan_Cover_Letter_%INITIALS%.docx "%DIR_PATH%"

rem Rename and move resume
rename resume.docx Sky_Quan_Resume_%INITIALS%.docx
move Sky_Quan_Resume_%INITIALS%.docx "%DIR_PATH%"

echo Script completed successfully!
