import feedparser
from html.parser import HTMLParser
from notion.client import NotionClient
from notion.block import TextBlock, SubheaderBlock, BulletedListBlock
import html2text

notiontoken = ""
notionpage = ""
client = NotionClient(token_v2=notiontoken)
page = client.get_block(notionpage)

class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
        print(data)

def rssparser(url):
    parser = MyHTMLParser()
    feed = feedparser.parse(url)
    for entry in feed.entries:
        title = entry.title
        link = entry.link
        text = html2text.html2text(entry.summary)
        write_notion(title,link,text)

def link_finder(file):
    f = open(file, "r")
    for param in f.readlines():
        rssparser(param)

def write_notion(title,link,text):
    page.children.add_new(SubheaderBlock, title=title)
    page.children.add_new(BulletedListBlock, title=link)
    page.children.add_new(TextBlock, title=text)
    page.children.add_new(TextBlock, title="")

if __name__ == "__main__":
    link_finder("links.txt")
