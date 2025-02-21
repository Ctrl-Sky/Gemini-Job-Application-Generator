from dotenv import load_dotenv
from google import genai
import format_prompts
import helpers
import os
import argparse

def generate_cover_letter(company_name, job_title, gemini_api_token):
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

def generate_resume():
    # Get prompts
    resume_prompt = format_prompts.get_resume_prompt()

    # Generate LLM response
    client = genai.Client(api_key=gemini_api_token)
    response = client.models.generate_content(
        model="gemini-2.0-flash", 
        contents=resume_prompt
    )
    print(response.text)

def generate_resume_and_cl(company_name, job_title):
    resume_prompt = format_prompts.get_resume_prompt()
    cl_prompt = format_prompts.get_cl_prompt(phone_number, email)

    client = genai.Client(api_key=gemini_api_token)
    chat = client.chats.create(model="gemini-2.0-flash")
    response = chat.send_message(resume_prompt)
    helpers.formatted_text_to_docx(response.text, "resume.docx")
    response = chat.send_message(cl_prompt)
    helpers.formatted_text_to_docx(response.text, "cover_letter.docx")


if __name__=="__main__":
    # Load and get environment variables from .env
    load_dotenv()
    gemini_api_token = os.getenv("GEMINI_API_TOKEN")
    phone_number = os.getenv("PHONE_NUMBER")
    email = os.getenv("EMAIL")
    # generate_cover_letter("hi", "hello", gemini_api_token)
    # generate_resume()
    generate_resume_and_cl("hi", "hello")

#     parser = argparse.ArgumentParser()
#     parser.add_argument("company-name")
#     parser.add_argument("job-title")
#     args = parser.parse_args()
#     generate_cover_letter(args.company_name, args.job_title)