import os
from dotenv import load_dotenv
from google import genai

def get_company_name():
    with open("inputs/job_description.txt", encoding="utf-8") as desc:
        job_desc = desc.read()

    client = genai.Client(api_key=GEMINI_API_TOKEN)

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=f"{job_desc} What is the company name? Only output the company name. For example, if you think the company name is Amazon, only output Amazon",
    )
    print(response.text)

if __name__=="__main__":
    load_dotenv()
    GEMINI_API_TOKEN=os.getenv("GEMINI_API_TOKEN")
    get_company_name()