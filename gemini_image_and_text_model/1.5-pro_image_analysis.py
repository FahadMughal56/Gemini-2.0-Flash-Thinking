import os
from dotenv import load_dotenv  # Import the dotenv module
import PIL.Image
import google.generativeai as genai

# Load the .env file
load_dotenv()

# Retrieve the API key from the environment variable
api_key = os.getenv("API_KEY_1.5-pro")

if not api_key:
    raise ValueError("API key not found in .env file")

# Configure the generative AI API with the loaded API key
genai.configure(api_key=api_key)

# Image path
image_path_1 = r"PATH_TO_IMAGE"  # Replace with the actual path to your first image
sample_file_1 = PIL.Image.open(image_path_1)

# Choose a Gemini model
model = genai.GenerativeModel(model_name="gemini-1.5-pro")

prompt = "Please extract relevant skills from this Resume and return as a valid JSON containing a list of skills"

# Generate content
response = model.generate_content([prompt, sample_file_1])

# Print the response
print(response.text)
