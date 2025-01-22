# Gemini AI Image and Chatbot Integration

This project integrates two Gemini models for generating AI-based responses and processing image data. It consists of two Python scripts:

1. **2.0Flash.py**: A chatbot that communicates with the user and provides intelligent responses, powered by the Gemini 2.0 model.
2. **1.5-pro_image_analysis.py**: An image analysis tool that extracts relevant skills from a resume image using the Gemini 1.5 Pro model.

## Prerequisites

Before running the scripts, ensure the following requirements are met:

- Python 3.x installed.
- Install dependencies using the following command:

```bash
pip install -r requirements.txt
```

You can create the `requirements.txt` file by running the following:

```plaintext
Pillow
python-dotenv
google-generativeai
```

- Create a `.env` file in the root directory to store your API keys.

Example of `.env` file:

```plaintext
GEMINI_API_KEY_2.0=your-gemini-2.0-api-key
API_KEY_1.5-pro=your-gemini-1.5-pro-api-key
```

## File Descriptions

### 1. **2.0Flash.py**

This script enables a chatbot to interact with the user in a loop using the **Gemini 2.0** model.

#### Key Features:
- Uses the **Gemini 2.0 Flash** model for conversation.
- Configurable with **temperature**, **top_p**, and other settings for response tuning.
- Loads the API key from the `.env` file and initializes the chat session.
- Interactive loop where the user can send messages and receive responses from the AI.

#### How to Run:
1. Ensure your `.env` file has the correct API key for Gemini 2.0.
2. Run the script in the terminal:

```bash
python 2.0Flash.py
```

3. Start typing messages. Type `exit` to end the conversation.

### 2. **1.5-pro_image_analysis.py**

This script processes an image (such as a resume) and extracts relevant skills using the **Gemini 1.5 Pro** model.

#### Key Features:
- Loads an image (e.g., resume) and analyzes it with the **Gemini 1.5 Pro** model.
- Extracts relevant skills from the image content and returns the result as a JSON.
- Configurable with the API key loaded from the `.env` file.

#### How to Run:
1. Update the image path in the script to point to your desired image (e.g., `resume.jpg`).
2. Ensure your `.env` file has the correct API key for Gemini 1.5 Pro.
3. Run the script in the terminal:

```bash
python 1.5-pro_image_analysis.py
```

4. The extracted skills will be printed in the terminal.

## Contributing

If you'd like to contribute to this project, feel free to submit issues or pull requests. Please make sure to test your changes thoroughly before submitting.

## License

This project is open-source and available under the MIT License.

---

This README should help explain how the scripts work, how to set up the environment, and how to run the Python files for both chatbot interaction and image analysis.
