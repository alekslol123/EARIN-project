from pathlib import Path
import shutil
import kagglehub


def download_dataset():
    # download the dataset and copy it to the target folder
    SCRIPT_DIR = Path(__file__).resolve().parent
    TARGET_FOLDER = SCRIPT_DIR / "data" / "raw"

    path_downloaded = Path(kagglehub.dataset_download("eswarchandt/amazon-music-reviews"))

    if TARGET_FOLDER.exists():
        shutil.rmtree(TARGET_FOLDER)

    shutil.copytree(path_downloaded, TARGET_FOLDER)

    print("Path to dataset files:", TARGET_FOLDER)


download_dataset()
