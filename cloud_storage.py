import dropbox
import os 
from dropbox.files import WriteMode

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        for root,dirs,files in os.walk(file_from):
            for filename in file:
                lpath=os.path.join(root,filename)
                rpath=os.path.relpath(lpath,file_from)
                dpath=os.path.join(file_to,rpath)
                with open(lpath,'rb') as f:
                    dbx.files_upload(f.read(), dpath,mode=WriteMode('overwrite'))
                    
def main():
    access_token = 'sl.A6vrSWUy-P9lutic18kLmjw3gt8kin7RcFaSWBovVstgsmYoijLitCCfThq_BjNIRs3HCN9VBvOfgv03NZl8KJv8RJjunIX5_R1ERRenEw6CTyawsXTwZ4bFYYfV-tTL5ojjg-I'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer : -")
    file_to = input("enter the full path to upload to dropbox:- ")  # This is the full path to upload the file to, including name that you wish the file to be called once uploaded.

    transferData.upload_file(file_from, file_to)
    print("file has been moved !!!")


main()
