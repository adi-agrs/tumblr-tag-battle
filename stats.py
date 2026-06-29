def rank_by_notes(posts, top_n):
    sorted_posts = sorted(posts, key=lambda x: x.get("note_count", 0), reverse=True)
    return sorted_posts[:top_n]
