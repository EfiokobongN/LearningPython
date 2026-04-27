import youtube_dl

url = input("enter the youtube video url:\n")

with youtube_dl.YoutubeDL() as ydl:
    ydl.download([url])