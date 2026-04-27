import yt_dlp
from moviepy import VideoFileClip
import os

url = input("Enter the YouTube video URL:\n")

ydl_opts = {
    'format': 'mp4',
    'outtmpl': 'downloaded_video.mp4',
    'cookiesfrombrowser': ('chrome',),  # change to 'firefox' or 'edge' if needed
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

videoclip = VideoFileClip("downloaded_video.mp4")
audioclip = videoclip.audio
audioclip.write_audiofile("audio.mp3")

videoclip.close()
os.remove("downloaded_video.mp4")

print("Done! Audio saved as audio.mp3")