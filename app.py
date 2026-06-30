import streamlit as st
from datetime import datetime


st.set_page_config(
    page_title="MediGuide AI",
    page_icon="🩺",
    layout="wide"
)


# ---------- Session ----------
if "messages" not in st.session_state:
    st.session_state.messages = []


# ---------- Agent Logic ----------
def coordinator_agent(user_text):

    text = user_text.lower()

    if any(x in text for x in ["chest pain", "emergency", "can't breathe", "breathing problem"]):
        return "🚨 Emergency Agent"

    elif any(x in text for x in ["stress", "anxiety", "sad", "mental"]):
        return "🧠 Mental Wellness Agent"

    elif any(x in text for x in ["sleep", "diet", "food", "exercise"]):
        return "🥗 Lifestyle Agent"

    elif any(x in text for x in ["fever", "pain", "symptom", "sick"]):
        return "🩺 Symptom Agent"

    else:
        return "📚 Health Education Agent"



def agent_response(agent, question):

    responses = {

        "🚨 Emergency Agent":
        "This may need urgent attention. Please contact emergency medical services or a healthcare professional.",

        "🧠 Mental Wellness Agent":
        "Try relaxation techniques, healthy routines, talking with trusted people, and consider professional support if needed.",

        "🥗 Lifestyle Agent":
        "Focus on balanced nutrition, good sleep habits, hydration, and regular physical activity.",

        "🩺 Symptom Agent":
        "Track your symptoms, rest, stay hydrated, and consult a healthcare professional if symptoms are serious or continue.",

        "📚 Health Education Agent":
        "I can provide general health information and awareness guidance."
    }

    return responses[agent]



# ---------- UI ----------

st.title("🩺 MediGuide AI")
st.subheader("Agentic AI Health & Wellness Assistant")

st.info(
"""
🌍 SDG 3: Good Health and Well-being

MediGuide AI uses multiple specialized agents coordinated by an AI routing system.
"""
)


# Sidebar

st.sidebar.title("🤖 AI Agents")

st.sidebar.write(
"""
🎯 Coordinator Agent

🚨 Emergency Agent

🧠 Mental Wellness Agent

🥗 Lifestyle Agent

🩺 Symptom Agent

📚 Health Education Agent
"""
)


# Input

user_input = st.chat_input(
    "Ask MediGuide AI..."
)


if user_input:

    selected_agent = coordinator_agent(user_input)

    answer = agent_response(
        selected_agent,
        user_input
    )


    st.session_state.messages.append(
        {
            "time": datetime.now().strftime("%H:%M"),
            "user": user_input,
            "agent": selected_agent,
            "answer": answer
        }
    )



# Chat display

for msg in st.session_state.messages:

    with st.chat_message("user"):
        st.write(msg["user"])


    with st.chat_message("assistant"):

        st.success(
            msg["agent"]
        )

        st.write(
            msg["answer"]
        )


# Dashboard

st.divider()

st.subheader("📊 Agent Activity Dashboard")

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Total Queries",
        len(st.session_state.messages)
    )


with col2:

    if st.session_state.messages:
        st.metric(
            "Last Agent",
            st.session_state.messages[-1]["agent"]
        )
    else:
        st.metric(
            "Last Agent",
            "None"
        )
