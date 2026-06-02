from pathlib import Path
import kagglehub

# Folder next to this script
script_dir = Path(__file__).resolve().parent
dataset_dir = script_dir / "data"

path = kagglehub.dataset_download("eswarchandt/amazon-music-reviews", output_dir=str(dataset_dir))

print("Path to dataset files:", path)
