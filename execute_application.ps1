# Powershell equivalent of execute_application.sh

# Install Dependencies
python3.12 -m venv .venv
.venv\Scripts\Activate

# Install required packages
pip install -r requirements.txt

# Get variables from job_description.txt
$COMPANY_NAME = python3.12 utils/get_company_name.py
$JOB_TITLE = python3.12 utils/get_job_title.py

# Generate Resume and Cover Letter
python3.12 src/main.py

# Store and save resume and cover letter
.\cleanup_scipts\store_resume_and_cl.ps1 $COMPANY_NAME $JOB_TITLE
python3.12 cleanup_scipts\save_to_csv.py $COMPANY_NAME $JOB_TITLE

Write-Host "Application successfully executed"