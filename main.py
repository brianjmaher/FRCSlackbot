import datetime, sys, time
import settings as st
from slackbot import SlackBot

def next_scrape():
	return "Next scrape at %s\n" % (datetime.datetime.now() + \
		datetime.timedelta(seconds = st.LOOP_CYCLE))


def main():
	bot = SlackBot(st.SLACK_TOKEN, st.SLACK_USERNAME, st.SLACK_CHANNEL)
	while True:
		try:
			print "Scraping (%s)" % datetime.datetime.now()
			bot.update()
			print next_scrape()
			time.sleep(st.LOOP_CYCLE)
		except KeyboardInterrupt:
			print "Exiting."
			sys.exit(0)

if __name__ == "__main__":
	main()