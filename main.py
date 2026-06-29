import os
from fetch import fetch_posts_for_tag
from stats import rank_by_notes
from config import fetch_limit, leaderboard_limit

print("Fetching posts for tag 'lestat'...\n")
all_posts = fetch_posts_for_tag(tag="lestat", max_posts=fetch_limit)
print(f"Fetched {len(all_posts)} posts for tag 'lestat'.\n")

top_posts = rank_by_notes(all_posts, top_n=leaderboard_limit)

print(f"Top {leaderboard_limit} posts by note count:\n")

for post in top_posts:
    print("Name:", post["blog_name"])
    print("Note count:", post["note_count"])
    print("---")

print("\nDone.")


