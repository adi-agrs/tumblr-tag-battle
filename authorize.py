from requests_oauthlib import OAuth1Session
from config import api_key, api_secret

# Step 1: Get a request token
oauth = OAuth1Session(api_key, client_secret=api_secret)
fetch_response = oauth.fetch_request_token("https://www.tumblr.com/oauth/request_token")

request_token = fetch_response.get("oauth_token")
request_token_secret = fetch_response.get("oauth_token_secret")

# Step 2: Direct user to Tumblr to authorize
auth_url = f"https://www.tumblr.com/oauth/authorize?oauth_token={request_token}"
print(f"\nGo to this URL and click 'Allow':\n{auth_url}\n")

# Step 3: Get the verifier code back
verifier = input("Paste the oauth_verifier from the redirect URL here: ")

# Step 4: Exchange for access token
oauth = OAuth1Session(
    api_key,
    client_secret=api_secret,
    resource_owner_key=request_token,
    resource_owner_secret=request_token_secret,
    verifier=verifier
)
access_token_response = oauth.fetch_access_token("https://www.tumblr.com/oauth/access_token")

print("\nAdd these to your .env file:")
print(f"TUMBLR_ACCESS_TOKEN={access_token_response.get('oauth_token')}")
print(f"TUMBLR_ACCESS_SECRET={access_token_response.get('oauth_token_secret')}")

# https://example.com/?oauth_token=hXIYaKSZthbpH0tQnxmpoNDB9aJvlLNjyUaGZjTXSjZ9jtmykJ&oauth_verifier=yl7zQnhwi0lH3i3KwBmOPd53ONPElO3kjy6F4PkIUCPxnzF2e6#_=_