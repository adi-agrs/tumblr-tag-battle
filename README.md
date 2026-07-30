# Tumblr Tag Battle

Compare the popularity of two Tumblr tags head-to-head using real engagement data — total notes, likes, reblogs, and replies — and crown a winner.

**Live at:** https://tumblr-tag-battle.onrender.com

Built as a personal project to explore API integration, OAuth authentication, data aggregation with Python, and full-stack web deployment.

---

## What it does

- Fetches up to 100 recent posts (within the last year) for two Tumblr tags
- Finds the single highest-noted post per tag
- Fetches a notes breakdown (likes / reblogs / replies) for just those two posts via OAuth
- Extracts the highest-noted image post per tag and displays it on the results page
- Crowns a winner based on total notes across all fetched posts
- Displays a dramatic animated results page with confetti

---

## How it works

### Data pipeline

```
fetch posts (paginated) → find top post → fetch breakdown → compare → display
```

1. **Fetching** — uses Tumblr's `/v2/tagged` endpoint with timestamp-based pagination to collect posts going back up to one year, stopping early once the time boundary is crossed (no wasted API calls)
2. **Ranking** — finds the single highest `note_count` post per tag using `max()` instead of sorting the whole list
3. **Breakdown** — calls Tumblr's `/v2/blog/{blog}/notes` endpoint (requires OAuth 1.0a) for just the two top posts — one per tag — to split the combined note count into likes, reblogs, and replies
4. **Image extraction** — separately finds the highest-noted photo post per tag and extracts its image URL
5. **Comparison** — sums total notes across all posts per tag and picks the winner

### Why two-step fetching?

The `/tagged` endpoint returns `note_count` for free on every post, which is enough for ranking. The detailed breakdown (likes vs. reblogs vs. replies) requires a separate authenticated call. By only fetching the breakdown for the single top post per tag, the entire comparison costs just 2 extra API calls — well within Tumblr's 5,000 requests/day limit.

### Loading page architecture

Processing takes time. Rather than making the user stare at a blank page, the app uses an async architecture:

1. `/compare` immediately redirects to `/loading` with the tags in the URL
2. The loading page renders instantly and starts a fake "results preview" — numbers ticking up, blog names cycling, winner randomly flickering
3. The loading page simultaneously calls `/process` in the background via `fetch`
4. When Flask finishes, it stores results in a session and returns `"done"`
5. The loading page plays a wave transition and redirects to `/results`

---

## Tech stack

- **Python** — core logic
- **Flask** — web framework + session management
- **requests** + **requests-oauthlib** — HTTP calls and OAuth 1.0a signing
- **python-dotenv** — secret management
- **gunicorn** — production WSGI server
- **Vanilla JS** — animations, cursor effects, async fetch, confetti
- **CSS** — dot grid background, wave transitions, parallax scroll
- **Render** — deployment

---

## Setup

### 1. Clone the repo

```bash
git clone https://github.com/adi-agrs/tumblr-tag-battle
cd tumblr-tag-battle
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Get a Tumblr API key

Register an app at https://www.tumblr.com/oauth/apps to get your **OAuth Consumer Key** and **Secret Key**.

### 4. Authorize with OAuth

Run the one-time authorization script:

```bash
python authorize.py
```

Follow the prompts — it opens a Tumblr URL, you click Allow, paste back the verifier code, and it prints your access token and secret.

### 5. Set up your `.env` file

```
TUMBLR_API_KEY=your_consumer_key
TUMBLR_API_SECRET=your_secret_key
TUMBLR_ACCESS_TOKEN=your_access_token
TUMBLR_ACCESS_SECRET=your_access_secret
SECRET_KEY=your_flask_secret_key
```

Generate a secret key with:
```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

### 6. Run locally

```bash
python app.py
```

Then open `http://127.0.0.1:5000`.

---

## Project structure

```
tumblr-tag-battle/
├── app.py             # Flask routes — index, compare, loading, process, results
├── analyze.py         # Core pipeline: fetch → rank → breakdown → image extraction
├── fetch.py           # Paginated tag fetching with 1-year cutoff
├── stats.py           # Sorting and ranking logic
├── notes_breakdown.py # OAuth-authenticated notes breakdown per post
├── authorize.py       # One-time OAuth setup script
├── config.py          # Loads API keys and config constants from .env
├── requirements.txt   # Python dependencies
├── render.yaml        # Render deployment config
├── templates/
│   ├── index.html     # Home page — tag input form
│   ├── loading.html   # Animated loading page with fake preview
│   └── results.html   # Results page — winner, stats, top post image
├── static/
│   ├── style.css      # All styles
│   ├── script.js      # Cursor, waves, confetti, form handling
│   ├── images/        # SVG assets
│   └── sounds/        # Audio files
├── .env               # Secrets (not committed)
└── .gitignore
```

---

## Known limitations

- Render's free tier spins down after 15 minutes of inactivity — first visit after idle takes ~30 seconds to wake up
- The `/tagged` endpoint returns at most 20 posts per request, so fetching 100 posts requires ~5 paginated API calls
- Tumblr's notes endpoint returns the first ~50 notes per post — for posts with hundreds of notes, the breakdown is a sample, not a complete count
- `total_notes` from Tumblr occasionally differs from a manual tally by 1-2, due to a `"posted"` note type included in Tumblr's count

---

## ✅ Roadmap

- [x] Core data pipeline — fetch, rank, breakdown
- [x] OAuth 1.0a authentication
- [x] Flask web interface
- [x] Animated loading page with async processing
- [x] Top post image display
- [x] Deployed to Render
