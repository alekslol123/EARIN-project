import kagglehub

# Download latest version
path = kagglehub.dataset_download("eswarchandt/amazon-music-reviews")

print("Path to dataset files:", path)
