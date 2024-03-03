## S3 Tools ##

### How to use ###

1. Install boto3 using command line / terminal
```bash
pip install boto3
``````

2. Replace the Bucket name & folder name you want to download in **_download_folder.py_**
```bash
BUCKET = 'bucket'       # Replace with the bucket name you want to download
FOLDER = 'output'             # Name of the folder in s3 bucket
```
3. Run **_download_folder.py_**
```bash
python download_folder.py
```

### Outputs 
Outputs the file to an "output" folder.


