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

    def health_agent(message, agent):

    prompt = f"""
You are the {agent} in MediGuide AI.

User:
{message}

Give a helpful, safe health response.
Do not diagnose.
"""

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        return "AI connection error: " + str(e)

# Chat box
user = st.text_input(
    "Ask MediGuide AI:"
)


if st.button("Send"):

    if user:

        agent = choose_agent(user)

        st.success(
            f"Selected Agent: {agent}"
        )

        st.write(
            "🤖 MediGuide AI Response:"
        )

        st.write(
            f"""
Your question:
{user}

The {agent} is analyzing your request.

General guidance:
- Maintain healthy habits
- Monitor your wellbeing
- Consult a healthcare professional for serious concerns
"""
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
import streamlit as st

st.set_page_config(
    page_title="MediGuide AI",
    page_icon="🩺"
)

st.title("🩺 MediGuide AI")
st.subheader("Agentic AI Health & Wellness Assistant")

st.info(
    "SDG 3: Good Health and Well-being\n\n"
    "This AI provides general health information only."
)


def choose_agent(message):

    message = message.lower()

    if "stress" in message or "anxiety" in message:
        return "🧠 Mental Wellness Agent"

    elif "sleep" in message or "food" in message or "exercise" in message:
        return "🥗 Lifestyle Agent"

    elif "pain" in message or "fever" in message:
        return "🩺 Symptom Agent"

    else:
        return "📚 Health Education Agent"



def get_response(message, agent):

    return f"""
**Agent:** {agent}

I analyzed your question:

{message}

General guidance:
- Maintain healthy habits
- Track your wellbeing
- Consult a healthcare professional for serious concerns

"""


user = st.text_input("Ask MediGuide AI:")


if st.button("Send"):

    if user:

        agent = choose_agent(user)

        st.success(
            "Selected Agent: " + agent
        )

        st.write(
            get_response(user, agent)
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
