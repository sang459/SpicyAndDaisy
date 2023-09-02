import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import json
from functools import partial

st.set_page_config(initial_sidebar_state="collapsed")

st.markdown("""
            <style>
            [data-testid="stSidebar"] {
                display: none
            }

            [data-testid="collapsedControl"] {
                display: none
            }
            </style>
            """, unsafe_allow_html=True)

OPENAI_API_KEY = st.secrets['OPENAI_API_KEY']

if 'page' not in st.session_state:
    st.session_state['page'] = 'main'


def main():

    st.title("Onboarding Demo")
    st.markdown("*Reflect and stay on track*")
    st.markdown('Goal tracker + personal journal + calendar, combined with a chatbot.')
    st.markdown('In this demo, you will be able to experience the onboarding process with a help from Spicy and Daisy.')
    
    to_onboarding = st.button("Let's get started!")
    if to_onboarding:
        switch_page("onboarding")




if __name__ == "__main__":
    main()
