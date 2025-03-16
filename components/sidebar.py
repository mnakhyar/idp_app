# components/sidebar.py
import streamlit as st

def show_sidebar():
    """
    Show navigation sidebar after successful login.
    """
    with st.sidebar:
        st.header("Navigation")

        # Contoh tombol navigasi
        if st.button("Dashboard"):
            st.session_state["current_page"] = "dashboard"

        if st.button("Individual Development Plan"):
            st.session_state["current_page"] = "idp"

        if st.button("Elevate Your Journey"):
            st.session_state["current_page"] = "elevate"

        # Tombol logout
        if st.button("Logout"):
            st.session_state["authenticated"] = False
            st.success("Logout successful. Redirecting...")

            # ⬇⬇ Reload otomatis setelah 0.5 detik ⬇⬇
            st.markdown(
                """
                <script>
                setTimeout(function(){
                    window.location.reload(1);
                }, 500);
                </script>
                """,
                unsafe_allow_html=True
            )
            st.stop()  # Hentikan eksekusi agar tidak ada error
