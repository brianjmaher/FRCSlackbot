url = 'https://my.usfirst.org/myarea/index.lasso?event_type=FRC&year=2017'

months = {
			"Feb": 2,
			"Mar": 3,
			"Apr": 4,
}

event_weeks =  [
				"2017-03-05",
				"2017-03-12",
				"2017-03-19",
				"2017-03-26",
				"2017-04-02",
				"2017-04-09",
				"2017-04-16",
				"2017-04-23",
				"2017-04-30",
			   ]

def convert_date_range(date_string): 
	split_range = date_string.replace(" ","").split("-")
	start_date = "%s-%02d-%02d" % (split_range[4], months[split_range[1]], int(split_range[0]))
	end_date = "%s-%02d-%02d" % (split_range[4], months[split_range[3]], int(split_range[2]))
	return start_date, end_date

def remove_special(string):
	return string.replace( u"\xa0", u"," )

class Event(object):

	def __init__(self, tr):
		tds = tr.find_all("td")
		if len(tds[0]) == 1:
			self.event_type = tds[0].string.strip()
		else:
			self.event_type = remove_special( "%s %s" % ( tds[0].find("em").string, \
				tds[0].contents[3].strip()) )
		if "Championship" in self.event_type:
			if self.event_type == "Championship":	
				self.name = "FIRST %s" % tds[1].contents[1].contents[1]
			else:
				contents = tr.find("a").contents
				if len(contents) == 1:
					self.name = tr.find("a").contents[0]
				else:
					self.name = "%s %s" % (tr.find("a").find("em").string, \
						tr.find("a").contents[1])
		else:
			self.name = tds[1].find("a").string
		self.name = self.name.strip()
		self.venue = tds[2].string
		self.location = remove_special(tds[3].string)
		self.start_date, self.end_date = convert_date_range(tds[4].string)
		for i, end_date in enumerate(event_weeks):
			if end_date >= self.end_date:
				self.week = i+1
				break
		self.is_regional = (self.event_type == "Regional")

	def __str__(self):
		return "*Week %d %s:* %s, _%s to %s_" % (self.week, self.event_type, self.name, \
			self.start_date, self.end_date)