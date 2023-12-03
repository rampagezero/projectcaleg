# retrieving data comment based on channel id
import requests
from googleapiclient.discovery import build
import pymongo
from alive_progress import alive_bar

api_key=open('C:\\Users\\andik\\Documents\\project\\Project NLP 1\\Youtube\\API_youtube.txt').readlines()
youtube=build('youtube','v3',developerKey=api_key)
request=youtube.search().list(part='snippet',q='',maxResults=5)
channelId=request.execute()['items'][0]['snippet']['channelId']
request=youtube.search().list(part='snippet',channelId=channelId,maxResults=100,q='handphone')
data=request.execute()['items']
video_snippet={}

request=youtube.videos().list(part='snippet',id=j)
data=request.execute()
video_dict=dict()
video_dict['videoid']=j
video_dict['judul']=data['items'][0]['snippet']['title']
video_dict['time published']=data['items'][0]['snippet']['publishedAt']
batas_komen=len(youtube.commentThreads().list(part='snippet',videoId=j ,textFormat='plainText',
order='time',maxResults=50).execute()['items'])
print(batas_komen)
if batas_komen<50:
    batas_komen=batas_komen
elif batas_komen>=50:
    batas_komen=49
list_komen=[]
for i in range(0,batas_komen):
    list_komen.append(youtube.commentThreads().list(part='snippet',videoId=j ,textFormat='plainText',
            order='time',maxResults=50).execute()['items'][i]['snippet']['topLevelComment']['snippet']['textDisplay'])
video_dict['komentar']=list_komen

            

