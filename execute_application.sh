#!/bin/bash

# Install Dependencies
python3.12 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt

# Get variables from job_description.txt
export COMPANY_NAME=$(python3.12 utils/get_company_name.py)
export JOB_TITLE=$(python3.12 utils/get_job_title.py)

# Generate Resume and Cover Letter
python3.12 src/main.py

# Store and save resume and cover letter
bash cleanup_scipts/store_resume_and_cl.sh "${COMPANY_NAME}" "${JOB_TITLE}"
python3.12 cleanup_scipts/save_to_csv.py "${COMPANY_NAME}" "${JOB_TITLE}"

echo "Application successfully executed"