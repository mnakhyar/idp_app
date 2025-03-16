# auth/login.py
import streamlit as st
from auth.auth_utils import authenticate

def login_page():
    st.title("Login to Individual Development Plan")

    # Pastikan key 'authenticated' ada
    if "authenticated" not in st.session_state:
        st.session_state["authenticated"] = False

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if authenticate(username, password):
            st.session_state["authenticated"] = True
            st.success("Login successful! Redirecting...")

            # ⬇⬇ HACK: Reload otomatis (setelah 0.5 detik) dengan JavaScript ⬇⬇
            st.markdown(
                """
                <script>
                setTimeout(function(){
                    window.location.reload(2);
                }, 500);
                </script>
                """,
                unsafe_allow_html=True
            )
            st.stop()  # Hentikan eksekusi lanjutan agar tidak error
        else:
            st.error("Invalid username or password.")
