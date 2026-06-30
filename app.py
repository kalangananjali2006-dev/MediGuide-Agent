import streamlit as st

st.set_page_config(
    page_title="MediGuide AI",
    page_icon="🩺",
    layout="centered"
)

# Header
st.title("🩺 MediGuide AI")
st.subheader("Agentic AI Health & Wellness Assistant")

st.write(
    "An AI solution aligned with SDG 3: Good Health and Well-being"
)

st.info(
    "⚠️ MediGuide AI provides general health information only. "
    "It does not replace professional medical advice."
)


# Agent selection demo
def choose_agent(message):

    import google.generativeai as genai

    model = genai.GenerativeModel("gemini-2.5-flash")

    prompt = f"""
You are a Coordinator Agent.

Choose the correct agent:

🩺 Symptom Agent:
For pain, fever, illness, symptoms

🧠 Mental Wellness Agent:
For stress, anxiety, emotions, mood

🥗 Lifestyle Agent:
For sleep, food, exercise, habits

📚 Health Education Agent:
For general health questions

User message:
{message}

Reply only with the agent name.
"""

    response = model.generate_content(prompt)

    return response.text

# Chat box
user = st.text_input(
    "Ask MediGuide AI:"
)


if st.button("Send"):

    if user:

        agent = choose_agent(user)

        st.success(
            f"Agent selected: {agent}"
        )

        st.write(
            "🤖 MediGuide AI Response:"
        )

        st.write(
            f"""
Based on your question:

**{user}**

The {agent} is handling your request.

MediGuide AI suggests:
- Maintain healthy habits
- Monitor your wellbeing
- Seek professional medical help if symptoms are serious
"""
        )


# Sidebar
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

st.sidebar.title("SDG Goal")

st.sidebar.write(
"SDG 3: Good Health and Well-being"
)
