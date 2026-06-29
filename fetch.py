import requests
import time
from config import api_key, page_length

def fetch_posts_for_tag(tag, max_posts):
    all_posts = []
    before_timestamp = None # Start at the most recent post.

    while len(all_posts) < max_posts:
        params = {"tag": tag, "api_key": api_key, "limit": page_length} 
        if before_timestamp:
            params["before"] = before_timestamp
        
        response = requests.get("https://api.tumblr.com/v2/tagged", params=params)
        data = response.json()
        posts = data["response"]

        if not posts: 
            break  # No more posts to fetch.

        all_posts.extend(posts)
        before_timestamp = posts[-1]["timestamp"]  # Update the timestamp to fetch older posts next.

        time.sleep(0.5)  # Sleep to avoid hitting rate limits.

    return all_posts