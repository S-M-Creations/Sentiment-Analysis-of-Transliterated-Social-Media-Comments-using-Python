# 🌟 **Sentiment Analysis of Transliterated Social Media Comments** 🌟

## 🧑‍💻 **Developed by:**
- **Kataru Shreya**  |  [GitHub Profile](https://github.com/KataruShreya) | [LinkedIn Profile](https://www.linkedin.com/in/shreyakataru)
- **S.K. Mruduvani**  |  [GitHub Profile](https://github.com/Mrudu17) | [LinkedIn Profile](https://www.linkedin.com/in/s-k-mruduvani)

---

## 📜 **Project Overview**

Welcome to **Sentiment Analysis of Transliterated Social Media Comments!** This project dives into analyzing the sentiment of social media comments, specifically from YouTube and Twitter (X), using Natural Language Processing (NLP) techniques. The goal is to assess the overall mood (positive, negative, or neutral) of user comments on various platforms and provide insightful analysis for content creators and marketers.

---

## 🚀 **How It Works**

### 1. **Platform Selection:**
- You can choose to analyze comments from **YouTube**, **Twitter**, or **Instagram** (coming soon). Simply click on the platform of your choice.

### 2. **Input Your URL:**
- For **YouTube**: Paste the URL of a YouTube video to fetch the latest comments.
- For **Twitter**: Paste the URL of a tweet to fetch the replies.

### 3. **Processing & Analysis:**
- The application will **preprocess** the comments by removing unnecessary text like URLs, emojis, and handles, while keeping non-ASCII characters (such as Telugu).
- **Sentiment Analysis** will then classify each comment as either **positive**, **negative**, or **neutral**.
- **Translation**: If comments are not in English, they will be automatically **transliterated and translated** to English for analysis.

### 4. **Results:**
- The app will present a **detailed analysis** of the comments, along with a **pie chart** showing the sentiment distribution.
- You can download the results in **CSV** format for further analysis.

---

## 🔧 **Technologies Used**
- **Python** (Core Language)
- **Streamlit** (Interactive Web Interface)
- **Google YouTube API** (Fetching YouTube comments)
- **Twitter API** (Fetching tweets)
- **TextBlob** (Sentiment Analysis)
- **Googletrans** (Translation)
- **Matplotlib** (Data Visualization)

---

## 🌍 **Features**

### 🎯 **Sentiment Analysis**:
Using the **TextBlob** library, the sentiment of each comment is analyzed. The polarity of the text determines if it's **positive**, **negative**, or **neutral**.

### 🌐 **Multilingual Handling**:
Supports multiple languages and retains non-ASCII characters like **Telugu** while removing unwanted characters (e.g., emojis).

### 📥 **Downloadable Results**:
Once the analysis is complete, the results can be downloaded in a **CSV** format to further study or integrate into other applications.

### 📊 **Data Visualization**:
A **pie chart** visualizes the sentiment distribution, showing you how people feel overall about the content.

---
## How to Create YouTube & Twitter API from RapidAPI and storing them

### Step 1: Create YouTube API Key from Google Cloud

1. Go to [Google Cloud Console](https://console.cloud.google.com/) and sign in.
2. Click **Select a Project** → **New Project** → Give it a name.
3. Navigate to **APIs & Services** → **Library**.
4. Search for **YouTube Data API v3** and enable it.
5. Go to **APIs & Services** → **Credentials**.
6. Click **Create Credentials** → **API Key**.
7. Copy the generated API Key.

### Step 2: Create Twitter API Key from RapidAPI

1. Go to [RapidAPI](https://rapidapi.com/) and sign in.
2. Search for **Twitter API** in the RapidAPI marketplace.
3. Select an API and subscribe to a pricing plan (free or paid).
4. Navigate to the **Endpoints** section to test API requests.
5. Copy the **API Key** from the **Header Parameters** section.

### Step 3: Store API Keys in a `.env` File

1. Inside your Streamlit project, create a `.env` file.
2. Add the API keys to the `.env` file:

```env
# .env file
YOUTUBE_API_KEY="your_youtube_api_key"
TWITTER_API_KEY="your_twitter_api_key"
```

### Step 4: Run the .py file

```
streamlit run fine_name.py
```

---
## 📷 OUTPUT SCREENS

![image](https://github.com/user-attachments/assets/354e32f6-3e8b-4372-ac7a-b192ecca66b5)

![image](https://github.com/user-attachments/assets/01e73311-9058-40c3-8785-7b3a526dc517)

![image](https://github.com/user-attachments/assets/c2917a74-7bc6-4aee-9cb4-f446d16d5fc8)

---

## 📈 **Use Case Scenarios**

- **Content Creators**: Get insights into how your audience is reacting to your YouTube videos or Twitter posts.
- **Marketing Teams**: Monitor customer feedback on social media, and identify the overall sentiment toward your brand.
- **Researchers**: Analyze public opinion on specific topics by collecting comments from social media.

---
