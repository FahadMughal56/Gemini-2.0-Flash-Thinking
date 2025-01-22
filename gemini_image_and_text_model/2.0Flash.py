import os
from dotenv import load_dotenv  # Ensure environment variables are loaded
import google.generativeai as genai
from google.generativeai.types import GenerationConfig  # Import the correct type

# Load environment variables from .env file
load_dotenv()

# Configure the API key
api_key = os.getenv("GEMINI_API_KEY_2.0")
if not api_key:
    raise ValueError("GEMINI_API_KEY is not set in the environment variables.")

genai.configure(api_key=api_key)

# Define the model configuration using the correct type
generation_config = GenerationConfig(
    temperature=0.7,
    top_p=0.95,
    top_k=64,
    max_output_tokens=65536,
    response_mime_type="text/plain",
)

# Initialize the model
model = genai.GenerativeModel(
    model_name="gemini-2.0-flash-thinking-exp-01-21",
    generation_config=generation_config,
)

# Start a chat session with an empty history
chat_session = model.start_chat(history=[])

# Continuous conversation loop
print("Chatbot is ready! Type 'exit' to end the conversation.")
while True:
    # Get user input
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    # Send user input to the chat model
    response = chat_session.send_message(user_input)

    # Print the AI's response
    print(f"AI: {response.text}")

    # The history is automatically updated within the `chat_session`.
