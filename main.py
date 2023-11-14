import dropbox
import os
from dropbox.files import WriteMode # I got an error so I googled it and found out that I need to import that package :)

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        for root, dirs, files in os.walk(file_from):
            for filename in files:
                path = os.path.join(root, filename)
                relative_path = os.path.relpath(path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)

                with open(path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main():
    access_token = str(open("C:/Users/TayoYuva/Documents/Mine/Studies/White Hat JR/Project/C101/API_KEY.txt", "r").read())
    transferData = TransferData(access_token)

    file_from = input("Enter the folder from: ")
    file_to = input("Enter the folder name into Dropbox: ")
    transferData.upload_file(file_from, file_to)

if __name__ == '__main__': # Used howdoi package
    main()