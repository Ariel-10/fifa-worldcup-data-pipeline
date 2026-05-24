import os
from minio import Minio
from minio.error import S3Error
import pandas as pd

# Connection
client = Minio(
    "localhost:9000",
    access_key="root",
    secret_key="rootroot",
    secure=False  # no HTTPS locally
)

# Config
BUCKET_NAME = "fifa-worldcup"
FILES = [
    "data/raw/wcmatches.csv",
    "data/raw/worldcups.csv",
]

# Create bucket if not exists
def create_bucket():
    if not client.bucket_exists(BUCKET_NAME):
        client.make_bucket(BUCKET_NAME)
        print(f"Bucket '{BUCKET_NAME}' created")
    else:
        print(f"Bucket '{BUCKET_NAME}' already exists")

# Upload CSV files
def upload_files():
    for file_path in FILES:
        file_name = os.path.basename(file_path)
        client.fput_object(
            BUCKET_NAME,
            f"raw/{file_name}",  # path inside bucket
            file_path,           # local path
        )
        print(f"Uploaded: {file_name}")

# Main
if __name__ == "__main__":
    create_bucket()
    upload_files()
    print("Ingestion complete")