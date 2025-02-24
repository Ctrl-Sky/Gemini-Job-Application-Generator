COMPANY_NAME := $(shell python3.12 utils/get_company_name.py)
JOB_TITLE := $(shell python3.12 utils/get_job_title.py)

all: generate_resume_and_cover_letter save_to_directory save_to_csv

generate_resume_and_cover_letter:
	python3.12 src/main.py

save_to_directory:
	bash store_resume_and_cl.sh "$(COMPANY_NAME)" "$(JOB_TITLE)"

save_to_csv:
	python3.12 save_to_csv.py "$(COMPANY_NAME)" "$(JOB_TITLE)"

