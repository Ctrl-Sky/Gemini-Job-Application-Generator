all: get_company_name get_job_title generate_resume_and_cover_letter save_to_directory save_to_csv

get_company_name:
	export COMPANY_NAME=$(python3.12 utils/get_company_name.py)

get_job_title:
	export JOB_TITLE=$(python3.12 utils/get_job_title.py)

generate_resume_and_cover_letter:
	python3.12 src/main.py

save_to_directory:
	bash store_resume_and_cl.sh $COMPANY_NAME $JOB_TITLE

save_to_csv:
	python3.12 save_to_csv.py $COMPANY_NAME $JOB_TITLE

