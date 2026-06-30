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

    message = message.lower()

    if "stress" in message or "anxiety" in message:
        return "🧠 Mental Wellness Agent"

    elif "sleep" in message or "diet" in message or "exercise" in message:
        return "🥗 Lifestyle Agent"

    elif "pain" in message or "fever" in message:
        return "🩺 Symptom Agent"

    else:
        return "📚 Health Education Agent"


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
