#!/bin/bash

python3.12 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt

export COMPANY_NAME=$(python3.12 utils/get_company_name.py)
export JOB_TITLE=$(python3.12 utils/get_job_title.py)

python3.12 src/main.py
bash store_resume_and_cl.sh "${COMPANY_NAME}" "${JOB_TITLE}"
python3.12 save_to_csv.py "${COMPANY_NAME}" "${JOB_TITLE}"