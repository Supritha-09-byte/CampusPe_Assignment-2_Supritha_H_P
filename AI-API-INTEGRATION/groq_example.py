import os
from groq import Groq
from dotenv import load_dotenv

def query_groq(prompt):
    """Sends a prompt to Groq and returns the generated response."""
    load_dotenv()
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        return "Error: GROQ_API_KEY environment variable not set."
    
    try:
        client = Groq(api_key=api_key)
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "user", "content": prompt}
            ],
            model="llama-3.1-8b-instant",
        )
        return chat_completion.choices[0].message.content.strip()
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    user_prompt = input("Enter your prompt for Groq: ")
    print("\nThinking...")
    result = query_groq(user_prompt)
    print("\n--- Response ---")
    print(result)