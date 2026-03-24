import os
from google import genai
from dotenv import load_dotenv

def query_gemini(prompt):
    """Sends a prompt to Google Gemini and returns the response."""
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        return "Error: GOOGLE_API_KEY environment variable not set."
    
    try:
        # Use the modern google.genai SDK
        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=prompt
        )
        return response.text.strip()
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    user_prompt = input("Enter your prompt for Google Gemini: ")
    print("\nThinking...")
    result = query_gemini(user_prompt)
    print("\n--- Response ---")
    print(result)