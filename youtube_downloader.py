import pytube
url=input("enter the url")
yt=pytube.YouTube(url)
path=input("enter the path")
yt.streams.first().download(path)

