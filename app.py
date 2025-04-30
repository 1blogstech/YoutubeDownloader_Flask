from flask import Flask, render_template, redirect, request, flash, url_for
from YoutubeDownload_Code import *

app = Flask(__name__)
app.secret_key = "abc1234@2232ddfjdfsdksd"

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/download", methods=['GET'])
def download():
        url = request.args.get("videoUrl",None)
        type = request.args.get("downloadType",None)

        if url is None:
            flash("Mention url for download.","error")
            return redirect(url_for("main"))
        if type is None:
            flash("Please select audio type.","error")
            return redirect(url_for("main"))

        if type.lower() == "video":
            downloader = video_downloader(url)

            if "invalidUrl" == downloader:
                flash("The Url is Invalid.","error")
                return redirect(url_for("main"))

            stream_url = downloader[0]
            info = downloader[1]

            video_data = {
                "title": info.get("title"),
                "thumbnail": info.get("thumbnail"),
                "channel": info.get("channel"),
                "uploader": info.get("uploader"),
                "channel_id": info.get("channel_id"),
                "view_count": info.get("view_count"),
                "like_count": info.get("like_count"),
                "duration": info.get("duration"),  # in seconds
                "upload_date": info.get("upload_date"),
                "description": info.get("description"),
                "webpage_url": info.get("webpage_url"),
            }
        elif type.lower() == "audio":
            audio_downloader = get_audio_url(url)

            if audio_downloader == None:
                flash("Audio is not Available or Invalid url","error")
                return redirect(url_for("main"))

            info = audio_downloader[1]
            stream_url = audio_downloader[0]

            video_data = {
                "title": info.get("title"),
                "thumbnail": info.get("thumbnail"),
                "channel": info.get("channel"),
                "uploader": info.get("uploader"),
                "channel_id": info.get("channel_id"),
                "view_count": info.get("view_count"),
                "like_count": info.get("like_count"),
                "duration": info.get("duration"),  # in seconds
                "upload_date": info.get("upload_date"),
                "description": info.get("description"),
                "webpage_url": info.get("webpage_url"),
            }

        return render_template("download_video.html",url=stream_url,info=video_data, requested=type)
