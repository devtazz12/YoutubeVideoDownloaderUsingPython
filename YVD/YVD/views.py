from django.shortcuts import render
from pytube import YouTube
import os





# video =YouTube(videoUrl).streams.filter(progressive=True, file_extension='mp4').get_highest_resolution()

def home(request):
    return render(request, 'home.html')

def videoinfo(request):
    global videoUrl 
    videoUrl = request.GET.get('videoUrl')
    video=YouTube(videoUrl)
    thumbnail_url = video.thumbnail_url
    title = video.title
    return render(request, 'videoinfo.html', {'thumbnail_url':thumbnail_url, 'title':title} )


def download(request):
    global videoUrl
    homdir=os.path.expanduser('~')
    dirs = homdir + '/Downloads'
    if request.method=="POST":
        try:
           YouTube(videoUrl).streams.filter(progressive=True, file_extension="mp4").get_highest_resolution().download(dirs)
           return render(request, 'downloadSuccess.html', {'dirs':dirs})
        except Exception as e:
            print(e)
            exception = "exception occured"
            return render(request, 'failure.html',{'e':exception})
    return render(request, 'home.html')









