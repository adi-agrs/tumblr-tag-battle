import time
from fetch import fetch_posts_for_tag
from stats import rank_by_notes
from config import fetch_limit, leaderboard_limit
from notes_breakdown import get_notes_breakdown



def analyze_tag(tag):

    total_notes_for_tag = 0
    total_likes_for_tag = 0
    total_reblogs_for_tag = 0
    total_replies_for_tag = 0

    print(f"Fetching posts for tag '{tag}'...\n")
    all_posts = fetch_posts_for_tag(tag=tag, max_posts=fetch_limit)
    print(f"Fetched {len(all_posts)} posts for tag '{tag}'.\n")

    # top_posts is the base leaderboard.

    top_posts = rank_by_notes(all_posts, top_n=leaderboard_limit)
    print(f"Top {leaderboard_limit} for {tag} posts by note count:\n")

    for post in all_posts: 
        total_notes_for_tag += post["note_count"]

    for post in top_posts:
        print("Name:", post["blog_name"])
        print("Note count:", post["note_count"])
        print("---")

    print("DONE!")

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


    print(f"\nTotal notes for tag '{tag}': {total_notes_for_tag}")
    print(f"\nTotal likes for tag '{tag}': {total_likes_for_tag}")
    print(f"Total reblogs for tag '{tag}': {total_reblogs_for_tag}")
    print(f"Total replies for tag '{tag}': {total_replies_for_tag}")

    return top_posts, total_notes_for_tag, total_likes_for_tag, total_reblogs_for_tag, total_replies_for_tag
