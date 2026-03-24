import os
from huggingface_hub import InferenceClient
from dotenv import load_dotenv

def query_huggingface(prompt):
    """Sends a prompt to Hugging Face Inference API and returns the response."""
    load_dotenv()
    api_key = os.getenv("HUGGINGFACE_API_KEY")
    if not api_key:
        return "Error: HUGGINGFACE_API_KEY environment variable not set."
    
    # Using the official Hugging Face Python SDK.
    # This automatically guarantees the correct routing URL, avoiding 404/410 errors completely.
    try:
        client = InferenceClient(api_key=api_key)
        
        messages = [{"role": "user", "content": prompt}]
        # Qwen2.5-7B-Instruct is an excellent, freely-available conversational model
        response = client.chat_completion(
            model="Qwen/Qwen2.5-7B-Instruct",
            messages=messages,
            max_tokens=250
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    user_prompt = input("Enter your prompt for Hugging Face: ")
    print("\nThinking...")
    result = query_huggingface(user_prompt)
    print("\n--- Response ---")
    print(result)