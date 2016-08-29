import sys
from event_feed import Event, EventFeed
from slackclient import SlackClient


#Requires settings.txt file to work, formatted as such:
""" 
SLACK_TOKEN = "xoxp-24282660422-24283165281-27325068118-7e0029c775"
SLACK_CHANNEL = "#comp-feed"
SLACK_USERNAME = "CompBot"
"""

def settings_helper():
	try:
		settings_file = open("settings.txt", "r")
	except IOError:
		print '"settings.txt" not found'
		sys.exit()
	token = None
	channel = None
	username = None
	for line in settings_file:
		line = line.replace(" ", "").split("=")
		if line[0] == "SLACK_TOKEN":
			token = line[1]
		elif line[0] == "SLACK_CHANNEL":
			channel = line[1]
		elif line[0] == "SLACK_USERNAME":
			username = line[1]
	if not token or not channel or not username:
		print 'Improperly formatted "settings.txt"'
		sys.exit()


class SlackBot(object):

	def __init__(self, token, username, channel):
		self.SLACK_TOKEN = token
		self.SLACK_USERNAME = username
		self.SLACK_CHANNEL = channel

		self.client = SlackClient(self.SLACK_TOKEN)
		self.event_feed = EventFeed()

	def update(self):
		events = self._get_events()
		events.sort(key=lambda event: (event.week, int(event.event_type != "Regional"), \
			event.event_type, event.end_date, event.name))
		self._post_message("\nUPDATE:\n")
		for event in events:
			self._post_event(event)

	def _get_events(self):
		return self.event_feed.get_events()

	def _post_event(self, event_obj):
		self._post_message(event_obj.get_description())

	def _post_message(self, text):
		self.client.api_call(
		    "chat.postMessage", channel=self.SLACK_CHANNEL, text=text,
		    username=self.SLACK_USERNAME, icon_emoji=':robot_face:'
		)

if __name__ == "__main__":
	SlackBot(SLACK_TOKEN, SLACK_USERNAME, SLACK_CHANNEL).update()