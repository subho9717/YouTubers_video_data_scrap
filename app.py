from flask import Flask,render_template,request,redirect,url_for,jsonify
from pytube import YouTube
from mysql.connector import  connect
from youtube_scrap import get_all_video_url


app = Flask(__name__)

conn = connect(
    host="bj1tj4neicdlfx9e5sxi-mysql.services.clever-cloud.com",
    user="ufgi5z1fldgybbtw",
    password="uK0HGPH80WlVvS8j086W",
    database = "bj1tj4neicdlfx9e5sxi"
)
cursor = conn.cursor()


@app.route('/',methods=['POST','GET'])
def index():  # put application's code here

    cursor.execute("select * from YouTubers_Table")
    fnl_data = [r for r in cursor.fetchall()]

    print(fnl_data)
    return render_template('index.html',data = fnl_data)


@app.route('/video_url',methods=["POST","GET"])
def youtube():  # put application's code here

    videourl = request.form['videourl']

    if videourl :
        data = get_all_video_url(videourl)
        cursor.execute("select * from YouTubers_Table where Video_watch_url = '%s'"%data)
        fnl_data = [r for r in cursor.fetchall()]

        print(fnl_data)
        return redirect(url_for('/'))
        # return jsonify({data: fnl_data})
        # return render_template("index.html",data=fnl_data)

    return jsonify({'error': 'Missing data!'})


    return jsonify({'error':"Missing data!"})

if __name__ == '__main__':
    app.run(debug=True)
