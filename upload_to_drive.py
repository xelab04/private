from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth

# For using listdir()
import os


# Below code does the authentication
# part of the code
# Creates local webserver and auto
# handles authentication.
gauth = GoogleAuth()

gauth.LoadCredentialsFile("mycreds.txt")
if gauth.credentials is None:
    # Authenticate if they're not there
    gauth.LocalWebserverAuth()
elif gauth.access_token_expired:
    # Refresh them if expired
    gauth.Refresh()
else:
    # Initialize the saved creds
    gauth.Authorize()
# Save the current credentials to a file
gauth.SaveCredentialsFile("mycreds.txt")
# Creates local webserver and auto
# handles authentication.
drive = GoogleDrive(gauth)

# replace the value of this variable
# with the absolute path of the directory
#path = r"C:\Games\Battlefield"

# iterating thought all the files/folder
# of the desired directory
#for x in os.listdir(path):
x = "/home/alex/Desktop/covid.csv"
f = drive.CreateFile({'title': "Covid Spreadsheet.csv"})
f.SetContentFile(x)
f.Upload()

# Due to a known bug in pydrive if we
# don't empty the variable used to
# upload the files to Google Drive the
# file stays open in memory and causes a
# memory leak, therefore preventing its
# deletion
f = None
