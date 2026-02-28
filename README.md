# 📰 Fake News Detection using Machine Learning

## 📌 Overview

This project implements a Machine Learning–based system that automatically classifies news headlines as **Real** or **Fake** using Natural Language Processing (NLP) techniques. The goal is to detect misleading information and demonstrate how text classification models can be applied to real-world problems.

---

## 🎯 Objective

To build an end-to-end machine learning pipeline that:

* preprocesses textual news data
* converts text into numerical features
* trains a classification model
* predicts whether news is real or fake

---

## 🧠 Model Used

* Logistic Regression (primary model)

---

## ⚙️ Technologies & Libraries

* Python
* Pandas
* NumPy
* Scikit-learn
* NLTK
* TF-IDF Vectorizer

---

## 🔄 Workflow

```
Dataset → Text Cleaning → Stopword Removal → Vectorization (TF-IDF)
→ Train/Test Split → Model Training → Prediction → Evaluation
```

---

## 📊 Results

The model achieved approximately:

**Accuracy: ~82.8%**

This demonstrates reliable performance for headline-based fake news classification using classical machine learning methods.

---

## 📁 Dataset

The dataset contains:

* news headlines
* metadata
* label indicating whether news is real or fake


---

## ▶️ How to Run the Project

### 1️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 2️⃣ Run Notebook

Open and run:

```
fake_news_detection.ipynb
```

---

## 🚀 Future Improvements

* Compare multiple models (Naive Bayes, SVM, Random Forest)
* Train on full news articles instead of headlines
* Hyperparameter tuning
* Deploy as a web app interface
* Use deep learning NLP models (LSTM/BERT)

---

## 💡 Key Learning Outcomes

* Text preprocessing techniques
* Feature extraction using TF-IDF
* Training supervised ML models
* Evaluating classification performance
* Building reproducible ML pipelines

---

## Conclusion
*This model can be extended with deep learning architectures such as LSTM or BERT for improved performance.

## 👩‍💻 Author

**Deepthi**

---

## ⭐ Project Purpose

This project was developed as part of a self-learning journey in **Machine Learning and NLP** to strengthen practical skills for internships, research programs, and real-world applications.
 of self-learning journey in Machine Learning and NLP to strengthen practical skills for internships and placements.
