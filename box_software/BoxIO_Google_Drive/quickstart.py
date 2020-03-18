from __future__ import print_function
import auth
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.http import MediaFileUpload

import json
import os
import requests

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive.file']

# The ID of a sample document.
#DOCUMENT_ID = '195j9eDD3ccgjQRttHhJPymLJUCOUjs-jmwTrekvdjFE'

def upload_mp4(service, file_name, file_path):
    print("Uploading file " + file_name + "...")

    # We have to make a request hash to tell the google API what we're giving it
    body = {'name': file_name}

    # Now create the media file upload object and tell it what file to upload,
    # in this case 'test.html'
    media = MediaFileUpload(file_path, mimetype='video/mp4', chunksize=1048576, resumable=True)
    # media = MediaFileUpload('test_image.png', mimetype='image/png')

    # Now we're doing the actual post, creating a new file of the uploaded type
    request = service.files().create(body=body, media_body=media)
    response = None

    while response is None:
        status, response = request.next_chunk()
        if status:
            print("Uploaded %d%%." % int(status.progress() * 100))

    print('Media Uploaded!')

def main():
    """Shows basic usage of the Docs API.
    Prints the title of a sample document.
    """
    authInst = auth.auth(SCOPES)

    creds = authInst.auth()

    service = build('drive', 'v3', credentials=creds)

    upload_mp4(service, 'test_video.mp4','videos/test_video.mp4')


if __name__ == '__main__':
    main()

