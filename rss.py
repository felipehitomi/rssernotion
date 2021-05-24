import feedparser

feed = feedparser.parse("http://feeds.dzone.com/devops")
entry = feed.entries[0]

print("Title: ",entry.title)



curl 'https://api.notion.com/v1/pages/89c60de0b68f4fda91bd13a756e08a1f' -H 'Notion-Version: 2021-05-13' -H 'Authorization: Bearer '"$NOTION_API_KEY"''
curl 'https://api.notion.com/v1/blocks/89c60de0b68f4fda91bd13a756e08a1f/children?page_size=100' -H 'Authorization: Bearer '"$NOTION_API_KEY"'' -H "Notion-Version: 2021-05-13"
curl -X PATCH 'https://api.notion.com/v1/blocks/89c60de0b68f4fda91bd13a756e08a1f/children' \
  -H 'Authorization: Bearer '"$NOTION_API_KEY"'' \
  -H "Content-Type: application/json" \
  -H "Notion-Version: 2021-05-13" \
  --data '{
	"children": [
		{
			"object": "block",
			"type": "heading_2",
			"heading_2": {
				"text": [{ "type": "text", "text": { "content": "Lacinato kale" } }]
			}
		},
		{
			"object": "block",
			"type": "paragraph",
			"paragraph": {
				"text": [
					{
						"type": "text",
						"text": {
							"content": "Lacinato kale is a variety of kale with a long tradition in Italian cuisine, especially that of Tuscany. It is also known as Tuscan kale, Italian kale, dinosaur kale, kale, flat back kale, palm tree kale, or black Tuscan palm.",
							"link": { "url": "https://en.wikipedia.org/wiki/Lacinato_kale" }
						}
					}
				]
			}
		}
	]
}'
