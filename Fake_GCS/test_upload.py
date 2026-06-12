import os
from google.auth.credentials import AnonymousCredentials
from google.cloud import storage

os.environ.setdefault("STORAGE_EMULATOR_HOST", "http://localhost:4443")


def upload_blob(bucket_name, source_file_path, destination_blob_name=None):
    """Uploads a file to the bucket."""

    if destination_blob_name is None or destination_blob_name == "":
        destination_blob_name = source_file_path.split("\\")[-1].split("/")[-1]

    storage_client = storage.Client(
        credentials=AnonymousCredentials(),
        project="test",
    )

    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_path)

    print(
        "File {} uploaded to bucket {} as {}.".format(
            source_file_path, bucket_name, destination_blob_name
        )
    )


if __name__ == "__main__":
    bucket_name = input("Please enter bucket name: ")
    source_file = input("Please enter full path to your file: ")
    destination = input("Please enter destination name in bucket (leave blank to use the same name): ")

    upload_blob(bucket_name, source_file, destination)