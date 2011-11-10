import unittest
from vortex import SpotifyLink, APP_DIR

class TestSpotifyLink(unittest.TestCase):
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

  def test_path(self):
    u = SpotifyLink(self.urls[1])
    self.assertEqual("%s/davroot/music/Drive/02. Desire - Under Your Spell.mp3" % APP_DIR, u.path())

if __name__ == '__main__':
  unittest.main()