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

if 'key' not in st.session_state:
    st.session_state.goals = {}
    st.session_state.goals['MONDAY'] = []
    st.session_state.goals['TUESDAY'] = []
    st.session_state.goals['WEDNESDAY'] = []
    st.session_state.goals['THURSDAY'] = []
    st.session_state.goals['FRIDAY'] = []
    st.session_state.goals['SATURDAY'] = []
    st.session_state.goals['SUNDAY'] = []

st.subheader("Your Daily Goals:")
goals = st.text_area("Enter your goals for tomorrow (one goal per line):", height=150)
goals_list = goals.split("\n")
for i, goal in enumerate(goals_list):
    st.session_state.goals['MONDAY'].append(goal)
    st.write(f"Goal {i + 1}: {goal}")

if st.button('Confirm'):
    switch_page("set_goal_fin")