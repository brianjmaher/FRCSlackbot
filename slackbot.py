import sys
from event import Event
from event_feed import EventFeed
from slackclient import SlackClient
import settings as st

# Requires settings.py file, formatted as such:
""" 
SLACK_TOKEN = "your_slack_api_token"
SLACK_CHANNEL = "#channel_name"
SLACK_USERNAME = "YourBotName"
"""


class SlackBot(object):

	def __init__(self, token, username, channel):
		self.SLACK_TOKEN = token
		self.SLACK_USERNAME = username
		self.SLACK_CHANNEL = channel

		self.client = SlackClient(self.SLACK_TOKEN)
		self.event_feed = EventFeed()

	def update(self):
		events = self._get_events()
		new_events = self._filter_new_events(events)
		new_events.sort(key=lambda event: (event.week, int(not event.is_regional), \
			event.event_type, event.end_date, event.name))
		for event in new_events:
			self._post_event(event)

	def _get_events(self):
		return self.event_feed.get_events()

	def _post_event(self, event_obj):
		message = "*NEW*: %s" % str(event_obj)
		self._post_message(message)
		print message

	def _post_message(self, text):
		self.client.api_call(
		    "chat.postMessage", channel=self.SLACK_CHANNEL, text=text,
		    username=self.SLACK_USERNAME, icon_emoji=':robot_face:'
		)

	def _filter_new_events(self, events):
		new_events = []
		event_archive = self._get_event_archive()
		for event in events:
			if event.name not in event_archive:
				new_events.append(event)
				self._archive_event(event)
		return new_events

	def _get_event_archive(self):	
		return [line.strip() for line in open(st.EVENT_ARCHIVE, "r")]

	def _archive_event(self, event):
		f = open(st.EVENT_ARCHIVE, "a")
		f.write(event.name + "\n")
		f.close()

if __name__ == "__main__":
	SlackBot(st.SLACK_TOKEN, st.SLACK_USERNAME, st.SLACK_CHANNEL).update()