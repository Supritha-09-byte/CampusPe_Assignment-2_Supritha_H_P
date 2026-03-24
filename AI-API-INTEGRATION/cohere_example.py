import os
import cohere
from dotenv import load_dotenv

def query_cohere(prompt):
    """Sends a prompt to Cohere and returns the response."""
    load_dotenv()
    api_key = os.getenv("COHERE_API_KEY")
    if not api_key:
        return "Error: COHERE_API_KEY environment variable not set."
    
    try:
        co = cohere.Client(api_key, timeout=120)
        response = co.chat(
            model="command-r-08-2024",
            message=prompt
        )
        return response.text.strip()
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    user_prompt = input("Enter your prompt for Cohere: ")
    print("\nThinking...")
    result = query_cohere(user_prompt)
    print("\n--- Response ---")
    print(result)