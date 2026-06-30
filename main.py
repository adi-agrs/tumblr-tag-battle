import sys
from analyze import analyze_tag

tag1 = sys.argv[1]
tag2 = sys.argv[2]

top_posts_1, notes_1, likes_1, reblogs_1, replies_1 = analyze_tag(tag1)
top_posts_2, notes_2, likes_2, reblogs_2, replies_2 = analyze_tag(tag2)

if notes_1 > notes_2:
    print(f"\n🏆 Winner: #{tag1} with {notes_1} total notes!")
elif notes_2 > notes_1:
    print(f"\n🏆 Winner: #{tag2} with {notes_2} total notes!")
else:
    print(f"\n🤝 It's a tie! Both tags have {notes_1} notes.")

# TODO: 
# - Crown winner based on higher number of total notes between two tags (DONE)
# - Display the breakdown of each post in the leaderboard (like, reblog, reply)
# - get some way to extract the image form highest liked tag post and display it on the website
# - Implement a simple web interface to display the results