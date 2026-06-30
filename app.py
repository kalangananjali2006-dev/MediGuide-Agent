import streamlit as st

st.write(
"""
### 🌍 Problem
People need quick access to basic health awareness and wellness support.

### 💡 AI Solution
MediGuide AI uses multiple agents that collaborate to guide users.

### 🎯 SDG Goal
SDG 3 - Good Health and Well-being
"""
)
st.set_page_config(
    page_title="MediGuide AI",
    page_icon="🩺"
)

if "history" not in st.session_state:
    st.session_state.history = []


st.title("🩺 MediGuide AI")
st.subheader("Chat History")

if "history" in st.session_state:

    for chat in st.session_state.history:

        st.write("👤 User:")
        st.write(chat["question"])

        st.success(
            chat["agent"]
        )


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
