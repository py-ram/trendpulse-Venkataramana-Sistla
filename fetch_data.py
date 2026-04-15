import requests
import json

def fetch_top_stories(limit=20):
    url = "https://hacker-news.firebaseio.com/v0/topstories.json"
    story_ids = requests.get(url).json()

    stories = []
    for i in story_ids[:limit]:
        story_url = f"https://hacker-news.firebaseio.com/v0/item/{i}.json"
        story = requests.get(story_url).json()
        stories.append(story)

    with open("data/hn_data.json", "w") as f:
        json.dump(stories, f, indent=4)

    return stories
