from flask import Flask,render_template,request,redirect,url_for,jsonify
from pytube import YouTube
from mysql.connector import  connect
from youtube_scrap import get_all_video_url
import pymongo

app = Flask(__name__)

conn = connect(
    host="bj1tj4neicdlfx9e5sxi-mysql.services.clever-cloud.com",
    user="ufgi5z1fldgybbtw",
    password="uK0HGPH80WlVvS8j086W",
    database = "bj1tj4neicdlfx9e5sxi"
)
cursor = conn.cursor()

client = pymongo.MongoClient("mongodb+srv://subho9717:subho9717@ineuron.8npdrfs.mongodb.net/?retryWrites=true&w=majority")


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
        cursor.execute("truncate YouTubers_Table")
        conn.commit()
        data = get_all_video_url(videourl)
        cursor.execute("select * from YouTubers_Table where Video_watch_url = '%s'"%data)
        fnl_data = [r for r in cursor.fetchall()]

        print(fnl_data)
        return redirect(url_for('index',data=fnl_data))
        # # return jsonify({data: fnl_data})
        return render_template("index.html",data=fnl_data)

    return render_template("index.html",data=fnl_data)

@app.route('/video_comment',methods=["POST","GET"])
def comment():  # put application's code here
    comm = request.form['comment']
    print(comm)
    if comm:
        db = client['YouTube_Video_Data']
        coll = db['YouTubers_table']
        data = coll.find({"Video_watch_url":comm})
        fnldata = []
        for r in data:
            fnldata.append([r['Commenter_Name'],r['Comment']])
        print(fnldata)


   
        return render_template("index.html",cdata=fnldata)

        
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
