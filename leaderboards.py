
def display_leaderboard(top_posts):
    print("Which Leaderboard do you want to see? (1) Likes, (2) Reblogs, (3) Replies")
    response = input("Enter the number of your choice: ")

    if response == "1":
        print("\nLikes Leaderboard:\n")
        sorted_posts = sorted(top_posts, key=lambda x: x["like_count"], reverse=True)
        for post in sorted_posts:
            print("Name:", post["blog_name"])
            print("Like count:", post["like_count"])
            print("---")

    if response == "2":
        print("\nReblogs Leaderboard:\n")
        sorted_posts = sorted(top_posts, key=lambda x: x["reblog_count"], reverse=True)
        for post in sorted_posts:
            print("Name:", post["blog_name"])
            print("Reblog count:", post["reblog_count"])
            print("---")

    if response == "3":
        print("\nReplies Leaderboard:\n")
        sorted_posts = sorted(top_posts, key=lambda x: x["reply_count"], reverse=True)
        for post in sorted_posts:
            print("Name:", post["blog_name"])
            print("Reply count:", post["reply_count"])
            print("---")
