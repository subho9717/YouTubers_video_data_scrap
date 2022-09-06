from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup as bsp
import time
import requests
import pandas as pd
from tqdm import tqdm
from pytube import YouTube,Channel
from googleapiclient.discovery import build
import pandas as pd
from pydrive.auth import GoogleAuth
gauth = GoogleAuth()
gauth.LocalWebserverAuth() # Creates local webserver and auto handles authentication.
from pydrive.drive import GoogleDrive
import os

drive = GoogleDrive(gauth)

api_key = 'AIzaSyByQMt4VH7I4BylDHElcxxilZVFhMwWWAc'
youtube = build('youtube', 'v3', developerKey=api_key)

box = []


def video_data(url_video, final_url):
    # video link
    video_link1 = final_url

    title_data = youtube.videos().list(part='snippet,contentDetails,statistics', id=url_video).execute()
    for t in title_data['items']:
        title = t["snippet"]["title"]
        likeCount = t['statistics']['likeCount']
        commentCount = t['statistics']['commentCount']
        viewCount = t['statistics']['viewCount']
        thumbnails = t["snippet"]['thumbnails']['high']['url']
        print(thumbnails)

    data = youtube.commentThreads().list(part='snippet', videoId=url_video, maxResults='100',
                                         textFormat="plainText").execute()

    for i in data["items"]:
        name = i["snippet"]['topLevelComment']["snippet"]["authorDisplayName"]
        comment = i["snippet"]['topLevelComment']["snippet"]["textDisplay"]
        box.append([name, comment])

    while ("nextPageToken" in data):

        data = youtube.commentThreads().list(part='snippet', videoId=url_video, pageToken=data["nextPageToken"],
                                             maxResults='100', textFormat="plainText").execute()

        for i in data["items"]:
            name = i["snippet"]['topLevelComment']["snippet"]["authorDisplayName"]
            comment = i["snippet"]['topLevelComment']["snippet"]["textDisplay"]

            box.append([name, comment])

    df = pd.DataFrame(
        {'Title': title, 'likeCount': likeCount, 'commentCount': commentCount, 'Name': [i[0] for i in box],
         'Comment': [i[1] for i in box]})

    ##########################################Image
    imglink = thumbnails
    image = requests.get(imglink).content
    img_title = str(title).replace(" ", "_").replace("?", "_").replace("|", "_").replace("/", "_").replace("'\'", "_")
    # imgtitle = r"media/images/" + img_title + '.jpg'
    imgtitleg = img_title + '.jpg'
    # with open(imgtitle, "wb") as file:
    #     file.write(image)

    imagefolder = '1vKXX5hwd2K9FWH2l9gwrXebN0hKosnum'
    file5 = drive.CreateFile({
        'title':imgtitleg,
        'parents': [{'id': imagefolder}]
    })
    with open(imgtitleg, "wb") as file:
        file.write(image)
    file5.SetContentFile(imgtitleg)
    # file5.Upload()

    ######################################################
    videofolder = '1qDl8vUE3qy0yBhxTIz1ztfNQ3KDsWVB4'
    youtube_1 = YouTube(final_url)
    # # print(youtube_1.thumbnail_url)
    videos_1 = youtube_1.streams.all()
    vid = list(enumerate(videos_1))
    strm = 0
    videos_1[strm].download("media/video/")

    dir = r"./media/video"
    all_files = os.listdir(dir)

    for f in all_files:
        path = os.path.join(dir, f)
        file6 = drive.CreateFile({
            'title': f,
            'parents': [{'id': videofolder}]
        })
        file6.SetContentFile(path)
        file6.Upload()
    print('successfully')
def get_all_video_url(video_url):

    c = Channel(video_url)
    count = 0
    for r in c:
        dir = r"./media/video"
        all_files = os.listdir(dir)
        for f in all_files:
            path = os.path.join(dir, f)
            os.remove(path)

        final_url = str(r)
        url_video = str(r)[-11:]
        print(url_video, final_url,count)
        video_data(url_video, final_url)
        if count == 50:
            break
        count += 1


# get_all_video_url('https://www.youtube.com/user/krishnaik06/videos')

