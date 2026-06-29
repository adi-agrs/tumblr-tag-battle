import os
from dotenv import load_dotenv

load_dotenv() # parses .env file and loads everything environment variables

api_key = os.getenv("TUMBLR_API_KEY")
api_secret = os.getenv("TUMBLR_API_SECRET")
fetch_limit = 50 # maximum number of posts 
page_length = 2 # page length always needs to be smaller than max_posts
leaderboard_limit = 10 # must be smaller than fetch_limit, otherwise it will return all posts