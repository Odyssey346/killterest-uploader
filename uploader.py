import requests
import random
def main():
    print("Welcome to the Killterest Uploader by Odyssey346. This allows you to upload any .mp4 to Killterest.com")
    print("Let's get started. Please type in your file's path (type like C:\\Users\\User\\Videos\\video.mp4)")
    filelocation = input("My file's path is: ")
    print(filelocation)
    print("What do you want your score to be?")
    myscore = input("My score is: ")
    print(myscore)
    print("What do you want your Real Time to be? (format: 69.420)")
    myrealtime = input("My real time is: ")
    print(myrealtime)
    print("What do you want your game time to be? (same format as Real Time)")
    mygametime = input("My game time is: ")
    print("What do you want your level to be?")
    print(mygametime)
    mylevel = input("My level name is: ")
    print(mylevel)
    print("That's all we need. Uploading now")
    upload(filelocation, myscore, myrealtime, mygametime, mylevel)
def upload(filelocation, myscore, myrealtime, mygametime, mylevel):
    url = "http://killstagram.azurewebsites.net/api/Mp4Upload"
    headers = {
        'X-UploaderFingerprint': str(random.randint(1,999999999999999999)) + "\\r\\n",
        'X-Level': mylevel + "\\r\\n",
        'X-Score': myscore + "\\r\\n",
        'X-RealTime': myrealtime + "\\r\\n",
        'X-GameTime': mygametime + "\\r\\n"
    }
    with open(filelocation, "rb") as myfile:
        thing = {filelocation: myfile}
        response = requests.post(url=url, files=thing, headers=headers)
        print(response.text)
main()