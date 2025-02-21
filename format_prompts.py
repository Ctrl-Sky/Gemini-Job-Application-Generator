from datetime import datetime
from textwrap import dedent

def get_cl_prompt(email, phone_num):
    today = datetime.today()
    cl_prompt = dedent(f"""\
        For the same job description, I want you to write a cover letter that is 225 words long using the resume you just helped me create.
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
    """)
    return cl_prompt

# def get_cl_prompt(phone_num, email, job_desc, resume):
#     today = datetime.today()
#     cl_prompt = dedent(f"""\
#         I want you to write a cover letter that is 225 words long using my resume and the job description.
#         When writing the cover letter follow this format:
#         {today:%B %d, %Y}
#         Sky Quan
#         Ajax, Ontario, Canada
#         {email}
#         {phone_num}

#         Dear Hiring Team,
#         [Opening Paragraph]
#         [Body Paragraph]
#         [Body Paragraph 2]
#         [Closing Paragraph]

#         Sincerely,
#         Sky Quan

#         Here are the constraints when writing this cover letter.
#         Do not include any information that you do not already have. For example, do not include a line like this: “I found this opening at [Platform where you saw the job posting].” 
#         When writing the cover letter, always ensure that it would be able to fit into a single A4 piece of paper. Have it only fill 3/4th of the page.
#         Only Include [Body Paragraph 2] as long as it isn't longer than 225 words
#         Finally, only output the cover letter. For example, do not output: “Ok here is the cover letter: [cover letter]”, only output “[cover letter]”
        
#         Here is my resume:
#         {resume}

#         Here is the job description:
#         {job_desc}\
#     """)
#     return cl_prompt

def get_resume_prompt():
    with open("inputs/job_description.txt") as desc:
        job_desc = desc.read()
    with open("inputs/skillset.txt") as skills:
        skillset = skills.read()
    with open("inputs/resume_template.txt") as resume:
        resume_format = resume.read()
    
    resume_prompt = dedent(f"""\
        I will provide you with a job description, my skillset, and a resume template. Your task is to to map key-value pairs in my skillset to the resume template to best fit the job description.
        
        Do these when filling in the template:
        Generate the unqiue highlight of qualifications based on what you included in the resume. Do not copy exactly what is on the resume, include unqiue highlights based off of the info. 
        There will sometimes be more than 3 points listed, take which points you think best fit the job description
        Do not shorten any of the points. Only include the full point and do not cut it off and summarise it. For example do not shorten:
        Developed an application integrating Google's Gemini 2.0 model with Python to optimize resumes based on job descriptions. The project then automatically generates a tailored cover letter based on the previous results, then stores the optimized resume and cover letter in a directory. All executed within a GitHub Actions workflow for scalability.
        to: Developed an application integrating Google's Gemini 2.0 model with Python to optimize resumes based on job descriptions.
        Follow the template exactly, do not add more points than needed. For example, the format list one course name and one course description. Only add one course from the skillset and not more.
        Finally, only output the resume. For example, do not output: “Ok here is the resume: [resume]”, only output “[resume]”
        
        Here is the job description:
        {job_desc}

        Here is my skillset:
        {skillset}

        Here is the resume template:
        {resume_format}\
    """)
    print(resume_prompt)
    return resume_prompt