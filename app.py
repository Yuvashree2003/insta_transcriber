from flask import Flask, render_template, request
import os
import tempfile
import yt_dlp
import whisper
import torch

app = Flask(__name__)

device = "cuda" if torch.cuda.is_available() else "cpu"
model = whisper.load_model("base", device=device)

def download_instagram_video(insta_url):
    ydl_opts = {
        'format': 'mp4',
        'outtmpl': tempfile.gettempdir() + '/%(title)s.%(ext)s',
        'quiet': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(insta_url, download=True)
        return ydl.prepare_filename(info)  # returns the path of the downloaded file

@app.route('/', methods=['GET', 'POST'])
def index():
    transcription = None
    if request.method == 'POST':
        video_url = request.form['video_url']
        try:
            video_path = download_instagram_video(video_url)
            result = model.transcribe(video_path)
            transcription = result["text"]
        except Exception as e:
            transcription = f"❌ Error: {str(e)}"
    return render_template('index.html', transcription=transcription)

if __name__ == '__main__':
    app.run(debug=True)
