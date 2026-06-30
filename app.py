import streamlit as st

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
def agent_response(agent, question):

    q = question.lower()


    if agent == "🚨 Emergency Agent":

        if "pain" in q or "bleeding" in q or "breath" in q:

            return (
                "This may need urgent attention. "
                "If symptoms are severe, seek emergency medical help."
            )

        return (
            "Tell me more about the emergency situation "
            "so I can guide you better."
        )


    elif agent == "🧠 Mental Wellness Agent":

        if "stress" in q or "anxiety" in q:

            return (
                "Stress and anxiety can feel overwhelming. "
                "Try slow breathing, relaxation exercises, "
                "and consider speaking with someone you trust."
            )

        elif "sleep" in q:

            return (
                "For better sleep, keep a regular schedule, "
                "reduce screen time before bed, and create a calm routine."
            )

        return (
            "I can support your mental wellness. "
            "Tell me what you are currently experiencing."
        )


    elif agent == "🩺 Symptom Agent":

        if "fever" in q:

            return (
                "Fever can happen due to many causes. "
                "Rest, stay hydrated, and monitor your symptoms."
            )

        elif "headache" in q:

            return (
                "Headaches may have different causes. "
                "Consider hydration, rest, and tracking triggers."
            )

        return (
            "Describe your symptoms, when they started, "
            "and their severity."
        )


    elif agent == "🥗 Lifestyle Agent":

        if "diet" in q or "food" in q:

            return (
                "A balanced diet includes vegetables, fruits, "
                "protein sources, whole grains, and enough water."
            )

        elif "exercise" in q:

            return (
                "Regular physical activity supports overall health. "
                "Start with activities suitable for your fitness level."
            )

        return (
            "I can help with nutrition, exercise, and healthy habits."
        )


    elif agent == "📚 Health Education Agent":

        if "diabetes" in q:

            return (
                "Diabetes affects how the body manages blood sugar. "
                "Healthy lifestyle choices and medical guidance are important."
            )

        return (
            "I can explain health topics. "
            "Ask me about a specific condition or topic."
        )


    return "How can I help you today?"


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
