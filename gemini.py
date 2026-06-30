import google.generativeai as genai


def setup_gemini(api_key):

    genai.configure(
        api_key=api_key
    )


def ask_gemini(prompt):

    model = genai.GenerativeModel(
        "gemini-1.5-flash"
    )

    response = model.generate_content(
        prompt
    )

    return response.text
