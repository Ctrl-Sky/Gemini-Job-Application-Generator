from dotenv import load_dotenv
from google import genai
import os

# Load environment variables from .env
load_dotenv()
gemini_api_token = os.getenv("GEMINI_API_TOKEN")

client = genai.Client(api_key=gemini_api_token)
response = client.models.generate_content(
    model="gemini-2.0-flash-exp", contents="Explain how AI works"
)
print(response.text)