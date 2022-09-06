from flask import Flask,render_template,request,redirect,url_for,jsonify
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
from youtube_scrap import get_all_video_url


app = Flask(__name__)


@app.route('/',methods=['POST','GET'])
def index():  # put application's code here
    return render_template('index.html')


@app.route('/video_url',methods=["POST","GET"])
def youtube():  # put application's code here
    youtuber_channel = YouTube('https://www.youtube.com/user/krishnaik06/videos').video_id

    videourl = request.form['videourl']
    print(videourl)
    if videourl :
        get_all_video_url(videourl)
        return render_template("youtube.html",result = videourl)

    return jsonify({'error':"Missing data!"})

if __name__ == '__main__':
    app.run(debug=True)
