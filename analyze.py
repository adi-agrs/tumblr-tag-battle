import time
from fetch import fetch_posts_for_tag
from config import fetch_limit
from notes_breakdown import get_notes_breakdown
from bs4 import BeautifulSoup

def get_photo_url(post):
    body = post.get("body", "")

    if not body:
        return None

    soup = BeautifulSoup(body, "html.parser")
    img = soup.find("img")

    if img:
        return img.get("src")

    return None

def get_top_photo(all_posts):
    image_posts = [p for p in all_posts if get_photo_url(p)]

    if not image_posts:
        return None

    top_photo = max(image_posts, key=lambda p: p.get("note_count", 0))
    return get_photo_url(top_photo)


def analyze_tag(tag):
    total_notes_for_tag = 0

    # print(f"Fetching posts for tag '{tag}'...\n")
    all_posts = fetch_posts_for_tag(tag=tag, max_posts=fetch_limit)
    # print(f"Fetched {len(all_posts)} posts for tag '{tag}'.\n")

    if not all_posts:
        return None, 0, None

    for post in all_posts:
        total_notes_for_tag += post["note_count"]

    top_post = max(all_posts, key=lambda p: p.get("note_count", 0))

    # print(f"Top post: {top_post['blog_name']} with {top_post['note_count']} notes")

    breakdown = get_notes_breakdown(top_post["blog_name"], top_post["id"])
    top_post["like_count"] = breakdown["like"]
    top_post["reblog_count"] = breakdown["reblog"]
    top_post["reply_count"] = breakdown["reply"]

    image_url = get_top_photo(all_posts)

    # print("DONE!")

    return top_post, total_notes_for_tag, image_url