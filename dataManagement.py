from pathlib import Path
import pandas as pd

DATA_FOLDER = "data/"
DATASET_FILE = "raw/Musical_instruments_reviews.csv"
RAW_DATASET_PATH = f"{DATA_FOLDER}{DATASET_FILE}"


def download_dataset():
    # download the dataset and copy it to the target folder
    SCRIPT_DIR = Path(__file__).resolve().parent
    TARGET_FOLDER = SCRIPT_DIR / "data" / "raw"

    path_downloaded = Path(kagglehub.dataset_download("eswarchandt/amazon-music-reviews"))

    if TARGET_FOLDER.exists():
        shutil.rmtree(TARGET_FOLDER)

    shutil.copytree(path_downloaded, TARGET_FOLDER)

    print("Path to dataset files:", TARGET_FOLDER)


def clean_data():
    output_folder = Path("data/clean")
    output_folder.mkdir(parents=True, exist_ok=True)  # create the clean folder first

    df = pd.read_csv(RAW_DATASET_PATH)

    df = df[["reviewText", "overall", "summary"]]

    df.to_csv("data/clean/cleaned_reviews.csv", index=False)

    print(df.head())


def balance_data():  # balance the overall ratings
    pass


if __name__ == "__main__":
    clean_data()
    download_dataset()
    balance_data()
