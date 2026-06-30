import os
import time
from fetch import fetch_posts_for_tag
from stats import rank_by_notes
from config import fetch_limit, leaderboard_limit
from notes_breakdown import get_notes_breakdown

total_likes_for_tag = 0
total_reblogs_for_tag = 0
total_replies_for_tag = 0

print("Fetching posts for tag 'lestat'...\n")
all_posts = fetch_posts_for_tag(tag="lestat", max_posts=fetch_limit)
print(f"Fetched {len(all_posts)} posts for tag 'lestat'.\n")

# top_posts is the base leaderboard.

top_posts = rank_by_notes(all_posts, top_n=leaderboard_limit)

print(f"Top {leaderboard_limit} posts by note count:\n")

for post in top_posts:
    print("Name:", post["blog_name"])
    print("Note count:", post["note_count"])
    print("---")

print("\nDone.")

# Filling up each leaderboard post's dictionary with the breakdown of notes (like, reblog, reply)

for post in top_posts:
    breakdown = get_notes_breakdown(post["blog_name"], post["id"])
    post["like_count"] = breakdown["like"]
    total_likes_for_tag += breakdown["like"]
    post["reblog_count"] = breakdown["reblog"]
    total_reblogs_for_tag += breakdown["reblog"]
    post["reply_count"] = breakdown["reply"]
    total_replies_for_tag += breakdown["reply"]

    time.sleep(0.5)  # Sleep to avoid hitting rate limits.

print(f"\nTotal likes for tag 'lestat': {total_likes_for_tag}")
print(f"Total reblogs for tag 'lestat': {total_reblogs_for_tag}")
print(f"Total replies for tag 'lestat': {total_replies_for_tag}")

# TODO: 
# - Crown winner based on higher number of total notes between two tags 
# - Display the breakdown of each post in the leaderboard (like, reblog, reply)
# - get some way to extract the image form highest liked tag post and display it on the website
# - Implement a simple web interface to display the results