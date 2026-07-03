import os
from dotenv import load_dotenv

load_dotenv() # parses .env file and loads everything environment variables

api_key = os.getenv("TUMBLR_API_KEY")
api_secret = os.getenv("TUMBLR_API_SECRET")
access_token = os.getenv("TUMBLR_ACCESS_TOKEN")
access_secret = os.getenv("TUMBLR_ACCESS_SECRET")
fetch_limit = 20 # maximum number of posts 
page_length = 10 # page length always needs to be smaller than max_posts
leaderboard_limit = 1 # must be smaller than fetch_limit, otherwise it will return all posts