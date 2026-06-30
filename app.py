import streamlit as st

st.set_page_config(
    page_title="MediGuide AI",
    page_icon="🩺"
)

if "history" not in st.session_state:
    st.session_state.history = []


st.title("🩺 MediGuide AI")
st.subheader("Agentic AI Health & Wellness Assistant")

st.write(
"""
🌍 SDG 3: Good Health and Well-being

MediGuide AI uses multiple agents to provide health awareness support.
"""
)


def choose_agent(message):

    message = message.lower()

    if "chest pain" in message or "emergency" in message:
        return "🚨 Emergency Alert Agent"

    elif "stress" in message or "anxiety" in message:
        return "🧠 Mental Wellness Agent"

    elif "sleep" in message or "diet" in message:
        return "🥗 Lifestyle Agent"

    elif "pain" in message or "fever" in message:
        return "🩺 Symptom Agent"

    else:
        return "📚 Health Education Agent"



user = st.text_input("Ask MediGuide AI")


if st.button("Send"):

    if user:

        agent = choose_agent(user)

        st.session_state.history.append(
            {
                "question": user,
                "agent": agent
            }
        )

        st.success(
            "Selected Agent: " + agent
        )



st.subheader("Chat History")

for chat in st.session_state.history:

    st.write("User:")
    st.write(chat["question"])

    st.write("Agent:")
    st.write(chat["agent"])



st.sidebar.title("AI Agents")

st.sidebar.write(
"""
🎯 Coordinator Agent

🚨 Emergency Agent

🧠 Mental Wellness Agent

🥗 Lifestyle Agent

🩺 Symptom Agent

📚 Education Agent
"""
)
