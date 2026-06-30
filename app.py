import streamlit as st
from database_chat import (
    save_chat,
    get_chats
)
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
        <div style="
        text-align:center;
        padding:20px;
        ">

        <h1 style="color:#2E86C1;">
        🩺 MediGuide AI
        </h1>

        <p>
        Agentic AI Health & Wellness Assistant
        </p>

        <p>
        Your intelligent health companion powered by specialized AI agents.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


    tab1, tab2 = st.tabs(
        [
            "🔐 Login",
            "📝 Create Account"
        ]
    )


    with tab1:

        st.subheader("Welcome Back 👋")


        username = st.text_input(
            "Username",
            key="login_username"
        )

        password = st.text_input(
            "Password",
            type="password",
            key="login_password"
        )


        if st.button(
            "Login",
            key="login_btn"
        ):

            if check_user(
                username,
                password
            ):

                st.session_state.logged_in = True

                st.session_state.username = username

                st.success(
                    "Login successful"
                )

                st.rerun()

            else:

                st.error(
                    "Invalid username or password"
                )


    with tab2:

        st.subheader("Create Your Account 🚀")


        new_username = st.text_input(
            "Choose Username",
            key="signup_username"
        )

        new_password = st.text_input(
            "Choose Password",
            type="password",
            key="signup_password"
        )


        if st.button(
            "Create Account",
            key="signup_btn"
        ):

            if create_user(
                new_username,
                new_password
            ):

                st.success(
                    "Account created! Please login."
                )

            else:

                st.error(
                    "Username already exists"
                )


    st.stop()



with tab2:

    new_username = st.text_input(
        "Create Username",
        key="signup_username"
    )

    new_password = st.text_input(
        "Create Password",
        type="password",
        key="signup_password"
    )


    if st.button(
        "Create Account",
        key="signup_btn"
    ):

        if create_user(
            new_username,
            new_password
        ):

            st.success(
                "Account created. Please login."
            )

        else:

            st.error(
                "Username already exists"
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

    if agent == "🚨 Emergency Agent":

        return (
            "This may require urgent attention. "
            "If symptoms are severe, contact emergency services."
        )


    elif agent == "🧠 Mental Wellness Agent":

        return (
            "I understand. Try taking some time to relax, "
            "practice breathing exercises, and talk to someone you trust."
        )


    elif agent == "🩺 Symptom Agent":

        return (
            "I can help you understand symptoms. "
            "Monitor your condition and consider consulting a healthcare professional."
        )


    elif agent == "🥗 Lifestyle Agent":

        return (
            "Maintain a balanced diet, regular activity, "
            "good sleep, and healthy daily habits."
        )


    elif agent == "📚 Health Education Agent":

        return (
            "I can explain health topics in simple terms "
            "and provide general information."
        )


    else:

        return (
            "I am your MediGuide AI assistant. "
            "How can I help you today?"
        )



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
with st.expander("📜 Chat History"):

    chats = get_chats(
        st.session_state.username
    )

    for chat in chats:

        st.write(
            "🤖",
            chat[0]
        )

        st.write(
            "Q:",
            chat[1]
        )

        st.write(
            "A:",
            chat[2]
        )

        st.divider()
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

save_chat(
    st.session_state.username,
    selected_agent,
    user_input,
    answer
)

   save_chat(
    st.session_state.username,
    selected_agent,
    user_input,
    answer
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
