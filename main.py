import sys
from analyze import analyze_tag

tag1 = sys.argv[1]
tag2 = sys.argv[2]

top_posts_1, notes_1 = analyze_tag(tag1)
top_posts_2, notes_2 = analyze_tag(tag2)