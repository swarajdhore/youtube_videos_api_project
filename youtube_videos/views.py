import requests
from youtube_videos.models import Videos
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from isodate import parse_duration

# Create your views here.
def home(request):
    url_search="https://www.googleapis.com/youtube/v3/search"
    url_video="https://www.googleapis.com/youtube/v3/videos"
    
    search_parameters= {
        'part' : 'snippet',
        'q':'football',          # this is the predefined query
        'key': settings.YOUTUBE_API_KEY,
        'type':'video',
        'order':'date',
        'publishedAfter':'2021-01-01T00:00:00Z'
    }
    videoids =[]
    r= requests.get(url_search, params=search_parameters)
    videos = r.json()['items']

    for i in videos:
        videoids.append(i['id']['videoId'])

    video_parameters= {
        'part' : 'snippet,contentDetails',
        'key': settings.YOUTUBE_API_KEY,
        'id': ','.join(videoids),
    }
    r = requests.get(url_video, params=video_parameters)
    videos = r.json()['items']

    videos_list = []
    y = Videos.objects.all().delete()
    for i in videos:
        # print(i['id'])
        # print(i['snippet']['title'])
        # print(i['snippet']['description'])
        # print(i['snippet']['publishedAt'])
        # print(i['snippet']['thumbnails']['high']['url'])
        # print(parse_duration(i['contentDetails']['duration']))
        
        video_info = {
        'id':i['id'],
        'title':i['snippet']['title'],
        'description':(i['snippet']['description']),
        'publish_date':i['snippet']['publishedAt'],
        'thumbnail':i['snippet']['thumbnails']['high']['url'],
        'duration':int(parse_duration(i['contentDetails']['duration']).total_seconds()//60),
        }
        
        x= Videos.objects.create(video_id=i['id'],duration=int(parse_duration(i['contentDetails']['duration']).total_seconds()//60),publish_date=i['snippet']['publishedAt'],thumbnail=i['snippet']['thumbnails']['high']['url'],title=i['snippet']['title'],description=i['snippet']['description'])    
        print("Inserted")
        videos_list.append(video_info)
    print(videos_list)
    dict = {
        'videos_list': videos_list
    }
    
    return render(request, 'base.html', dict)
