from pip import main
from pytube import YouTube


# # url = input("Enter the url of video: ")
# # https://youtu.be/Doo1T5WabEU
# url = "https://youtu.be/Doo1T5WabEU"

# yt = YouTube(url)


# # Youtube video title 
# title = yt.title 

# # for thumbnail 
# thumbnail = yt.thumbnail_url

# print(yt.streams.second())
# # resolution = yt.streams.get_by_itag(18)

# # resolution.download()

def youtube(url, resolution):
    yt = YouTube(url)
    yt.streams.get_by_resolution(res=resolution).download()
    print("successful")


if __name__ == '__main__':
    video_url = input("Enter the url of video: ")
    res = input("Enter the resolution: ")
    youtube(video_url, res)
