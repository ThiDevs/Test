#!/usr/bin/python

import apiclient as b
import apiclient as a
from oauth2client.tools import argparser

DEVELOPER_KEY = "AIzaSyDGRbEc7qbGJ59Vsv68fL0aHml1FYpX_1g"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def youtube_search(options):
  youtube = b.discovery.build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

  search_response = youtube.search().list(
    q=options.q,
    part="id,snippet",
    maxResults=options.max_results
  ).execute()

  videos = []
  channels = []
  playlists = []

  for search_result in search_response.get("items", []):
    if search_result["id"]["kind"] == "youtube#video":
      videos.append("%s (%s)" % (search_result["snippet"]["title"],
                                 search_result["id"]["videoId"]))
    elif search_result["id"]["kind"] == "youtube#channel":
      channels.append("%s (%s)" % (search_result["snippet"]["title"],
                                   search_result["id"]["channelId"]))
    elif search_result["id"]["kind"] == "youtube#playlist":
      playlists.append("%s (%s)" % (search_result["snippet"]["title"],
                                    search_result["id"]["playlistId"]))

  print ("Videos:\n", "\n".join(videos), "\n")
  #print ("Channels:\n", "\n".join(channels), "\n")
  #print ("Playlists:\n", "\n".join(playlists), "\n")


if __name__ == "__main__":
  argparser.add_argument("--q", help="Search term", default="Instumental Rap Lord")
  argparser.add_argument("--max-results", help="Max results", default=5)
  args = argparser.parse_args()

  try:
    youtube_search(args)
  except a.errors.HttpError as e:
      print ("An HTTP error %d occurred:\n%s" % (e.resp.status, e.content))