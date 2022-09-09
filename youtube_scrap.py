import requests
from pytube import YouTube,Channel
from googleapiclient.discovery import build
from pydrive.auth import GoogleAuth
gauth = GoogleAuth()
gauth.LocalWebserverAuth() # Creates local webserver and auto handles authentication.
from pydrive.drive import GoogleDrive
import os
from mysql.connector import  connect
import base64
import pymongo

drive = GoogleDrive(gauth)

api_key = 'AIzaSyByQMt4VH7I4BylDHElcxxilZVFhMwWWAc'
youtube = build('youtube', 'v3', developerKey=api_key)

box = []

conn = connect(
    host="youtube-data.cgje4yzuebxp.us-east-1.rds.amazonaws.com",
    user="admin",
    password="subho987",
    database = "sys"
)
cursor = conn.cursor()

client = pymongo.MongoClient("mongodb+srv://subho9717:subho9717@ineuron.8npdrfs.mongodb.net/?retryWrites=true&w=majority")


def video_data(url_video, final_url):
    # video link
    print(url_video,final_url)
    video_link1 = final_url
    video_author = YouTube(final_url).author

    mqldata1 =[]
    title_data = youtube.videos().list(part='snippet,contentDetails,statistics', id=url_video).execute()
    for t in title_data['items']:
        title = t["snippet"]["title"]
        title = str(title).replace("?", "_").replace("|", "_").replace("/", "_").replace("'\'", "_").replace("~", "_").replace("`", "_").replace("!", "_").replace("@", "_").replace("#", "_").replace("$", "_").replace("%", "_").replace("^", "_").replace("&", "_").replace("*", "_").replace("(", "_").replace(")", "_").replace("-", "_").replace("+", "_").replace("=", "_").replace(":", "_").replace(";", "_").replace('"""', "_").replace("'", "_").replace(",", "_").replace("<", "_").replace(">", "_")
        likeCount = t['statistics']['likeCount']
        commentCount = t['statistics']['commentCount']
        thumbnails = t["snippet"]['thumbnails']['high']['url']
        mqldata1.append([title,likeCount,commentCount,thumbnails])
        # print(thumbnails)

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

    # df = pd.DataFrame(
    #     {'Author': video_author,   'Commenter_Name': [i[0] for i in box],
    #      'Comment': [i[1] for i in box]})

    ##########################################Image
    imglink = thumbnails
    image = requests.get(imglink).content
    img_title = str(title).replace("?", "_").replace("|", "_").replace("/", "_").replace("'\'", "_").replace("~", "_").replace("`", "_").replace("!", "_").replace("@", "_").replace("#", "_").replace("$", "_").replace("%", "_").replace("^", "_").replace("&", "_").replace("*", "_").replace("(", "_").replace(")", "_").replace("-", "_").replace("+", "_").replace("=", "_").replace(":", "_").replace(";", "_").replace('"""', "_").replace("'", "_").replace(",", "_").replace("<", "_").replace(">", "_")
    # imgtitle = r"media/images/" + img_title + '.jpg'
    imgtitleg ='media/images/'+ img_title + '.jpg'
    # with open(imgtitle, "wb") as file:
    #     file.write(image)

    # imagefolder = '1vKXX5hwd2K9FWH2l9gwrXebN0hKosnum'
    # file5 = drive.CreateFile({
    #     'title':url_video+'.jpg',
    #     'parents': [{'id': imagefolder}]
    # })
    with open(imgtitleg, "wb") as file:
        file.write(image)

    dir = r"media/images"
    all_files = os.listdir(dir)
    for f in all_files:
        path = os.path.join(dir, f)
        with open(path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
            # print(encoded_string)
            for i in box:
                for j in mqldata1:
                    data = {'Author': video_author,
                            'title':j[0].replace(" ", "_").replace("?", "_").replace("|", "_").replace("/", "_").replace("'\'", "_").replace("~", "_").replace("`", "_").replace("!", "_").replace("@", "_").replace("#", "_").replace("$", "_").replace("%", "_").replace("^", "_").replace("&", "_").replace("*", "_").replace("(", "_").replace(")", "_").replace("-", "_").replace("+", "_").replace("=", "_").replace(":", "_").replace(";", "_").replace('"""', "_").replace("'", "_").replace(",", "_").replace("<", "_").replace(">", "_"),
                            'Commenter_Name': i[0],
                            'Comment': i[1],
                            'thumbnail':encoded_string,
                            'Video_watch_url': url_video
                            }
                    db = client['YouTube_Video_Data']
                    coll = db['YouTubers_table']
                    coll.insert_one(data)


    # file5.SetContentFile(imgtitleg)
    # file5.Upload()

    ######################################################
    videofolder = '1qDl8vUE3qy0yBhxTIz1ztfNQ3KDsWVB4'
    youtube_1 = YouTube(final_url)
    # # print(youtube_1.thumbnail_url)
    # videos_1 = youtube_1.streams.filter(file_extension='mp4')
    videos_1 = youtube_1.streams.all()
    # print(videos_1)
    vid = list(enumerate(videos_1))
    strm = 0
    videos_1[strm].download("media/video/")

    dir = r"media/video"
    all_files = os.listdir(dir)

    for f in all_files:
        path = os.path.join(dir, f)
        vfname = str(f).replace(" ", "_").replace("?", "_").replace("|", "_").replace("/", "_").replace("'\'", "_").replace("~", "_").replace("`", "_").replace("!", "_").replace("@", "_").replace("#", "_").replace("$", "_").replace("%", "_").replace("^", "_").replace("&", "_").replace("*", "_").replace("(", "_").replace(")", "_").replace("-", "_").replace("+", "_").replace("=", "_").replace(":", "_").replace(";", "_").replace('"""', "_").replace("'", "_").replace(",", "_").replace("<", "_").replace(">", "_")
        # print(vfname)
        file6 = drive.CreateFile({
            'title':vfname,
            # 'title': url_video+'.'+str(vfname).split('.')[1],
            'parents': [{'id': videofolder}]
        })
        # file6.SetContentFile(path)
        # file6.Upload()

    print('successfully')
    for i in mqldata1:
        
        sqlq1 = "INSERT INTO YouTubers_Table(YouTubers_Name ,Video_Link ,Video_Likes , Number_Of_Comments ,Title_Of_Video ,Thumbnail_Of_Video_Link,Video_watch_url) values (%s,%s,%s,%s,%s,%s,%s)"
        val = (video_author, video_link1, i[1], i[2], i[0], imglink, url_video)

        cursor.execute(sqlq1, val)
        conn.commit()
    # return url_video

def get_all_video_url(video_url):

    try:
        print(video_url)
        
        print('ok')

        db = client['YouTube_Video_Data']
        col = db['YouTubers_table']
        col.drop()

        c = Channel(video_url)
        count = 0
        for r in c:
            print(r)
            dir = r"./media/images"
            all_files = os.listdir(dir)
            for f in all_files:
                path = os.path.join(dir, f)
                os.remove(path)

            dir = r"./media/video"
            all_files = os.listdir(dir)
            for f in all_files:
                path = os.path.join(dir, f)
                os.remove(path)

            final_url = str(r)
            url_video = str(r)[-11:]
            print(url_video, final_url,count)
            data = video_data(url_video, final_url)

            if count == 5:
                break

            count += 1

            print('completed')
            # return data
    except Exception as e:
        pass
        print(e)
    conn.close()

# get_all_video_url('https://www.youtube.com/c/HiteshChoudharydotcom/videos')