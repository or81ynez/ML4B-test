import streamlit as st
st.title('SuperApp')
st.write('Allerlei')
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted ?',
    ('Email','home phone', 'fax')
)
add_slider = st.sidebar.slider(
'Bitte stellen sie ihre Schriftgröße ein:',
0.0,100.0)