import google.generativeai as genai


def setup_gemini(api_key):

    genai.configure(
        api_key=api_key
    )


def ask_gemini(prompt):

    try:

        available_models = []

        for model in genai.list_models():

            if "generateContent" in model.supported_generation_methods:

                available_models.append(model.name)


        if not available_models:

            return "No Gemini model available for this API key."


        model = genai.GenerativeModel(
            available_models[0]
        )


        response = model.generate_content(
            prompt
        )

        return response.text


    except Exception as e:

        return f"Gemini error: {e}"
