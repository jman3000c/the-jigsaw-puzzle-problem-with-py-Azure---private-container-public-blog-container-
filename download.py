from azure.storage.blob import BlobServiceClient

try:
    blob_service_client = BlobServiceClient(account_url="https://inversionrecruitment.blob.core.windows.net/")
    
    for i in range(1, 1201):  # This will loop from 1 to 1200
        file_name = f"({i}).png"
        blob_client = blob_service_client.get_blob_client("find-the-code", file_name)
        print(f"\nDownloading blob to local file: {file_name}")
        
        with open(f"/mnt/c/Users/Mandla/Downloads/Documents/js/images/{file_name}", "wb") as download_file:
            download_file.write(blob_client.download_blob().readall())

        print("Download completed!")

except Exception as ex:
    print('Exception:')
    print(ex)

