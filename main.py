import ctypes
import time
import requests
import urllib.request

    # Install Liberys for Begin
    # Request Are limited to 50 requests per hour.
    # https://api.unsplash.com/photos/?client_id=YOUR_ACCESS_KEY
    # https://unsplash.com/documentation

    
def getImage():
    accessKey = "API_KEY"                           # Login before APIKEY
    url = f'https://api.unsplash.com/photos/random/?client_id={accessKey}&orientation=landscape'
    response  = requests.get(url)                  # HTTP get Resquest
    if response.status_code == 200 :
        data = response.json()                     # Image Data as json
        randomPhoto = data['urls']['regular']      # get URL
        print("Random Photo : \n" , randomPhoto)
        return randomPhoto
    else : 
        print("ERROR Failed to Call API")
    print(response)


def downloadImage(imageURL , filepath):
    urllib.request.urlretrieve(imageURL , filepath) # DownloadImage
    print("\t --- Image Download Sucessful ---")

def loopSystem(seconds , filepath):
    cycleCount = 1;
    while True:
        imageURL = getImage()                       # call API getImage
        downloadImage(imageURL , filepath)          # download Image from url to System
        changeBackground(filepath);                 # change Background
        cycleCount = cycleCount + 1                 # cycle count
        time.sleep(seconds)                  


def changeBackground(filepath):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, filepath , 0)


filepath = "file_Directory"                     # filepath = "D:\\python\\ChangeBackground\\BackgroundImage.jpg"
seconds = 72                                    # 72 * 50 = 3600 seconds = 1 hour
loopSystem(seconds , filepath);



