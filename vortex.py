import os
import requests
from urlparse import urlparse

from BeautifulSoup import BeautifulSoup
from beets import Library

APP_DIR = os.path.abspath(os.path.join(__file__, ".."))
LIB = Library(path="%s/musiclibrary.blb" % APP_DIR, directory="%s/davroot" % APP_DIR)

class SpotifyLink(object):
  title       = None
  artist      = None
  album       = None
  albumartist = None 
  track       = 0
  duration    = 0

  def __init__(self, url):
    self.url = urlparse(url)
    if self.url.path.startswith("/local"):
      path = self.url.path.replace("+", " ")
      _, _, self.artist, self.album, self.title, _ = path.split("/")
    else:
      song = BeautifulSoup(requests.get(self.url.geturl()).content)
      self.title    = song.find("meta", property="og:title")["content"]
      self.track    = int(song.find("meta", property="music:album:track")["content"])
      self.duration = int(song.find("meta", property="music:duration")["content"])

      # query for album
      album_url = song.find("meta", property="music:album")["content"]
      album = BeautifulSoup(requests.get(album_url).content)
      self.album = album.find("meta", property="og:title")["content"]

      # query for album artist
      artist_url = song.find("meta", property="music:musician")["content"]
      artist = BeautifulSoup(requests.get(artist_url).content)
      self.artist = artist.find("meta", property="og:title")["content"]

  def path(self):
    query = "title:%s artist:%s album:%s" % (self.title, self.artist, self.album)
    paths = [i.path for i in LIB.items(query=query)]
    return paths[0]

  def __str__(self):
    return u"%s/%s/%s" % (self.artist, self.album, self.title)
