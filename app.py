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

if __name__ == '__main__':
    app.run(debug=True)