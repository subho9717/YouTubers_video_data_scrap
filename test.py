
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup as bsp
import time
import requests
import pandas as pd
from tqdm import tqdm
from pytube import YouTube
from googleapiclient.discovery import build
import pandas as pd

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

    #

    imglink = thumbnails
    image = requests.get(imglink).content
    img_title = str(title).replace(" ","_").replace("?","_").replace("|","_")
    imgtitle = r"media/images/" +img_title+'.jpg'
    with open(imgtitle, "wb") as file:
        file.write(image)
    youtube_1 = YouTube(final_url)
# # print(youtube_1.thumbnail_url)
    videos_1 = youtube_1.streams.all()
    vid = list(enumerate(videos_1))
    strm = 0
    videos_1[strm].download("media/images/")
    print('successfully')
def get_all_video_url(video_url):
    # option = webdriver.FirefoxOptions()
    # option.add_argument("--headless")
    # driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(),options=option)
    opt = Options()
    opt.add_argument("--headless")
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
    url = video_url
    print(url)
    driver.get(url)
    driver.execute_script("window.scrollBy(0,10000)", "")
    time.sleep(5)
    soup = bsp(driver.page_source, 'html.parser')
    driver.quit()
    video_list = soup.find_all('ytd-grid-video-renderer')
    # all_url = []
    for r in tqdm(range(50)):
        url_video = str(video_list[r].div.a['href'])[-11:]
        final_url_video = str(video_list[r].div.a['href'])
        final_url = "https://www.youtube.com" + final_url_video  #
        # print(url_video,final_url)
        video_data(url_video, final_url)



