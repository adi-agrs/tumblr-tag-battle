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

    top_post_1, notes_1, image_url_1 = analyze_tag(tag1)
    top_post_2, notes_2, image_url_2 = analyze_tag(tag2)

    if notes_1 > notes_2:
        winner = tag1
        winner_image_url = image_url_1
    elif notes_2 > notes_1:
        winner = tag2
        winner_image_url = image_url_2
    else:
        winner = None
        winner_image_url = None

    return render_template(
        'results.html',
        tag1=tag1, tag2=tag2,
        notes_1=notes_1, notes_2=notes_2,
        top_post_1=top_post_1,
        top_post_2=top_post_2,
        winner_image_url=winner_image_url,
        winner=winner
    )

@app.route('/test-results')
def test_results():
    fake_post_1 = {"blog_name": "testblog1", "note_count": 62, "like_count": 42, "reblog_count": 18, "reply_count": 2, "post_url": "https://tumblr.com"}
    fake_post_2 = {"blog_name": "otherblog1", "note_count": 38, "like_count": 25, "reblog_count": 10, "reply_count": 3, "post_url": "https://tumblr.com"}

    return render_template(
        'results.html',

        tag1="lestat", tag2="armand",
        notes_1=563, notes_2=334,
        top_post_1=fake_post_1,
        top_post_2=fake_post_2,
        winner="lestat", image_url_1="https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/PNG_transparency_demonstration_1.png/240px-PNG_transparency_demonstration_1.png",
        image_url_2="https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/PNG_transparency_demonstration_1.png/240px-PNG_transparency_demonstration_1.png"
    )

if __name__ == '__main__':
    app.run(debug=True)