################################################################################
# Download of Blobs in specified container
# 2025/02/02 Created by potofo
################################################################################
#! pip install azure-storage-blob
#! pip install azure-identity
#! pip install python-dotenv

# refer to https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blob-upload-python

import io
import os
import uuid
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, ContainerClient, BlobBlock, BlobClient, StandardBlobTier
from azure.core.exceptions import ResourceNotFoundError
from dotenv import load_dotenv

################################################################################
# Initialize Azure Blob Storage service client.
################################################################################
def init_blob_service():
    # Load .env file
    load_dotenv()

    # Get connection string from environment variable
    connection_string_tamplate = os.getenv("AZURE_STORAGE_CONNECTION_STRING_TEMPLATE")
    storage_accoount = os.getenv("AZURE_STORAGE_ACCOUNT")
    storage_key = os.getenv("AZURE_STORAGE_KEY")

    # Create connection_string
    if not connection_string_tamplate:
        raise ValueError("Environment variable 'AZURE_STORAGE_CONNECTION_STRING_TEMPLATE' is not set. Please check your .env file.")
    else:
        connection_string = connection_string_tamplate
        connection_string = connection_string.replace("{AZURE_STORAGE_ACCOUNT}",storage_accoount)
        connection_string = connection_string.replace("{AZURE_STORAGE_KEY}",storage_key)

    # Create the BlobServiceClient object
    return BlobServiceClient.from_connection_string(connection_string)

################################################################################
#  Upload specified file to the specified container and specified blob.
################################################################################
def upload_blob_file(blob_service_client: BlobServiceClient, container_name: str, blob_name: str, local_file_path: str):
    """
    Upload a file to Azure Blob Storage
    :param blob_service_client: BlobServiceClient object
    :param container_name: Name of the container
    :param blob_name: Name of the blob (including path)
    :param local_file_path: Local path of the file to upload
    """
    try:
        container_client = blob_service_client.get_container_client(container=container_name)
        with open(file=local_file_path, mode="rb") as data:
            blob_client = container_client.upload_blob(name=blob_name, data=data, overwrite=True)
            print(f"Successfully uploaded {local_file_path} to {container_name}/{blob_name}")
    except Exception as e:
        print(f"Error uploading file: {str(e)}")
        raise

################################################################################
# main process
################################################################################
def main():
    # Execute main process.
    try:
        # Initialize BlobServiceClient
        blob_service_client = init_blob_service()
        container_name = os.getenv("AZURE_STORAGE_CONTAINER_NAME")

        # Get blob name and local file path from user input
        print("\nAzure Blob Storage Uploader")
        print("--------------------------------")
        #local_file_path = input("Please enter the local file path to upload: ")
        local_file_path = "test.txt"
        #blob_name = input("Please enter the destination blob name (e.g., folder/file.txt): ")
        blob_name = "test.txt"

        # Validate inputs
        if not blob_name or not local_file_path:
            raise ValueError("Blob name and local file path are required.")
        
        if not os.path.exists(local_file_path):
            raise ValueError(f"Specified file not found: {local_file_path}")

        # Upload the specified blob
        upload_blob_file(blob_service_client, container_name, blob_name, local_file_path)

    except ValueError as e:
        print(f"Configuration Error: {str(e)}")
    except ResourceNotFoundError:
        print("Process terminated.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
    finally:
        # Close BlobServiceClient
        if 'blob_service_client' in locals():
            blob_service_client.close()

if __name__ == "__main__":
    main()