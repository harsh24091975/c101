import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)


        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.A6vrSWUy-P9lutic18kLmjw3gt8kin7RcFaSWBovVstgsmYoijLitCCfThq_BjNIRs3HCN9VBvOfgv03NZl8KJv8RJjunIX5_R1ERRenEw6CTyawsXTwZ4bFYYfV-tTL5ojjg-I'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer : -")
    file_to = input("enter the full path to upload to dropbox:- ")  # This is the full path to upload the file to, including name that you wish the file to be called once uploaded.

    transferData.upload_file(file_from, file_to)
    print("file has been moved !!!")


main()
