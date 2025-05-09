import streamlit as st
import re
import html
import pandas as pd
import matplotlib.pyplot as plt
from googleapiclient.discovery import build
from textblob import TextBlob
from googletrans import Translator
import http.client
import json
import requests
from dotenv import load_dotenv
import os 

load_dotenv()
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")

if not YOUTUBE_API_KEY or not TWITTER_API_KEY:
    st.error("API keys are missing! Please check your .env file!2")

# Function to extract video ID from URL
def extract_video_id(url):
    if "youtube.com/watch?v=" in url:
        return url.split("v=")[1].split("&")[0]
    return None

# Function to extract tweet ID from URL
def extract_tweet_id(url):
    return url.strip('/').split("/")[-1]


def remove_emojis(text):
    emoji_pattern = re.compile(
        "["
        "\U0001F600-\U0001F64F"  # Emoticons
        "\U0001F300-\U0001F5FF"  # Symbols & pictographs
        "\U0001F680-\U0001F6FF"  # Transport & map symbols
        "\U0001F700-\U0001F77F"  # Alchemical symbols
        "\U0001F780-\U0001F7FF"  # Geometric shapes
        "\U0001F800-\U0001F8FF"  # Supplemental arrows
        "\U0001F900-\U0001F9FF"  # Supplemental symbols & pictographs
        "\U0001FA00-\U0001FA6F"  # Chess symbols, etc.
        "\U0001FA70-\U0001FAFF"  # More symbols
        "\U00002702-\U000027B0"  # Dingbats
        "\U000024C2-\U0001F251"  # Enclosed characters
        "]+",
        flags=re.UNICODE
    )
    return emoji_pattern.sub('', text)

# Preprocess Comment (Preserve Telugu and other non-ASCII characters)
def preprocess_comment(comment):
    comment = html.unescape(comment)
    comment = re.sub(r'http[s]?://\S+|www\.\S+', '', comment)  # Remove URLs
    comment = re.sub(r'<.*?>', '', comment)  # Remove HTML tags
    comment = re.sub(r'@\w+', '', comment)  # Remove Twitter handles (e.g., @username)
    comment = remove_emojis(comment)  # Remove only emojis
    return ' '.join(comment.split())  # Remove extra spaces (but keep Telugu)


# Fetch YouTube comments
def fetch_youtube_comments(video_id, api_key):
    youtube = build('youtube', 'v3', developerKey=api_key)
    comments = []
    request = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        textFormat="plainText",
        maxResults=100
    )
    while request:
        results = request.execute()
        for item in results['items']:
            comments.append(item['snippet']['topLevelComment']['snippet']['textDisplay'])
        request = youtube.commentThreads().list_next(request, results)
    return comments

# Fetch tweets using Twitter API
def fetch_tweets(tweet_id, api_key):
    conn = http.client.HTTPSConnection("twitter-api45.p.rapidapi.com")
    headers = {
        'x-rapidapi-key': "68acfccf96msh43988501728891ep174caejsna4f16e4418ad",
        'x-rapidapi-host': "twitter-api45.p.rapidapi.com"
    }
    conn.request("GET", f"/latest_replies.php?id={tweet_id}", headers=headers)
    res = conn.getresponse()
    data = res.read()
    if res.status == 200:
        tweets = json.loads(data.decode("utf-8"))
        return [tweet['text'] for tweet in tweets.get('timeline', [])]
    return []

# Sentiment Analysis
def analyze_sentiment(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    sentiment = 'positive' if polarity > 0 else 'negative' if polarity < 0 else 'neutral'
    return {'sentiment': sentiment, 'polarity': polarity}

# Translate Text using Google Translator
def transliterate_and_translate(text):
    if not text.strip():
        return None
    try:
        translator = Translator()
        translation = translator.translate(text, src='auto', dest='en')
        return translation.text
    except Exception as e:
        print(f"Error during translation for '{text}': {e}")
        return None
st.markdown("""
    <div style="position: fixed; bottom: 10px; right: 10px; background-color: rgba(0, 0, 0, 0.5); padding: 10px; border-radius: 8px; width: auto;">
        <h3 style="color: white; font-size: 18px; font-weight: bold; text-align: center;">A Project By:</h3>
        <p style="color: white; font-size: 14px; line-height: 1.6;">
            <strong>S.K.Mruduvani</strong><br>
            GitHub <a href="https://github.com/Mrudu17" target="_blank">
                <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" width="18" height="18" style="vertical-align: middle;">
            </a><br>
            LinkedIn <a href="https://www.linkedin.com/in/s-k-mruduvani" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="18" height="18" style="vertical-align: middle;">
            </a><br><br>
            <strong>Kataru Shreya</strong><br>
            GitHub <a href="https://github.com/KataruShreya" target="_blank">
                <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" width="18" height="18" style="vertical-align: middle;">
            </a><br>
            LinkedIn <a href="https://www.linkedin.com/in/shreyakataru" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="18" height="18" style="vertical-align: middle;">
            </a><br>
        </p>
    </div>
""", unsafe_allow_html=True)

# Streamlit UI
st.markdown("<h1 style='text-align: center;'>Sentiment Analysis of Transliterated Social Media Comments</h1>", unsafe_allow_html=True)

st.markdown("<h4 style='text-align: center;'>Select a platform to analyze comments</h4>", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

def social_button(icon_path, label, key):
    st.image(icon_path, width=50)
    if st.button(label, key=key):
        st.session_state.platform_selected = key

with col1:
    social_button("images/youtube.png", "YouTube", "youtube")
with col2:
    social_button("images/X.png", "⠀⠀X⠀⠀", "twitter")
with col3:
    social_button("images/instagram.png", "instagram", "ig")
with col4:
    social_button("images/facebook.png", "facebook", "fb")

if "platform_selected" not in st.session_state:
    st.session_state.platform_selected = None

# Common function to run analysis
def run_analysis(comments):
    total_comments = len(comments)
    sentiment_counts = {'positive': 0, 'negative': 0, 'neutral': 0}
    translations = []
    
    progress_bar = st.progress(0)
    
    for i, comment in enumerate(comments):
        preprocessed_comment = preprocess_comment(comment)  # Preprocess comment
        translated_text = transliterate_and_translate(preprocessed_comment)  # Translate preprocessed comment
        
        if translated_text:
            sentiment = analyze_sentiment(translated_text)
            sentiment_counts[sentiment['sentiment']] += 1
            translations.append({
                'Original Comment': comment,
                'Preprocessed Comment': preprocessed_comment,
                'Translated Comment': translated_text,
                'Sentiment': sentiment['sentiment']
            })
        progress_bar.progress(min(int(((i + 1) / total_comments) * 100), 100))
    
    df = pd.DataFrame(translations)
    st.success("Analysis complete!")
    st.dataframe(df)
    
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("Download CSV", data=csv, file_name="sentiment_analysis.csv", mime="text/csv")
    
    fig, ax = plt.subplots(figsize=(2, 2))
    ax.pie(
        sentiment_counts.values(), 
        labels=sentiment_counts.keys(), 
        autopct='%1.1f%%', 
        colors= ['green', 'red', 'gray'],
        textprops={'color': 'white','fontsize': 5}
    )
    ax.set_title("Sentiment Distribution", fontsize=10, fontweight='bold',color='white')
    fig.patch.set_facecolor("#0E1117")
    ax.set_facecolor("#0E1117")
    st.pyplot(fig)
    
    most_common_sentiment = max(sentiment_counts, key=sentiment_counts.get)
    sentiment_percentage = (sentiment_counts[most_common_sentiment] / sum(sentiment_counts.values())) * 100
    
    st.markdown(f"""
    <div style='text-align: center;'>
        <h2 style="color: white; font-size: 30px; font-weight: bold;">Overall Sentiment</h2>
        <h2 style="color: white; font-size: 25px;">{most_common_sentiment.capitalize()} ({sentiment_percentage:.2f}%)</h2>
    </div>
    """, unsafe_allow_html=True)
    

if st.session_state.platform_selected:
    if st.session_state.platform_selected == "youtube":
        youtube_url = st.text_input("Enter the YouTube video URL:")
        if st.button("Analyze"):
            video_id = extract_video_id(youtube_url)
            if video_id:
                run_analysis(fetch_youtube_comments(video_id,YOUTUBE_API_KEY))
            else:
                st.error("Invalid YouTube URL!")
    elif st.session_state.platform_selected == "twitter":
        tweet_url = st.text_input("Enter the Tweet URL:")
        if st.button("Analyze"):
            tweet_id = extract_tweet_id(tweet_url)
            run_analysis(fetch_tweets(tweet_id,TWITTER_API_KEY))
    else:
        st.warning("🚀 Check back later! Support for this platform is coming soon.")