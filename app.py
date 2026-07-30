from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from analyze import analyze_tag
from config import secret_key

app = Flask(__name__)
app.secret_key = secret_key

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/compare', methods=['POST'])
def compare():
    tag1 = request.form['tag1']
    tag2 = request.form['tag2']
    return redirect(url_for('loading', tag1=tag1, tag2=tag2))

@app.route('/loading')
def loading():
    tag1 = request.args.get('tag1')
    tag2 = request.args.get('tag2')
    return render_template('loading.html', tag1=tag1, tag2=tag2)

@app.route('/process', methods=['POST'])
def process():
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
        winner_image_url = image_url_1

    # only store what we actually need
    session['results'] = {
        'tag1': tag1, 'tag2': tag2,
        'winner': winner,
        'notes_1': notes_1, 'notes_2': notes_2,
        'winner_image_url': winner_image_url,
        'image_url_1': image_url_1,
        'image_url_2': image_url_2,
        'top_post_1': {
            'blog_name': top_post_1['blog_name'],
            'note_count': top_post_1['note_count'],
            'like_count': top_post_1['like_count'],
            'reblog_count': top_post_1['reblog_count'],
            'reply_count': top_post_1['reply_count'],
            'post_url': top_post_1['post_url'],
        },
        'top_post_2': {
            'blog_name': top_post_2['blog_name'],
            'note_count': top_post_2['note_count'],
            'like_count': top_post_2['like_count'],
            'reblog_count': top_post_2['reblog_count'],
            'reply_count': top_post_2['reply_count'],
            'post_url': top_post_2['post_url'],
        }
    }

    return jsonify({'status': 'done'})

@app.route('/results')
def results():
    data = session.get('results')
    if not data:
        return redirect(url_for('home'))
    return render_template('results.html', **data)

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
        winner="lestat",
        winner_image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/PNG_transparency_demonstration_1.png/240px-PNG_transparency_demonstration_1.png",
        image_url_1=None,
        image_url_2=None
    )

if __name__ == '__main__':
    app.run(debug=True)