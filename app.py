from flask import Flask, render_template, request
from analyze import analyze_tag

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/compare', methods=['POST'])
def compare():
    tag1 = request.form['tag1']
    tag2 = request.form['tag2']

    top_posts_1, notes_1 = analyze_tag(tag1)
    top_posts_2, notes_2 = analyze_tag(tag2)

    if notes_1 > notes_2:
        winner = tag1
    elif notes_2 > notes_1:
        winner = tag2
    else:
        winner = None  # tie

    return render_template(
        'results.html',
        tag1=tag1, tag2=tag2,
        notes_1=notes_1, notes_2=notes_2,
        top_posts_1=top_posts_1, top_posts_2=top_posts_2,
        winner=winner
    )

@app.route('/test-results')
def test_results():
    fake_posts_1 = [
        {"blog_name": "testblog1", "note_count": 62, "like_count": 42, "reblog_count": 18, "reply_count": 2},
        {"blog_name": "testblog2", "note_count": 45, "like_count": 30, "reblog_count": 12, "reply_count": 3},
    ]
    fake_posts_2 = [
        {"blog_name": "otherblog1", "note_count": 38, "like_count": 25, "reblog_count": 10, "reply_count": 3},
        {"blog_name": "otherblog2", "note_count": 21, "like_count": 15, "reblog_count": 5, "reply_count": 1},
    ]
    return render_template(
        'results.html',
        tag1="lestat", tag2="armand",
        notes_1=563, notes_2=334,
        top_posts_1=fake_posts_1,
        top_posts_2=fake_posts_2,
        winner="lestat"
    )


if __name__ == '__main__':
    app.run(debug=True)