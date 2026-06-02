import pandas as pd

DATA_FOLDER = "data/"
DATASET_FILE = "raw/Musical_instruments_reviews.csv"
RAW_DATASET_PATH = f"{DATA_FOLDER}{DATASET_FILE}"


def clean_data():
    df = pd.read_csv(RAW_DATASET_PATH)

    df = df[["reviewText", "overall", "summary"]]

    df.to_csv("data/clean/cleaned_reviews.csv", index=False)

    print(df.head())


clean_data()
