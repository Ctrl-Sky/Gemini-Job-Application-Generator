from datetime import datetime
from textwrap import dedent

def get_cl_prompt(phone_num, email, job_desc, resume):
    today = datetime.today()
    cl_prompt = dedent(f"""\
        I want you to write a cover letter that is 225 words long using my resume and the job description.
        When writing the cover letter follow this format:
        {today:%B %d, %Y}
        Sky Quan
        Ajax, Ontario, Canada
        {email}
        {phone_num}

        Dear Hiring Team,
        [Opening Paragraph]
        [Body Paragraph]
        [Body Paragraph 2]
        [Closing Paragraph]

        Sincerely,
        Sky Quan

        Here are the constraints when writing this cover letter.
        Do not include any information that you do not already have. For example, do not include a line like this: “I found this opening at [Platform where you saw the job posting].” 
        When writing the cover letter, always ensure that it would be able to fit into a single A4 piece of paper. Have it only fill 3/4th of the page.
        Only Include [Body Paragraph 2] as long as it isn't longer than 225 words
        Finally, only output the cover letter. For example, do not output: “Ok here is the cover letter: [cover letter]”, only output “[cover letter]”
        
        Here is my resume:
        {resume}

        Here is the job description:
        {job_desc}\
    """)
    return cl_prompt

def get_resume_prompt():
    with open("inputs/job_description.txt") as desc:
        job_desc = desc.read()
    with open("inputs/skillset.txt") as skills:
        skillset = skills.read()
    with open("inputs/resume_template.txt") as resume:
        resume_format = resume.read()
    
    resume_prompt = dedent(f"""\
        I will provide you with a job description, my skillset, and a resume template. Your task is to to map key-value pairs in my skillset to the resume template to best fit the job description.

        Here is the job description:
        {job_desc}

        Here is my skillset:
        {skillset}

        Here is the resume template:
        {resume_format}

        Do these when filling in the template:
        Generate the highlight of qualifications based on what you included in the resume and what best fits the job description.
        Limit how much information you decide to include so that it can all fit into one A4 piece of paper.
        There will sometimes be more than 3 points listed, take which points you think best fit the job description
        Finally, only output the resume. For example, do not output: “Ok here is the resume: [resume]”, only output “[resume]”\
    """)
    print(resume_prompt)
    return resume_prompt