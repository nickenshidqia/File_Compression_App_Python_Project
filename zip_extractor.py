import zipfile

def extract_archive(archivepath, dest_dir):
    with zipfile.ZipFile(archivepath, 'r') as archive:
        archive.extractall(dest_dir)

#testing
if __name__ == "__main__":
    extract_archive("D:\Dokumen\PELATIHAN UDEMY\Python\pythonProject\compressed.zip",
                    "D:\Dokumen\PELATIHAN UDEMY\Python\pythonProject/file")