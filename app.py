import streamlit as st

st.set_page_config(
    page_title="MediGuide AI",
    page_icon="🩺"
)

st.title("🩺 MediGuide AI")
st.subheader("Agentic AI Health & Wellness Assistant")

st.info(
    "SDG 3: Good Health and Well-being\n\n"
    "General health guidance assistant"
)


def choose_agent(message):

    message = message.lower()

    if "stress" in message or "anxiety" in message:
        return "🧠 Mental Wellness Agent"

    elif "sleep" in message or "diet" in message:
        return "🥗 Lifestyle Agent"

    elif "pain" in message or "fever" in message:
        return "🩺 Symptom Agent"

    else:
        return "📚 Health Education Agent"


user = st.text_input("Ask MediGuide AI:")


if st.button("Send"):

    if user:

        agent = choose_agent(user)

        st.success("Selected Agent: " + agent)

        st.write(
            "🤖 MediGuide AI Response:"
        )

        st.write(
            "Your question: " + user
        )

        response = f"""
You are the {agent}.

User question:
{user}

Give a helpful health and wellness response.
Keep it simple.
Do not diagnose.
Suggest professional help if needed.
"""

st.write(response)


st.sidebar.title("AI Agents")

st.sidebar.write(
"""
🎯 Coordinator Agent

🩺 Symptom Agent

🧠 Mental Wellness Agent

🥗 Lifestyle Agent

📚 Health Education Agent
"""
)
