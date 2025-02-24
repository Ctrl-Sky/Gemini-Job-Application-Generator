import os
from dotenv import load_dotenv
from google import genai

def get_job_title():
    with open("inputs/job_description.txt", encoding="utf-8") as desc:
        job_desc = desc.read()

    client = genai.Client(api_key=GEMINI_API_KEY)

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=f"{job_desc} What is the job title? Only output the job title. For example, if you think the job title is Software Developer, only output Software Developer",
    )
    print(response.text)

if __name__=="__main__":
    load_dotenv()
    GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")
    get_job_title()