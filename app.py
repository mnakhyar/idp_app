# app.py
import streamlit as st
from auth.login import login_page
from components.sidebar import show_sidebar
from app_pages.dashboard import show as show_dashboard
from app_pages import idp
from app_pages.elevate import show as elevate_show


st.set_page_config(
    page_title="IDP",
    page_icon=":memo:",
    layout="wide",
    initial_sidebar_state="collapsed"  # Menyembunyikan sidebar di awal
)

def main():
    if "authenticated" not in st.session_state:
        st.session_state["authenticated"] = False
    if "current_page" not in st.session_state:
        st.session_state["current_page"] = "dashboard"

    if not st.session_state["authenticated"]:
        login_page()
    else:
        show_sidebar()
        # Routing
        if st.session_state["current_page"] == "dashboard":
            show_dashboard()
        if st.session_state["current_page"] == "elevate":
            elevate_show()
        elif st.session_state["current_page"] == "idp":
            idp.show()

if __name__ == "__main__":
    main()
