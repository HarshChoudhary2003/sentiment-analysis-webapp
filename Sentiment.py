import streamlit as st
from textblob import TextBlob
import pandas as pd
import emoji
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

st.set_page_config(page_title="Sentiment Analysis Web App", layout="centered")


@st.cache_data
def get_text(raw_url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    req = Request(raw_url, headers=headers)
    page = urlopen(req)
    soup = BeautifulSoup(page, 'html.parser')
    fetched_text = ' '.join(map(lambda p: p.text, soup.find_all('p')))
    return fetched_text

# ...existing code...
def main():
    """Sentiment Analysis Emoji App"""
    st.title(" 🧠Sentiment Analysis Web App Using NLP and ML 💡")
    activities = ["Sentiment", "Text Analysis on URL", "About"]
    choice = st.sidebar.selectbox("Select Activity", activities)
    if choice == "Sentiment":
        st.subheader("Sentiment Analysis")
        user_input = st.text_area("Enter Your Text",)
        if st.button("Analyze"):
            blob = TextBlob(user_input)
            sentiment = blob.sentiment.polarity

            if sentiment > 0:
                custom_emoji = emoji.emojize(":thumbs_up:", language='alias')
            elif sentiment < 0:
                custom_emoji = emoji.emojize(":thumbs_down:", language='alias')
            else:
                custom_emoji = emoji.emojize(":neutral_face:", language='alias')

            st.write(f"Sentiment Score: {sentiment}")
            st.write(f"Sentiment Emoji: {custom_emoji}")
    elif choice == "Text Analysis on URL": 
        st.subheader("Text Analysis From a web URL")
        url = st.text_input("Enter URL", "https://en.wikipedia.org/wiki/Natural_language_processing")  
        text_preview_length = st.slider("Length of preview", 50, 500, 200)
        if st.button("Submit"):
            if url:
                sentiment = get_text(url)
                blob = TextBlob(sentiment)
                len_of_full_text = len(sentiment)
                len_of_short_text = round(len(sentiment)/text_preview_length)

                st.success(f"Length of full text: {len_of_full_text}")
                st.success(f"Length of short text: {len_of_short_text}")
                st.info(sentiment[:len_of_short_text])

                c_sentences = [str(sent) for sent in blob.sentences]
                c_sentiments = [sent.sentiment.polarity for sent in blob.sentences]
                
                df = pd.DataFrame(list(zip(c_sentences, c_sentiments)), columns=['Sentences', 'Sentiments'])
                st.dataframe(df)
    else:
        st.subheader("About this App")
        st.info("Welcome to the Sentiment Analysis Web App – a smart, user-friendly tool designed to understand the emotions behind text and online content")
        st.info("This application is powered by Natural Language Processing (NLP) and Machine Learning (ML) algorithms that classify text into different sentiments such as positive, negative, or neutral. To make it even more engaging, the results are represented using expressive emojis 😊😒👌❤️😍😁😎😀😉, helping users instantly grasp the mood conveyed by the text.")
        st.info("✨ Key Features")
        st.info("📝 Text Sentiment Analysis – Type or paste any text, and the app will instantly predict its sentiment.")
        st.info("🌐 URL Sentiment Analysis – Provide a website link, and the app performs web scraping to fetch the content and analyze its sentiment.")
        st.info("😀 Emoji-Based Output – Instead of just plain labels, results are shown with emojis, making the analysis more interactive and visually appealing.")
        st.info("⚡ Fast & Accurate – Built using optimized NLP models for quick and reliable sentiment predictions.")
        st.info("📊 Practical Applications – Can be used for social media analysis, product reviews, blog insights, feedback analysis, and more.")

        
if __name__ == "__main__":
    main()