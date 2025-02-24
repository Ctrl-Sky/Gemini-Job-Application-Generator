import csv
import os
import argparse
from datetime import datetime

def save_to_csv(company_name, job_title, today, csv_path):
    csv_exist =  os.path.exists(csv_path)
    data = [company_name, "", job_title, "", "", today]

    with open(csv_path, "a", newline="") as file:
        writer = csv.writer(file)
        print("Writing to csv...")
        if not csv_exist:
            header = ["Company Name", " ", "Job Title", " ", " ", "Date Applied"]
            writer.writerow(header)

        writer.writerow(data)
    print("Successfully wrote to csv\n")

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("company_name")
    parser.add_argument("job_title")
    args = parser.parse_args()

    today = datetime.today()
    today = f"{today:%b-%d-%Y}"

    csv_path = "outputs/jobs_applied_to.csv"

    save_to_csv(args.company_name, args.job_title, today, csv_path)