import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from data import qa_pairs

st.set_page_config(page_title="AI Doubt Solver")

st.title("🤖 AI Doubt Solver")
st.write("Ask your programming doubts")

questions = list(qa_pairs.keys())
answers = list(qa_pairs.values())

vectorizer = TfidfVectorizer()
question_vectors = vectorizer.fit_transform(questions)

user_input = st.text_input("Ask your doubt:")

if st.button("Get Answer"):
    user_vec = vectorizer.transform([user_input])
    similarity = cosine_similarity(user_vec, question_vectors)

    index = np.argmax(similarity)
    score = similarity[0][index]

    if score > 0.2:
        st.success(answers[index])
    else:
        st.warning("Sorry, I don't know this yet.")