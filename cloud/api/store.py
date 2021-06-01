#storage.py

import logging
import os

from google.cloud import storage

#configure this environment variable via app.yaml
CLOUD_STORAGE_BUCKET = os.environ['CLOUD_STORAGE_BUCKET']


client = storage.Client()
bucket = client.get_bucket('sign-image')


def download_image():
	imageBlob = bucket.get_blob(r"/([^/]*[^/\d])\d*\.jpg")
	imageBlob.download_as_string()
