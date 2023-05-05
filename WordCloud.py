import streamlit as st

# for steps to install/import textblob and nltk, see https://blog.jcharistech.com/2020/12/14/deploying-nlp-apps-on-streamlit-sharing/

import textblob_download_utils
from textblob import TextBlob

from wordcloud import WordCloud
import matplotlib.pyplot as plt

st.title("Word Cloud of Shakespeare Sonnets")

st.header("Sonnet Cloud")

txt = st.text_area('''
  Shall I compare thee to a summer’s day?
  Thou art more lovely and more temperate:
  Rough winds do shake the darling buds of May,
  And summer’s lease hath all too short a date:
  Sometime too hot the eye of heaven shines,
  And often is his gold complexion dimm’d;
  And every fair from fair sometime declines,
  By chance or nature’s changing course untrimm’d;
  But thy eternal summer shall not fade
  Nor lose possession of that fair thou owest;
  Nor shall Death brag thou wander’st in his shade,
  When in eternal lines to time thou growest:
  So long as men can breathe or eyes can see,
  So long lives this and this gives life to thee.
  ''')
# st.write('you typed:', txt)

my_valence = TextBlob(txt)
st.write('sentiment of the sonnet is:', my_valence.sentiment)

cloud_sonnet = WordCloud().generate(txt)
# cloud_sonnet # returns a wordcloud object: <wordcloud.wordcloud.WordCloud at 0x7f6611fd8dc0>

plt.imshow(cloud_sonnet, interpolation='bilinear')
plt.axis("off")
plt.show()
#st.pyplot()
