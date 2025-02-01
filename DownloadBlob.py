################################################################################
# Download of Blobs in specified container
# 2025/02/02 Created by potofo
################################################################################
#! pip install azure-storage-blob
#! pip install azure-identity
#! pip install python-dotenv

# refer to https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blob-download-python

import io
import os
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobClient
from dotenv import load_dotenv
from azure.core.exceptions import ResourceNotFoundError

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
#  Download specified blobs in the specified container.
################################################################################
def download_blob_to_file(blob_service_client: BlobServiceClient, container_name, blob_name):
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
    # Create download directory if it doesn't exist
    os.makedirs('downloads', exist_ok=True)
    # Convert blob name to path for processing
    normalized_name = blob_name.replace('/', os.path.sep)
    download_path = os.path.join('downloads', normalized_name)
    # Create required directories
    os.makedirs(os.path.dirname(download_path), exist_ok=True)
    with open(file=download_path, mode="wb") as sample_blob:
        download_stream = blob_client.download_blob()
        sample_blob.write(download_stream.readall())
    print(f"Downloaded blob '{blob_name}' to {download_path}")


################################################################################
# main process
################################################################################
def main():
    # Execute main process.
    try:
        # Initialize BlobServiceClient
        blob_service_client = init_blob_service()
        container_name = os.getenv("AZURE_STORAGE_CONTAINER_NAME")

        # Get blob name from user input
        #blob_name = input("Please enter the blob name to download: ")
        #blob_name = "burgerking.md"
        blob_name = "burgerking/burgerking.ja-JP.md"

        # Download the specified blob
        download_blob_to_file(blob_service_client, container_name, blob_name)

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