import os
from dotenv import load_dotenv
import requests

load_dotenv()

api_key = os.getenv("TUMBLR_API_KEY")
api_secret = os.getenv("TUMBLR_API_SECRET")

response = requests.get("https://api.tumblr.com/v2/tagged", params={"tag": "harrypotter", "api_key": api_key, "limit": 5})

print("Status code:", response.status_code)

data = response.json()
posts = data["response"]

for post in posts: 
    print("Name:", post["blog_name"])
    print("Summary:", post["summary"])
    print("Tags:", post["tags"])
    print("Note count:", post["note_count"])