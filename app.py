from flask import Flask, render_template, request, redirect, url_for
from analyze import analyze_tag

app = Flask(__name__)

@app.route('/')
def home():
    return "HOMEPAAAAAAAAAGE!"

@app.route('/tags/<tag1>')
def show_tag(tag1):
    return f"Showing results for tag: {tag1}"

@app.route('/compare', methods=['POST', 'GET'])
def compare_tags():
    if request.method == 'POST':
        tag1 = request.form['tag1']
        tag2 = request.form['tag2']
        top_posts_1, notes_1, likes_1, reblogs_1, replies_1 = analyze_tag(tag1)
        top_posts_2, notes_2, likes_2, reblogs_2, replies_2 = analyze_tag(tag2)

        if notes_1 > notes_2:
            winner = f"🏆 Winner: #{tag1} with {notes_1} total notes!"
        elif notes_2 > notes_1:
            winner = f"🏆 Winner: #{tag2} with {notes_2} total notes!"
        else:
            winner = f"🤝 It's a tie! Both tags have {notes_1} notes."
        return winner 
    
    # If GET request, render a simple form to input tags
    return """
    <form method="POST">
            Tag 1: <input type="text" name="tag1"><br>
            Tag 2: <input type="text" name="tag2"><br>
            <input type="submit" value="Compare">
        </form>
    """


if __name__ == '__main__':
    app.run(debug=True)
