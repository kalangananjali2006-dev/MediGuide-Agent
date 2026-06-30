import google.generativeai as genai


def setup_gemini(api_key):
    genai.configure(
        api_key=api_key
    )


def ask_gemini(prompt):

    models = list(genai.list_models())

    available_model = None

    for m in models:
        if "generateContent" in m.supported_generation_methods:
            available_model = m.name
            break

    if available_model is None:
        return "No Gemini model available for this API key."

    model = genai.GenerativeModel(
        available_model
    )

    response = model.generate_content(
        prompt
    )

    return response.text
