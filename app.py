import streamlit as st
from database import (
    create_database,
    create_user,
    check_user
)
USERS = {
    "demo": "1234",
    "admin": "admin123"
}

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
from datetime import datetime


st.set_page_config(
    page_title="MediGuide AI",
    page_icon="🩺",
    layout="wide"
)

create_database()


if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if not st.session_state.logged_in:

    st.markdown(
        """
        <h1 style='text-align:center;'>
        🩺 MediGuide AI
        </h1>

        <p style='text-align:center;'>
        Your Agentic AI Health & Wellness Assistant
        </p>
        """,
        unsafe_allow_html=True
    )


    tab1, tab2 = st.tabs(
        ["🔐 Login", "📝 Create Account"]
    )


    with tab1:

    username = st.text_input(
    "Username",
    key="login_username"
)

password = st.text_input(
    "Password",
    type="password",
    key="login_password"
)

 st.button(
    "Login",
    key="login_button"
)
st.button(
    "Create Account",
    key="signup_btn"
)
    result = check_user(
        username,
        password
    )

    if result:

        st.session_state.logged_in = True
        st.session_state.username = username

        st.success("Login successful")

        st.rerun()

    else:

        st.error("Invalid username or password")
        

    if st.button("Sign In"):

        if username in USERS and USERS[username] == password:

            st.session_state.logged_in = True
            st.session_state.username = username

            st.success("Login successful")

            st.rerun()

        else:

            st.error("Wrong username or password")


    st.stop()

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
if not st.session_state.logged_in:

    st.title("🔐 MediGuide AI Account")

    option = st.selectbox(
        "Choose option",
        [
            "Login",
            "Create Account"
        ]
    )


    username = st.text_input(
        "Username"
    )

    password = st.text_input(
        "Password",
        type="password"
    )


    if option == "Create Account":

        if st.button("Sign Up"):

            if create_user(username, password):

                st.success(
                    "Account created. Now login."
                )

            else:

                st.error(
                    "Username already exists"
                )


    else:

        if st.button("Login"):

            if check_user(username, password):

                st.session_state.logged_in = True

                st.success(
                    "Welcome!"
                )

                st.rerun()

            else:

                st.error(
                    "Invalid login"
                )


    st.stop()
st.title("🩺 MediGuide AI")
if "username" in st.session_state:

    st.success(
        f"Welcome, {st.session_state.username} 👋"
    )
st.subheader("Agentic AI Health & Wellness Assistant")

st.info(
"""
🌍 SDG 3: Good Health and Well-being

MediGuide AI uses multiple specialized agents coordinated by an AI routing system.
"""
)


# Sidebar

      
st.sidebar.title("🤖 AI Agent System")

st.sidebar.info(
"""
Coordinator AI routes your query to the right specialist agent.
"""
)

st.sidebar.markdown("### Active Agents")

st.sidebar.success("🧠 Mental Wellness Agent")
st.sidebar.success("🩺 Symptom Agent")
st.sidebar.success("🥗 Lifestyle Agent")
st.sidebar.success("📚 Health Education Agent")
st.sidebar.warning("🚨 Emergency Agent")
     
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
