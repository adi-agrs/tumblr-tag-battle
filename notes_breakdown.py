import time 
import requests
from requests_oauthlib import OAuth1
from config import api_key, api_secret, access_token, access_secret

def get_notes_breakdown(blog_id, post_id):
    auth = OAuth1(api_key, api_secret, access_token, access_secret)
    response = requests.get(f"https://api.tumblr.com/v2/blog/{blog_id}/notes", params={"id": post_id}, auth=auth)
    data = response.json() 

    response_data = data.get("response", {})

    # Handle case where blog is private (returns [] instead of {})
    if not isinstance(response_data, dict):
        return {"like": 0, "reblog": 0, "reply": 0}

    notes = response_data.get("notes", []) or []

    if not notes:
        return {"like" : 0, "reblog" : 0, "reply" : 0}  # No post found with the given ID.

    
    notes = response_data.get("notes", []) or []
    breakdown = {"like": 0, "reblog": 0, "reply": 0}

    for note in notes:
        note_type = note.get("type")
        if note_type in breakdown:
            breakdown[note_type] += 1

    return breakdown