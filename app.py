
import streamlit as st

import pickle

import nltk

import re

from nltk.corpus import stopwords

from nltk.stem import PorterStemmer

nltk.download(
    "stopwords"
)

stemmer = PorterStemmer()

stop_words = set(
    stopwords.words(
        "english"
    )
)

# load files
model = pickle.load(
    open(
        "model.pkl",
        "rb"
    )
)

vectorizer = pickle.load(
    open(
        "vectorizer.pkl",
        "rb"
    )
)

# NLP preprocessing
def preprocess_text(text):

    text = text.lower()

    text = re.sub(
        r"[^a-zA-Z]",
        " ",
        text
    )

    words = text.split()

    processed = []

    for word in words:

        if word not in stop_words:

            processed.append(
                stemmer.stem(
                    word
                )
            )

    return " ".join(
        processed
    )

st.set_page_config(
    page_title="Fake News Detector"
)

st.title(
    "📰 Fake News Detection using NLP"
)

news = st.text_area(
    "Enter news article"
)

if st.button(
    "Predict"
):

    clean_news = preprocess_text(
        news
    )

    vec = vectorizer.transform(
        [
            clean_news
        ]
    )

    pred = model.predict(
        vec
    )[0]

    probs = model.predict_proba(
        vec
    )[0]

    st.write(
        f"Fake Probability: {probs[0]*100:.2f}%"
    )

    st.write(
        f"Real Probability: {probs[1]*100:.2f}%"
    )

    if pred == 0:

        st.error(
            "❌ FAKE NEWS"
        )

    else:

        st.success(
            "✅ REAL NEWS"
        )
