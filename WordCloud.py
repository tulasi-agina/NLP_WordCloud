import streamlit as st

st.title("Word Cloud of Shakespeare Sonnets")

st.header("Sonnet Cloud")

st.text("past a Sonnet here")
txt = st.text_input()
st.write('you typed:', txt)
