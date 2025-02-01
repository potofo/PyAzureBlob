# Azure Blob Storage Operation Tools

## Overview

This project provides a collection of Python scripts for operating Azure Blob Storage. It offers the following functionality:

- List files in a Blob container
- Download files from Blob storage
- Upload files to Blob storage

## Prerequisites

- Python 3.x
- Azure account
- Azure Storage account
- Required Python packages:
  - azure-identity==1.19.0
  - azure-storage-blob==12.24.1
  - python-dotenv==1.0.1

## Setup

1. Install required packages:
```bash
pip install -r requirements.txt
```

2. Configure environment variables:
Copy the `.env_template` file to `.env` and set the following information:

```
AZURE_STORAGE_CONNECTION_STRING_TEMPLATE="DefaultEndpointsProtocol=https;AccountName={AZURE_STORAGE_ACCOUNT};AccountKey={AZURE_STORAGE_KEY};EndpointSuffix=core.windows.net"
AZURE_STORAGE_ACCOUNT="<your-storage-account-name>"
AZURE_STORAGE_KEY="<your-storage-account-key>"
AZURE_STORAGE_CONTAINER_NAME="<your-container-name>"
```

You can find the required information in the following locations:
- Storage Account Name: Azure Portal -> Storage Account -> Overview
- Storage Account Key: Azure Portal -> Storage Account -> Security + networking -> Access keys
- Container Name: Azure Portal -> Storage Account -> Storage Explorer -> BLOB containers

## Usage

### List Blobs

```bash
python ListBlob.py
```

Displays a list of all blobs in the container.

### Download Blobs

```bash
python DownloadBlob.py
```

Downloads the specified blob to the `downloads` directory.
Directory structure is automatically created.

### Upload Blobs

```bash
python UploadBlob.py
```

Uploads local files to Blob storage.
Existing blobs will be overwritten.

## Project Structure

```
PyAzureBlob/
├── .env_template          # Environment variable template
├── .gitignore            # Git ignore settings
├── ListBlob.py           # Script for listing blobs
├── DownloadBlob.py       # Script for downloading blobs
├── UploadBlob.py         # Script for uploading blobs
├── requirements.txt      # List of dependencies
├── downloads/            # Directory for downloaded files
└── uploads/              # Directory for files to upload
```

## Reference Links

- [Azure Blob Storage Documentation](https://learn.microsoft.com/en-us/azure/storage/common/storage-samples-python)
- [Azure Blob Upload Python](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blob-upload-python)
- [Azure Blob Download Python](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blob-download-python)