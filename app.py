import streamlit as st

st.set_page_config(
    page_title="MediGuide AI",
    page_icon="🩺"
)

if "history" not in st.session_state:
    st.session_state.history = []


st.title("🩺 MediGuide AI")
st.subheader("Agentic AI Health & Wellness Assistant")

st.info(
    "SDG 3: Good Health and Well-being\n\n"
    "General health guidance assistant"
)


def choose_agent(message):

    message = message.lower()

    emergency_words = [
        "chest pain",
        "can't breathe",
        "difficulty breathing",
        "emergency",
        "severe bleeding"
    ]

    for word in emergency_words:
        if word in message:
            return "🚨 Emergency Alert Agent"

    if "stress" in message or "anxiety" in message:
        return "🧠 Mental Wellness Agent"

    elif "sleep" in message or "diet" in message:
        return "🥗 Lifestyle Agent"

    elif "pain" in message or "fever" in message:
        return "🩺 Symptom Agent"

    else:
        return "📚 Health Education Agent"

    for word in emergency_words:
        if word in message.lower():
            return "🚨 Emergency Alert Agent"
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

        response = f"""
Agent: {agent}

Your question:
{user}

Health guidance:
Maintain healthy habits, stay aware of your wellbeing,
and consult a healthcare professional for serious concerns.
"""

        st.session_state.history.append(
            {
                "user": user,
                "agent": agent,
                "response": response
            }
        )


st.subheader("Chat History")

for chat in st.session_state.history:

    st.write("👤 User:")
    st.write(chat["user"])

    st.progress(0.85)

st.caption(
    "Coordinator Agent → Specialist Agent → Health Guidance"
)

    st.write(chat["response"])



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
