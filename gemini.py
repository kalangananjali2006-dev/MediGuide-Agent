from google import genai


client = None


def setup_gemini(api_key):

    global client

    client = genai.Client(
        api_key=api_key
    )


def ask_gemini(prompt):

    try:

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )

        return response.text


    except Exception as e:

        return f"Gemini error: {e}"
