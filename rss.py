import feedparser
from html.parser import HTMLParser
from notion.client import NotionClient
from notion.block import TextBlock

import html2text

client = NotionClient(token_v2="f4678525ad72d98f7c312e90e11d22d94be41a812bc1a4922b03dc14307bde3d6fce405dba23e719469c4136885dbb41b6b1aa810e2d02bffc9263dc1d2b4cbc6527b5951af2d17c2b79d493ac4d")
page = client.get_block("https://www.notion.so/DevOps-RSS-89c60de0b68f4fda91bd13a756e08a1f")

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
    page.children.add_new(TextBlock, title=title)
    page.children.add_new(TextBlock, title=link)
    page.children.add_new(TextBlock, title=text)


if __name__ == "__main__":
    link_finder("links.txt")
