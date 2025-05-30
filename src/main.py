import google.generativeai as genai
import os

# Set your Google API key here
# You can get one from https://makersuite.google.com/app/apikey
# It's recommended to set this as an environment variable
# genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))

# Replace with your actual API key or uncomment the line above and set the environment variable
# Make sure to keep your API key secure and do not commit it directly to version control.
API_KEY = "AIzaSyCbPw-Rw2hx1SHLsIsdRedl0YBQvufc5ds"

genai.configure(api_key=API_KEY)

def generate_text(prompt):
    """
    Generates text using the Google Gemini API.

    Args:
        prompt (str): The prompt for text generation.

    Returns:
        str: The generated text, or an error message if the API call fails.
    """
    try:
        # Use a suitable Gemini model, e.g., 'gemini-1.5-flash-latest' or 'gemini-1.5-pro-latest'
        model = genai.GenerativeModel('gemini-1.5-flash-latest')
        response = model.generate_content(
            prompt,
            generation_config=genai.GenerationConfig(
                max_output_tokens=100,
                temperature=0.7
            )
        )
        # Accessing the text from the response object
        if response.candidates and response.candidates[0].content.parts:
             # Concatenate text from all parts
            generated_text = "".join(part.text for part in response.candidates[0].content.parts)
            return generated_text.strip()
        else:
            return "Could not generate text."

    except Exception as e:
        return f"An error occurred: {e}"

def summarize_text(text):
    """
    Summarizes the given text using the Google Gemini API.

    Args:
        text (str): The text to summarize.

    Returns:
        str: The summarized text, or an error message if the API call fails.
    """
    try:
        # Use a suitable Gemini model, e.g., 'gemini-1.5-flash-latest' or 'gemini-1.5-pro-latest'
        model = genai.GenerativeModel('gemini-1.5-flash-latest')
        response = model.generate_content(
            f"Summarize the following text:\n\n{text}",
            generation_config=genai.GenerationConfig(
                max_output_tokens=150 # Adjust as needed for summary length
            )
        )
        # Accessing the text from the response object
        if response.candidates and response.candidates[0].content.parts:
            # Concatenate text from all parts
            summarized_text = "".join(part.text for part in response.candidates[0].content.parts)
            return summarized_text.strip()
        else:
            return "Could not generate summary."

    except Exception as e:
        return f"An error occurred: {e}"

# Example usage:
if __name__ == "__main__":
    input_prompt = "Write a short story about a robot learning to feel."
    print(f"Prompt: {input_prompt}")
    generated_story = generate_text(input_prompt)
    print("\nGenerated Text:")
    print(generated_story)

    sample_text = """
    Artificial intelligence (AI) is a broad field of computer science that is concerned with building smart machines capable of performing tasks that typically require human intelligence. AI can be categorized into two main types: narrow AI and general AI. Narrow AI, also known as weak AI, is designed and trained for a specific task. Virtual assistants like Siri and Alexa are examples of narrow AI. General AI, or strong AI, is a theoretical type of AI that would have all the cognitive abilities of a human. The development of general AI is a long-term goal for many researchers.
    """
    print("Original Text:")
    print(sample_text)

    summary = summarize_text(sample_text)
    print("\nSummary:")
    print(summary)
