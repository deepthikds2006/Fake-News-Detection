# 📰 Fake News Detection using NLP and Machine Learning

A Fake News Detection web application built using **Natural Language Processing (NLP)**, **TF-IDF Vectorization**, **Multinomial Naive Bayes**, and **Streamlit**.

The model classifies news articles as **Real** or **Fake** based on the text content entered by the user.

---

## 🚀 Features

✅ News article classification (Fake / Real)  
✅ NLP text preprocessing  
✅ Stopword removal and stemming  
✅ TF-IDF vectorization  
✅ Multinomial Naive Bayes model  
✅ Probability score output  
✅ Interactive Streamlit web interface  

---

## 🛠 Technologies Used

- Python  
- Pandas  
- NLTK  
- Scikit-learn  
- Streamlit  
- Pickle  

---

## 📂 Project Structure

```text
Fake-News-Detection/
│── app.py                 # Streamlit application
│── model.pkl              # Trained model
│── vectorizer.pkl         # TF-IDF vectorizer
│── Fake news Detector.ipynb
│── requirements.txt
│── README.md
```

---

## ⚙️ Project Workflow

### 1. Data Collection
- Load fake and real news datasets
- Assign labels:
  - Fake = 0
  - Real = 1

### 2. Data Preprocessing
- Convert text to lowercase
- Remove special characters
- Remove stopwords
- Apply stemming using Porter Stemmer

### 3. Feature Extraction
TF-IDF Vectorization converts text into numerical form for machine learning.

### 4. Model Training
Model used:

**Multinomial Naive Bayes**

### 5. Prediction
User enters a news article → Model predicts whether it is **Fake** or **Real**

---

## 📊 Model Performance

Accuracy achieved:

```text
95.18%
```

Classification Metrics:

| Metric | Score |
|---------|---------|
| Precision | 95% |
| Recall | 95% |
| F1 Score | 95% |

---

## ▶️ Installation and Setup

Clone repository:

```bash
git clone https://github.com/deepthikds2006/Fake-News-Detection.git
```

Move to project folder:

```bash
cd Fake-News-Detection
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run Streamlit app:

```bash
streamlit run app.py
```

---

## 🖥 Application Interface

Input: News article text  

Output:
- Fake probability
- Real probability
- Prediction result

Example:

```text
Input:
Breaking news article text...

Output:
Fake Probability: 10%
Real Probability: 90%

✅ REAL NEWS
```

---

## 🔮 Future Enhancements

- Deploy using Streamlit Cloud
- Add visualization dashboard
- Use Deep Learning models (LSTM / BERT)
- Improve UI design
- Add live news checking support

---

## 👩‍💻 Author

**Deepthi**


