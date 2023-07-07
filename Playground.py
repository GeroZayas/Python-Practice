import streamlit as st

st.info('This is a purely informational message', icon="📡")
with st.expander('See explanation'):
    st.write("""
        The chart above shows some numbers I picked for you.
        I rolled actual dice for these, so they're *guaranteed* to
        be random.
    """)