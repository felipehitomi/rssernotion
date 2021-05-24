import feedparser

feed = feedparser.parse("http://feeds.dzone.com/devops")
entry = feed.entries[0]

print("Title: ",entry.title)
