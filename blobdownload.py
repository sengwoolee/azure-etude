import os, uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__

try:
    print("Azure Blob storage v" + __version__ + " - Python quickstart sample")
    # Quick start code goes here

    # Retrieve the connection string for use with the application. The storage
    # connection string is stored in an environment variable on the machine
    # running the application called AZURE_STORAGE_CONNECTION_STRING. If the environment variable is
    # created after the application is launched in a console or with Visual Studio,
    # the shell or application needs to be closed and reloaded to take the
    # environment variable into account.
    connect_str = "<connection string>"

    # Create the BlobServiceClient object which will be used to create a container client
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)

    # Create a file in local data directory to upload and download
    local_path = "./data"

    container_name = 'musicazuretest'
    local_file_name = 'testmusic.mp3'

    # Create a blob client using the local file name as the name for the blob
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=local_file_name)

    download_file_path = os.path.join(local_path, str.replace(local_file_name, '.txt', 'DOWNLOAD.txt'))
    print("\nDownloading blob to \n\t" + download_file_path)

    with open(download_file_path, "wb") as download_file:
        download_file.write(blob_client.download_blob().readall())

except Exception as ex:
    print('Exception:')
    print(ex)
