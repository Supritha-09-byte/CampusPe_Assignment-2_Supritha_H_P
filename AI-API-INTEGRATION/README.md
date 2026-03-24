AI API Integration Assignment

Hello! 
I am Supritha H P, and this is my submission for the AI API Integration assignment.

In this project, I explored how to integrate multiple AI models using Python. Instead of working with a single provider, I implemented integrations with five different AI platforms, including both cloud-based APIs and locally hosted models. This helped me understand the differences in API structures, performance, and usage across platforms.

Project Overview

I developed individual Python scripts for the following AI providers:

Groq – using LLaMA 3 (8B) for high-speed responses
Ollama – running LLaMA 3 locally on my system
Hugging Face – experimenting with models like DialoGPT / Qwen
Google Gemini – using Gemini 2.0 Flash
Cohere – using Command R+

Additionally, I created a unified interface called multi_api_query.py, which allows users to:

Select any AI provider
Enter prompts dynamically
Interact with multiple models from a single script
Project Structure
ai-api-integration/
├── .env                  
├── .gitignore            
├── cohere_example.py     
├── gemini_example.py     
├── groq_example.py       
├── huggingface_example.py
├── multi_api_query.py    
├── ollama_example.py     
├── README.md             
├── requirements.txt      
└── screenshots/          
Setup Instructions
1. Prerequisites
Python 3.8 or higher
API keys for:
Groq
Hugging Face
Google Gemini
Cohere
(Optional) Ollama installed for local model execution
2. Installation

Create a virtual environment:

python -m venv venv

Activate it:

Windows:

venv\Scripts\activate

Mac/Linux:

source venv/bin/activate

Install dependencies:

pip install -r requirements.txt
3. Environment Variables

Create a .env file and add your API keys:

GROQ_API_KEY=your_groq_api_key
HUGGINGFACE_API_KEY=your_huggingface_api_key
GOOGLE_API_KEY=your_google_api_key
COHERE_API_KEY=your_cohere_api_key
Running the Project

You can run individual scripts:

python groq_example.py

Or use the unified interface:

python multi_api_query.py

This will display a menu to choose the AI provider and interact with it directly.

Key Learnings & Challenges
Gained hands-on experience with multiple AI APIs and SDKs
Understood differences in API design, request/response handling, and performance
Learned to securely manage API keys using environment variables (.env)
Built a modular and scalable architecture to support multiple providers
Faced challenges in adapting to different SDK formats and resolved them through documentation and experimentation
Screenshots

Screenshots of successful execution and outputs are included in the screenshots/ folder as proof of implementation.