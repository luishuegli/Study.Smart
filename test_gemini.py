from google import genai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("No API Key found!")
else:
    client = genai.Client(api_key=api_key)
    print("Testing gemini-2.0-flash...")
    try:
        response = client.models.generate_content(
            model='gemini-2.0-flash',
            contents='Hello, respond with "Migration Successful"'
        )
        print(f"Response: {response.text}")
    except Exception as e:
        print(f"Error: {e}")
