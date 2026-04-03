🤖 AI Doubt Solver

An AI-powered doubt solving chatbot built using Python, NLP, and Streamlit.
This app answers programming, AI, and computer science questions using similarity matching.

🚀 Features

- 💬 Chat-style doubt solving
- 🧠 NLP-based question matching
- ⚡ Fast response using TF-IDF
- 🎨 Clean UI using Streamlit
- 📚 Expandable knowledge base
- 🧑‍💻 Beginner-friendly project

🛠️ Tech Stack

- Python
- Streamlit (UI)
- Scikit-learn (NLP)
- NumPy
- TF-IDF Vectorizer
- Cosine Similarity

📁 Project Structure

ai_doubt_solver/
│
├── app.py
├── data.py
├── requirements.txt
└── README.md

📦 Installation

Clone or download the project and install dependencies:

pip install -r requirements.txt

▶️ Run the Project

streamlit run app.py

Then open:

http://localhost:8501

🧠 How It Works

1. User enters a doubt
2. TF-IDF converts questions to vectors
3. Cosine similarity finds best match
4. Closest answer is displayed
5. If no match → fallback message

💡 Example Questions

- What is Python
- What is machine learning
- What is numpy
- What is regression
- What is flask
- What is AI

📈 Future Improvements

- ChatGPT-like conversation memory
- Voice input support
- Internet knowledge API
- Login system
- Chat history
- Dark mode UI
