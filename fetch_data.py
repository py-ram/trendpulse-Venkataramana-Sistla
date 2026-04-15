import requests
import time
import json
import os
from datetime import datetime

# Base API URLs
TOP_STORIES_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
ITEM_URL = "https://hacker-news.firebaseio.com/v0/item/{}.json"

# Required header (as per instructions)
headers = {"User-Agent": "TrendPulse/1.0"}

# Category keyword mapping
CATEGORY_KEYWORDS = {
    "technology": ["ai", "software", "tech", "code", "computer", "data", "cloud", "api", "gpu", "llm"],
    "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global"],
    "sports": ["nfl", "nba", "fifa", "sport", "game", "team", "player", "league", "championship"],
    "science": ["research", "study", "space", "physics", "biology", "discovery", "nasa", "genome"],
    "entertainment": ["movie", "film", "music", "netflix", "game", "book", "show", "award", "streaming"]
}

# Max stories per category
MAX_PER_CATEGORY = 25


def get_category(title):
    """
    Assign category based on keyword matching (case-insensitive).
    Returns category name or None if no match found.
    """
    title_lower = title.lower()

    for category, keywords in CATEGORY_KEYWORDS.items():
        for keyword in keywords:
            if keyword in title_lower:
                return category

    return None


def fetch_top_story_ids():
    """Fetch top 500 story IDs from Hacker News."""
    try:
        response = requests.get(TOP_STORIES_URL, headers=headers)
        response.raise_for_status()
        return response.json()[:500]
    except Exception as e:
        print(f"Error fetching top stories: {e}")
        return []


def fetch_story(story_id):
    """Fetch individual story details."""
    try:
        response = requests.get(ITEM_URL.format(story_id), headers=headers)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Failed to fetch story {story_id}: {e}")
        return None


def main():
    # Step 1: Fetch top IDs
    story_ids = fetch_top_story_ids()

    if not story_ids:
        print("No story IDs fetched. Exiting.")
        return

    collected_stories = []
    category_counts = {cat: 0 for cat in CATEGORY_KEYWORDS}

    print("Starting data collection...\n")

    # Step 2: Loop category-wise (important for sleep logic)
    for category in CATEGORY_KEYWORDS.keys():

        print(f"Collecting category: {category}")

        for story_id in story_ids:

            # Stop if category limit reached
            if category_counts[category] >= MAX_PER_CATEGORY:
                break

            story = fetch_story(story_id)

            if not story:
                continue

            title = story.get("title", "")

            # Assign category
            assigned_category = get_category(title)

            if assigned_category != category:
                continue

            # Extract required fields safely
            data = {
                "post_id": story.get("id"),
                "title": title,
                "category": assigned_category,
                "score": story.get("score", 0),
                "num_comments": story.get("descendants", 0),
                "author": story.get("by", "unknown"),
                "collected_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }

            collected_stories.append(data)
            category_counts[category] += 1

        # Sleep AFTER each category loop (IMPORTANT requirement)
        time.sleep(2)

    # Step 3: Create data folder if not exists
    os.makedirs("data", exist_ok=True)

    # Generate filename with date
    filename = f"data/trends_{datetime.now().strftime('%Y%m%d')}.json"

    # Save JSON
    with open(filename, "w") as f:
        json.dump(collected_stories, f, indent=4)

    # Final output
    print("\n--- SUMMARY ---")
    print(f"Collected {len(collected_stories)} stories.")
    print(f"Saved to {filename}")

    print("\nCategory Breakdown:")
    for cat, count in category_counts.items():
        print(f"{cat}: {count}")


if __name__ == "__main__":
    main()
