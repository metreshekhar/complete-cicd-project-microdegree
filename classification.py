import streamlit as st
import boto3
from botocore.exceptions import NoCredentialsError
import os

# S3 Config
AWS_ACCESS_KEY = ''
AWS_SECRET_KEY = ''
BUCKET_NAME = ''
REGION = 'us-east-1'

# Create S3 client
s3 = boto3.client(
    's3',
    region_name=REGION,
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY
)

st.title("🗂️ S3 File Manager")

# Upload section
st.header("📤 Upload File to S3")
upload_file = st.file_uploader("Choose a file to upload", type=None)
if upload_file:
    s3.upload_fileobj(upload_file, BUCKET_NAME, upload_file.name)
    st.success(f"Uploaded `{upload_file.name}` successfully!")

# List files
st.header("📁 Files in S3 Bucket")
try:
    contents = s3.list_objects_v2(Bucket=BUCKET_NAME)
    if "Contents" in contents:
        for obj in contents['Contents']:
            filename = obj['Key']
            col1, col2 = st.columns([3, 1])
            col1.write(filename)
            if col2.button("Download", key=filename):
                s3.download_file(BUCKET_NAME, filename, filename)
                with open(filename, "rb") as f:
                    st.download_button(label="Click to download", data=f, file_name=filename)
                os.remove(filename)
    else:
        st.info("No files found in the bucket.")
except NoCredentialsError:
    st.error("AWS credentials not found. Please check your configuration.")

