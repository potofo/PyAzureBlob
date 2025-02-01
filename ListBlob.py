################################################################################
# List of Blobs in specified container
# 2025/02/02 Created by potofo
# the followinf environment variables is required
#   AZURE_STORAGE_CONNECTION_STRING_TEMPLATE
#   AZURE_STORAGE_ACCOUNT:
#     You can confirm the storage account name in [Azure Portal]->[Storage Account]->[Overview]
#   AZURE_STORAGE_KEY:
#     You can confirm the storage account access key in [Azure Portal]->[Storage Account]->[Security + networking]->[Access keys]
#  AZURE_STORAGE_CONTAINER_NAME:
#     You can confirm the container name in [Azure Portal]->[Storage Account]->[Storage Explorer]->[Blob Containers]
################################################################################
#
# (venv) PS Q:\OneDrive\Python\PyAzureBlob> python .\ListBlob.py     
# List of Blobs in container 'ptf-container':
# --------------------------------------------------
# Name: burgerking.md
# Name: burgerking/burgerking.ja-JP.md
# --------------------------------------------------
# Total: 2 blob(s) found.

#! pip install azure-storage-blob
#! pip install azure-identity
#! pip install python-dotenv
# reffer to https://learn.microsoft.com/en-us/azure/storage/common/storage-samples-python

import os
from azure.core.exceptions import ResourceNotFoundError
from dotenv import load_dotenv
from azure.storage.blob import BlobServiceClient

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
# List all blobs in the specified container.
################################################################################
def list_blobs_flat(blob_service_client: BlobServiceClient, container_name: str):
    try:
        container_client = blob_service_client.get_container_client(container=container_name)
        print(f"\nList of Blobs in container '{container_name}':")
        print("-" * 50)

        blob_list = container_client.list_blobs()
        count = 0
        for blob in blob_list:
            count += 1
            print(f"Name: {blob.name}")
        
        print("-" * 50)
        print(f"Total: {count} blob(s) found.")

    except ResourceNotFoundError:
        print(f"Error: Container '{container_name}' not found.")
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

        # Get blob list
        list_blobs_flat(blob_service_client, container_name)

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