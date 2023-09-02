import streamlit as st
from streamlit_extras.switch_page_button import switch_page

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

st.balloons()

'💪'
'Your goal has been set!'
'Spicy and Daisy will help you stay on track!'

if st.button('End demo'):
    switch_page('main')