import os
from dotenv import load_dotenv
import requests
import time

load_dotenv()

api_key = os.getenv("TUMBLR_API_KEY")
api_secret = os.getenv("TUMBLR_API_SECRET")
fetch_limit = 500 


def fetch_posts_for_tag(tag, max_posts):
    all_posts = []
    before_timestamp = None # Start at the most recent post.

    while len(all_posts) < max_posts:
        params = {"tag": tag, "api_key": api_key, "limit": 20}
        if before_timestamp:
            params["before"] = before_timestamp
        
        response = requests.get("https://api.tumblr.com/v2/tagged", params=params)
        data = response.json()
        posts = data["response"]
        for post in posts:
            print("Name:", post["blog_name"])
           # print("Tags:", post["tags"])
           # print("Note count:", post["note_count"])
        
        if not posts: 
            break  # No more posts to fetch.

        all_posts.extend(posts)
        before_timestamp = posts[-1]["timestamp"]  # Update the timestamp to fetch older posts next.

        time.sleep(0.5)  # Sleep to avoid hitting rate limits.

    return all_posts

fetch_posts_for_tag(tag="lestat", max_posts=fetch_limit)


