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