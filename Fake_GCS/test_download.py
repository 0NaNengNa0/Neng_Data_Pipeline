import os
from google.auth.credentials import AnonymousCredentials
from google.cloud import storage

os.environ.setdefault("STORAGE_EMULATOR_HOST", "http://localhost:4443")


def download_blob(bucket_name, source_blob_name, destination_file_name):
    """Downloads a blob from the bucket."""
    storage_client = storage.Client(
        credentials=AnonymousCredentials(),
        project="test",
    )

    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_name)

    print(
        "Downloaded storage object {} from bucket {} to local file {}.".format(
            source_blob_name, bucket_name, destination_file_name
        )
    )


if __name__ == "__main__":
    bucket_name = input("Please enter bucket name: ")
    source_file = input("Please enter source file: ")
    destination = input("Please enter destination file (leave blank to use the same name): ")

    if destination is None or destination == "":
        destination = source_file.split("/")[-1]

    download_blob(bucket_name, source_file, destination)