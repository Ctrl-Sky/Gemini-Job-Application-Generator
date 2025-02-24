COMPANY_NAME := $(shell python3.12 utils/get_company_name.py)
JOB_TITLE := $(shell python3.12 utils/get_job_title.py)

all: install_dependencies execute_application

install_dependencies:
	python3.12 -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt

execute_application:
	. .venv/bin/activate && python3.12 src/main.py && bash store_resume_and_cl.sh "$(COMPANY_NAME)" "$(JOB_TITLE)" && python3.12 save_to_csv.py "$(COMPANY_NAME)" "$(JOB_TITLE)"

