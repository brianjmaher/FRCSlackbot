from bs4 import BeautifulSoup
from event import Event,url
import string, urllib

class EventFeed(object):

	def __init__(self):
		self.url = url

	def get_events(self):
		soup = BeautifulSoup(urllib.urlopen(url), "html.parser")
		table = soup.find("table")
		return [ Event(tr) for tr in table.find_all("tr")[5:-2] ]

if __name__ == "__main__":
	for event in EventFeed().get_events():
		print str(event)
	#for event in EventFeed().get_events():
	#	pass
		#print event.__dict__