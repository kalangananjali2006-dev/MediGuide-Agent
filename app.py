import streamlit as st
def coordinator_agent(question):

    q = question.lower()


    if any(word in q for word in [
        "chest",
        "breath",
        "bleeding",
        "unconscious",
        "severe pain"
    ]):

        return "🚨 Emergency Agent"


    elif any(word in q for word in [
        "stress",
        "anxiety",
        "sad",
        "sleep",
        "mental"
    ]):

        return "🧠 Mental Wellness Agent"


    elif any(word in q for word in [
        "fever",
        "pain",
        "cough",
        "symptom",
        "headache"
    ]):

        return "🩺 Symptom Agent"


    elif any(word in q for word in [
        "diet",
        "food",
        "exercise",
        "fitness"
    ]):

        return "🥗 Lifestyle Agent"


    else:

        return "📚 Health Education Agent"
from database_chat import save_chat, get_chats


st.set_page_config(
    page_title="MediGuide AI",
    page_icon="🩺",
    layout="centered"
)


# ---------------- USER DATABASE ----------------

users = {
    "demo": "1234"
}


def check_user(username, password):

    return users.get(username) == password



def create_user(username, password):

    if username in users:

        return False

    users[username] = password

    return True



# ---------------- AGENT SYSTEM ----------------


def agent_response(agent, question):

    if agent == "🚨 Emergency Agent":

        return "If this is serious or life threatening, please contact emergency services."


    elif agent == "🧠 Mental Wellness Agent":

        return "I understand. Try relaxation, breathing exercises, and talking with someone you trust."


    elif agent == "🩺 Symptom Agent":

        return "I can provide general health information. Monitor symptoms and consult a healthcare professional."


    elif agent == "🥗 Lifestyle Agent":

        return "Healthy lifestyle includes balanced food, exercise, hydration, and proper sleep."


    elif agent == "📚 Health Education Agent":

        return "I can explain health topics and provide educational information."


    else:

        return "Welcome to MediGuide AI."



# ---------------- SESSION ----------------


if "logged_in" not in st.session_state:

    st.session_state.logged_in = False


if "username" not in st.session_state:

    st.session_state.username = ""



# ---------------- LOGIN PAGE ----------------


if not st.session_state.logged_in:


    st.title("🩺 MediGuide AI")

    st.write(
        "Agentic AI Health & Wellness Assistant"
    )


    tab1, tab2 = st.tabs(
        [
            "🔐 Login",
            "📝 Create Account"
        ]
    )


    with tab1:


        username = st.text_input(
            "Username"
        )


        password = st.text_input(
            "Password",
            type="password"
        )


        if st.button("Login"):


            if check_user(username, password):

                st.session_state.logged_in = True

                st.session_state.username = username

                st.success(
                    "Login successful"
                )

                st.rerun()


            else:

                st.error(
                    "Wrong username or password"
                )



    with tab2:


        new_username = st.text_input(
            "New Username"
        )


        new_password = st.text_input(
            "New Password",
            type="password"
        )


        if st.button("Create Account"):


            if create_user(
                new_username,
                new_password
            ):

                st.success(
                    "Account created"
                )

            else:

                st.error(
                    "Username exists"
                )



    st.stop()



# ---------------- MAIN APP ----------------


st.title("🩺 MediGuide AI")


st.write(
    f"Welcome, {st.session_state.username} 👋"
)


agents = [

    "🧠 Mental Wellness Agent",

    "🩺 Symptom Agent",

    "🥗 Lifestyle Agent",

    "📚 Health Education Agent",

    "🚨 Emergency Agent"

]


selected_agent = st.selectbox(
    "Choose Agent",
    agents
)



user_input = st.chat_input(
    "Ask your health question"
)



if user_input:


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


    st.chat_message(
        "user"
    ).write(
        user_input
    )


    st.chat_message(
        "assistant"
    ).write(
        answer
    )



# ---------------- HISTORY ----------------


with st.expander(
    "📜 Chat History"
):


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



if st.sidebar.button("Logout"):

    st.session_state.logged_in = False

    st.rerun()
