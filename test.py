import requests
import unittest
from urlparse import urlparse

from BeautifulSoup import BeautifulSoup

from xml.dom.minidom import parseString


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

  def __str__(self):
    return u"%s/%s/%s" % (self.artist, self.album, self.title)


class TestResolver(unittest.TestCase):
  def setUp(self):
    self.urls = [
      'http://open.spotify.com/track/74rvo4QWd2LXGRvm7S07kq',
      'http://open.spotify.com/local/Desire/Drive/Under+Your+Spell/232',
      'http://open.spotify.com/local/College/Drive/A+Real+Hero+%28feat.+Electric+Youth%29/267',
      'http://open.spotify.com/local/Riz+Ortolani/Drive/Oh+My+Love+%28feat.+Katyna+Ranieri%29/170',
      'http://open.spotify.com/local/The+Chromatics/Drive/Tick+of+the+Clock/288',
      'http://open.spotify.com/track/27sDtZi0wxPDx8aAexaDee',
      'http://open.spotify.com/track/5G9Gp5O4hJqhjYn9Xn1yR2',
      'http://open.spotify.com/track/20c8ZyUsL0ClkKfHUUkmRR',
      'http://open.spotify.com/track/0txx5RrywpIhxc9yhYVk4S',
      'http://open.spotify.com/track/2HJTLaDO9zXJMDwQfpM5ja',
      'http://open.spotify.com/track/0B9IToH5Mpq8cd3khYAxbv',
      'http://open.spotify.com/track/2aZfOMtXXL5eUl07IMi0sJ',
      'http://open.spotify.com/track/3JBHmmP7W6lDgtyghETSlZ',
      'http://open.spotify.com/track/3puQED4FAQNG3hi3gWLaVr',
      'http://open.spotify.com/track/7FwWbNJ0GjLyZdTNcJ8Uzb',
      'http://open.spotify.com/track/4ElpOvjyhXcchQpv0LNL2U',
      'http://open.spotify.com/track/7xZPyGkmjHFQbLyuzPx7um',
      'http://open.spotify.com/track/1Lg0qnM3NQeSVCyIDs0RKG',
      'http://open.spotify.com/track/72wBv8yFC7CrSEJ6WxTklQ'
    ]

  def test_track_url(self):
    u = SpotifyLink(self.urls[0])
    self.assertEqual("Kavinsky/Drive/Nightcall", str(u))

  def test_local_url(self):
    u = SpotifyLink(self.urls[1])
    self.assertEqual("Desire/Drive/Under Your Spell", str(u))

if __name__ == '__main__':
  unittest.main()