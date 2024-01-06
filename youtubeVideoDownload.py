from pytube import YouTube
SAVE_PATH = "C:\\Users\\anvit\\Desktop\\Assistant\\downloadedVideos"

def downloadVideo():
    link = input("Please enter the link of video... ")
    try:
        yt = YouTube(link)
    except Exception as e:
        print("Connection Error... Please try again... ")
        return
    print("Title of your video is " , yt.title)
    print("Views of your video is ", yt.views)
    yd = yt.streams.get_highest_resolution()
    yd.download(SAVE_PATH)