import streamlit as st
from streamlit_extras.switch_page_button import switch_page

# Example of emotional report and Daisy's feedback data structure
if 'reports' not in st.session_state:
    st.session_state.reports = {
        day: {
            'emotion_report': "Example emotion report for " + day,
            'feedback': "Daisy's feedback for " + day
        } for day in ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']
    }

# Set the page title
st.title("Goals Page")

# Create a table to display the goals, emotional report, and Daisy's feedback for each day
table_data = {
    'Day': [],
    'Goals': [],
    'Emotion Report': [],
    'Daisy\'s Feedback': []
}

for day in ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']:
    table_data['Day'].append(day)
    table_data['Goals'].append(", ".join(st.session_state.goals[day]))
    table_data['Emotion Report'].append(st.session_state.reports[day]['emotion_report'])
    table_data['Daisy\'s Feedback'].append(st.session_state.reports[day]['feedback'])

# Display the table
st.table(table_data)

# Button to edit the goals which redirects to the "set_goals" page
if st.button('Edit Goals'):
    # Assuming you have a function called `change_page` to handle the page redirection
    switch_page("set_goals")

# Button to move to the "checklist" page
if st.button('Move to Checklist'):
    switch_page("checklist")
