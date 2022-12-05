# -*- coding: utf-8 -*-
from google.cloud import storage
from urllib.request import urlopen
import json
import os

# Upload Key Json File localy
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "Local path to SA key"

# Upload data to bucket
def upload_blob_from_stream(bucket_name, url, destination_blob_name, project_id):
    """Uploads bytes from a stream or other file-like object to a blob."""

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    # Upload data from the stream to your bucket.
    blob.upload_from_string(
        data=json.dumps(json.loads(urlopen(url).read())),
        content_type='application/json')

    print(
        f"Stream data uploaded to {destination_blob_name} in bucket {bucket_name}."
    )
    result = destination_blob_name + ' upload completed'
    return {'response' : result}


upload_blob_from_stream('bucket-name',"https://www.gov.uk/bank-holidays.json","example_bank_holidays.json","project-ID")



