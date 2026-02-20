import streamlit as st
from datetime import datetime

# Warm theme
st.markdown("""
    <style>
    body { background-color: #F8F4E9; color: #2E3B3B; font-family: 'Nunito', sans-serif; }
    h1, h2, h3 { font-family: 'Merriweather', serif; color: #6B8E7C; }
    .stButton > button { background-color: #A7C7B2; color: white; border-radius: 8px; }
    .stButton > button:hover { background-color: #6B8E7C; }
    .card { background: white; padding: 16px; border-radius: 12px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); margin: 16px 0; }
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Merriweather:wght@400;700&family=Nunito:wght@400;600&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)

st.set_page_config(page_title="Church Family", page_icon="🙏", layout="wide")

# Simple session state for "login" demo (no real auth here)
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.name = ""
    st.session_state.role = "Member"

if not st.session_state.logged_in:
    st.title("Welcome to Church Family App")
    name = st.text_input("Your Name")
    if st.button("Enter as Member"):
        if name:
            st.session_state.logged_in = True
            st.session_state.name = name
            st.rerun()
    if st.button("Enter as Admin (demo)"):
        st.session_state.logged_in = True
        st.session_state.name = "Pastor"
        st.session_state.role = "Admin"
        st.rerun()
else:
    st.sidebar.title(f"Hi {st.session_state.name} 🙏")
    page = st.sidebar.radio("Menu", ["Home", "Prayer Requests", "Directory"])

    if page == "Home":
        st.title(f"Hello, {st.session_state.name}! God bless you.")
        st.markdown("### Today's Verse")
        st.info("John 3:16 – For God so loved the world...")
        st.markdown("### Recent Prayers (demo)")
        st.markdown('<div class="card"><strong>Prayer for healing</strong><br>Prayed: 12 times • by Sarah</div>', unsafe_allow_html=True)

    elif page == "Prayer Requests":
        st.title("Prayer Requests")
        with st.expander("Submit New Prayer"):
            title = st.text_input("Title")
            desc = st.text_area("Details")
            public = st.checkbox("Make public?", value=True)
            if st.button("Submit"):
                if title and desc:
                    st.success(f"Submitted: {title}")
                else:
                    st.error("Fill title & details")

        st.markdown("### Public Prayers")
        if st.button("Prayed (demo counter)"):
            st.write("Prayer count increased! (resets on refresh)")

    elif page == "Directory":
        st.title("Church Directory")
        st.markdown('<div class="card">Sarah • Member</div>', unsafe_allow_html=True)
        st.markdown('<div class="card">Pastor • Admin</div>', unsafe_allow_html=True)
        if st.session_state.role == "Admin":
            st.info("Admin view: Full details here (stub)")
