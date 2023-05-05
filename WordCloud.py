import streamlit as st

# for steps to install/import textblob and nltk, see https://blog.jcharistech.com/2020/12/14/deploying-nlp-apps-on-streamlit-sharing/

import textblob_download_utils
from textblob import TextBlob

from wordcloud import WordCloud
import matplotlib.pyplot as plt

st.title("Word Cloud of Shakespeare Sonnets")

st.header("Sonnet Cloud")

txt = st.text_area('Copy-paste a Sonnet here')
# st.write('you typed:', txt)

my_valence = TextBlob(txt)
st.write('sentiment of the sonnet is:', my_valence.sentiment)

cloud_sonnet = WordCloud().generate(txt)
# cloud_sonnet # returns a wordcloud object: <wordcloud.wordcloud.WordCloud at 0x7f6611fd8dc0>

plt.imshow(cloud_sonnet, interpolation='bilinear')
plt.axis('off')
plt.show()
st.pyplot()
