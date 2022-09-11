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
import threading

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



def get_all_video_url():

    try:
        
        videofolder = '1qDl8vUE3qy0yBhxTIz1ztfNQ3KDsWVB4'
        folder = "\'" + videofolder + "\'" + " in parents and trashed=false" 
        file_list = drive.ListFile({'q': folder}).GetList()
        for file1 in file_list:
            print('title: %s, id: %s' % (file1['title'], file1['id']))
            file = drive.CreateFile({'id':file1['id']})
            file.Delete()
            
            # file1['id'].Delete()
            

            
    except Exception as e:
        pass
        print(e)
    conn.close()

get_all_video_url()