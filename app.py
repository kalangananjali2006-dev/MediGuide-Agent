import streamlit as st

st.title("🩺 MediGuide AI")
st.write("Agentic AI Health & Wellness Assistant")

st.warning(
    "This AI provides general health information only."
)

user = st.text_input("Ask your health question")

if st.button("Send"):
    if user:
        st.success("MediGuide AI is analyzing: " + user)
