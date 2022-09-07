from flask import Flask,render_template,request,redirect,url_for,jsonify
from pytube import YouTube

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
        context = {
            'videourl':videourl
        }
        return jsonify({'videourl':videourl})
    return jsonify({'error': 'Missing data!'})
        # return render_template("youtube.html",result = videourl)

    return jsonify({'error':"Missing data!"})

if __name__ == '__main__':
    app.run(debug=True)
