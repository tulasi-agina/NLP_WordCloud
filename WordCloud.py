import streamlit as st
import textblob_download_utils
from textblob import TextBlob

st.title("Word Cloud of Shakespeare Sonnets")

st.header("Sonnet Cloud")

st.text("past a Sonnet here")
txt = st.text_area('Copy-paste a Sonnet here to create a Word Cloud')
# st.write('you typed:', txt)

my_valence = TextBlob(txt)
st.write('sentiment of the sonnet is:', my_valence.sentiment)
