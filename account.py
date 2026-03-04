import streamlit as st


def app():
    def t():
        st.session_state.signedout = False
        st.session_state.main = False
        st.session_state.username = ''         
    st.text('Name: '+st.session_state.username)
    st.text('Email id: '+st.session_state.useremail)
    st.button('Sign out', on_click=t)
    st.image("3.png")
            
