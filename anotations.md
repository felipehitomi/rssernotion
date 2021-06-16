link do rss -> http://feeds.dzone.com/devops

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
				"text": [{ "type": "text", "text": {
          "content": "What is RAID in Linux?",
          "link": { "url": "https://dzone.com/articles/what-is-raid-in-linux" } } }]
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
							"content": "RAID stands for Redundant Array of Inexpensive Disks. It is more commonly known as Redundant Array of Independent Disks. Its a pool of disks that are used to create a logical volume. Its an essential method of saving or storing the same data through several hard disks to keep our data safe. This helps in situations such as disk failures, etc. RAID is a technique of combining multiple partitions in separate disks into a single large device or virtual storage unit. These units are called RAID arrays. disk mirroring (RAID Level 1), disk striping (RAID Level 0), and parity are some examples of RAID techniques."
						}
					}
				]
			}
		}
	]
}'
