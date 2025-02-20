from dotenv import load_dotenv
from google import genai
import format_prompts
import helpers
import os
import argparse

def generate_cover_letter(company_name, job_title):
    # Load and get environment variables from .env
    load_dotenv()
    gemini_api_token = os.getenv("GEMINI_API_TOKEN")
    phone_number = os.getenv("PHONE_NUMBER")
    email = os.getenv("EMAIL")

    # Get resume and job description input
    with open("inputs/job_description.txt", "r", encoding="utf-8") as job:
        job_desciption = job.read()

    with open("inputs/skillset.txt", "r", encoding="utf-8") as skill:
        skillset = skill.read()

    # Get prompts
    cl_prompt = format_prompts.get_cl_prompt(phone_number, email, job_desciption, skillset)

    # Generate LLM response
    client = genai.Client(api_key=gemini_api_token)
    response = client.models.generate_content(
        model="gemini-2.0-flash", 
        contents=cl_prompt
    )
    print(response.text)
    helpers.formatted_text_to_docx(response.text, company_name, job_title)

generate_cover_letter("hello", "hi")

# if __name__=="__main__":
#     parser = argparse.ArgumentParser()
#     parser.add_argument("company-name")
#     parser.add_argument("job-title")
#     args = parser.parse_args()
#     generate_cover_letter(args.company_name, args.job_title)