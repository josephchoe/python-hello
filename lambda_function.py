import os
import json
import argparse

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

DEVELOPER_KEY = os.environ['DEVELOPER_KEY']
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

def lambda_handler(event, context):
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY, cache_discovery=False)

  search_response = youtube.search().list(
    q='penguin',
    channelId='UCwez9XDNV_wS0WNDZteXjgw',
    part='id,snippet',
    maxResults=25
  ).execute()

  videos = []
  channels = []

  for search_result in search_response.get('items', []):
    if search_result['id']['kind'] == 'youtube#video':
      videos.append('%s (%s)' % (search_result['snippet']['title'],
                                 search_result['id']['videoId']))
    elif search_result['id']['kind'] == 'youtube#channel':
      channels.append('%s (%s)' % (search_result['snippet']['title'],
                                   search_result['id']['channelId']))

  print 'Videos:\n', '\n'.join(videos), '\n'
  print 'Channels:\n', '\n'.join(channels), '\n'

  return "Test"
