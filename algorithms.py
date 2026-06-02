from config import *
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.svm import LinearSVC
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report


def vectorize_data_text():
    df = pd.read_csv(CLEAN_DATASET_PATH)

    df = df.dropna(subset=["reviewText", "summary", "overall"])

    X = df["reviewText"]
    y = df["overall"].astype(int)

    SEED = 42
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=SEED, stratify=y)

    # GLOBAL TF-IDF VECTORIZER
    tfidf = TfidfVectorizer(lowercase=True, stop_words="english", max_features=50000, ngram_range=(1, 2))

    X_train_tfidf = tfidf.fit_transform(X_train)
    X_test_tfidf = tfidf.transform(X_test)

    return X_train_tfidf, X_test_tfidf, y_train, y_test


def naive_bayes():
    nb = MultinomialNB()

    X_train_tfidf, X_test_tfidf, y_train, y_test = vectorize_data_text()
    nb.fit(X_train_tfidf, y_train)

    nb_pred = nb.predict(X_test_tfidf)

    print("Naive Bayes")
    print(classification_report(y_test, nb_pred))


naive_bayes()


def linear_svm():
    svm = LinearSVC()
    X_train_tfidf, X_test_tfidf, y_train, y_test = vectorize_data_text()

    svm.fit(X_train_tfidf, y_train)

    svm_pred = svm.predict(X_test_tfidf)

    print("Linear SVM")
    print(classification_report(y_test, svm_pred))


linear_svm()


def lstm():
    pass
