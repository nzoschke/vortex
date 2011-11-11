import os
import requests
from urllib import unquote
from urlparse import urlparse

from BeautifulSoup import BeautifulSoup
from beets import Library

APP_DIR = os.path.abspath(os.path.join(__file__, ".."))

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
      path = unquote(self.url.path)
      path = path.replace("+", " ")
      path = path.replace("(", " ")
      path = path.replace(")", " ")
      _, _, self.artist, self.album, self.title, _ = path.split("/")
    else:
      print "SONG URL: %s" % self.url.geturl()
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
    lib = Library(path="%s/musiclibrary.blb" % APP_DIR, directory="%s/davroot" % APP_DIR)
    query = "%s %s %s" % (self.title, self.artist, self.album)
    paths = [i.path for i in lib.items(query=query)] + [None]
    print "SONG QUERY: %s" % query
    print "SONG PATH:  %s" % paths[0]
    return paths[0]

  def __str__(self):
    return u"%s/%s/%s" % (self.artist, self.album, self.title)
