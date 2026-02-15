import streamlit as st
from utils import generate_technical_questions

st.set_page_config(page_title="TalentScout Hiring Assistant", page_icon="🤖", layout="centered")

st.title("🤖 TalentScout Hiring Assistant")

# ---------------- SESSION INIT ----------------
if "step" not in st.session_state:
    st.session_state.step = 0
    st.session_state.data = {}
    st.session_state.finished = False
    st.session_state.chat = []

questions = [
    "Full Name?",
    "Email Address?",
    "Phone Number?",
    "Years of Experience?",
    "Desired Position?",
    "Current Location?",
    "Tech Stack?"
]

EXIT_WORDS = ["exit", "quit", "bye", "end"]

# ---------------- GREETING ----------------
if len(st.session_state.chat) == 0:
    greeting = """
👋 **Hello and welcome to TalentScout!**

I'm your AI Hiring Assistant.  
I'll ask a few questions to understand your background and tech skills.

Type **exit** anytime to stop.

Let's begin 👇
"""
    st.session_state.chat.append(("assistant", greeting))
    st.session_state.chat.append(("assistant", questions[0]))

# ---------------- DISPLAY CHAT ----------------
for role, message in st.session_state.chat:
    with st.chat_message(role):
        st.markdown(message)

# ---------------- USER INPUT ----------------
if not st.session_state.finished:

    user_input = st.chat_input("Type your answer...")

    if user_input:

        # show user message on RIGHT
        st.session_state.chat.append(("user", user_input))

        if user_input.lower() in EXIT_WORDS:
            st.session_state.chat.append(("assistant", "Conversation ended. Thank you!"))
            st.session_state.finished = True
            st.rerun()

        # save answer
        current_question = questions[st.session_state.step]
        st.session_state.data[current_question] = user_input
        st.session_state.step += 1

        # ask next question
        if st.session_state.step < len(questions):
            next_q = questions[st.session_state.step]
            st.session_state.chat.append(("assistant", next_q))

        # generate tech questions
        else:
            tech_stack = st.session_state.data["Tech Stack?"]

            st.session_state.chat.append(("assistant", "Generating technical questions... ⏳"))

            tech_q = generate_technical_questions(tech_stack)

            st.session_state.chat.append(("assistant", tech_q))
            st.session_state.chat.append(("assistant", "✅ Thank you! Recruiters will review your profile."))

            st.session_state.finished = True

        st.rerun()
