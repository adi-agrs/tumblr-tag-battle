# Tumblr Tag Battle ⚔️

Compare the popularity of two Tumblr tags head-to-head using real engagement data — total notes, likes, reblogs, and replies — and crown a winner.

Built as a personal project to explore API integration, OAuth authentication, and data aggregation with Python.

---

## What it does

- Fetches up to 500 recent posts (within the last year) for two Tumblr tags
- Ranks posts by total note count and identifies the top N per tag
- Fetches a detailed notes breakdown (likes / reblogs / replies) for each top post via OAuth
- Crowns a winner based on total notes across all fetched posts
- Displays leaderboards: Most Liked, Most Reblogged, Most Discussed

---

## How it works

### Data pipeline

```
fetch posts (paginated) → rank by notes → fetch breakdown for top N → compare & display
```

1. **Fetching** — uses Tumblr's `/v2/tagged` endpoint with timestamp-based pagination to collect posts going back up to one year, stopping early once the time boundary is crossed (no wasted API calls)
2. **Ranking** — sorts all fetched posts by `note_count` and takes the top N
3. **Breakdown** — calls Tumblr's `/v2/blog/{blog}/notes` endpoint (requires OAuth) for each top post to split the combined note count into likes, reblogs, and replies
4. **Comparison** — sums total notes across all posts per tag and picks the winner

### Why two-step fetching?

The `/tagged` endpoint returns `note_count` for free on every post, which is enough for ranking. The detailed breakdown (likes vs. reblogs vs. replies) requires a separate authenticated call per post. Fetching breakdowns for all 500 posts would cost 500 extra API calls — so only the top N posts get the detailed treatment, keeping the total well within Tumblr's 5,000 requests/day limit.

---

## Tech stack

- **Python** — core logic
- **requests** + **requests-oauthlib** — HTTP calls and OAuth 1.0a signing
- **python-dotenv** — secret management

---

## Setup

### 1. Clone the repo

```bash
git clone https://github.com/YOUR-USERNAME/tumblr-tag-battle
cd tumblr-tag-battle
```

### 2. Install dependencies

```bash
pip install requests python-dotenv requests-oauthlib
```

### 3. Get a Tumblr API key

Register an app at https://www.tumblr.com/oauth/apps to get your **OAuth Consumer Key** and **Secret Key**.

### 4. Authorize with OAuth

Run the one-time authorization script:

```bash
python authorize.py
```

Follow the prompts — it'll open a Tumblr URL, you click Allow, paste back the verifier code, and it prints your access token and secret.

### 5. Set up your `.env` file

```
TUMBLR_API_KEY=your_consumer_key
TUMBLR_API_SECRET=your_secret_key
TUMBLR_ACCESS_TOKEN=your_access_token
TUMBLR_ACCESS_SECRET=your_access_secret
```

---

## Usage

```bash
python main.py <tag1> <tag2>
```

**Example:**
```bash
python main.py lestat armand
```

**Sample output:**
```
Fetching posts for tag 'lestat'...
Fetched 117 posts for tag 'lestat'.

Top 5 for lestat posts by note count:
Name: lonelyvampx — 62 notes
Name: whitewolf-the-unforgiven — 58 notes
...

🏆 Winner: #lestat with 563 total notes!
```

After the comparison, you'll be prompted to select a tag and view its leaderboard sorted by likes, reblogs, or replies.

---

## Project structure

```
tumblr-tag-battle/
├── main.py            # Entry point — takes two tags, runs comparison
├── analyze.py         # Core pipeline: fetch → rank → breakdown → return stats
├── fetch.py           # Paginated tag fetching with 1-year cutoff
├── stats.py           # Sorting and ranking logic
├── notes_breakdown.py # OAuth-authenticated notes breakdown per post
├── leaderboards.py    # Leaderboard display (likes / reblogs / replies)
├── authorize.py       # One-time OAuth setup script
├── config.py          # Loads API keys and config constants from .env
├── .env               # Secrets (not committed)
└── .gitignore
```

---

## Known limitations

- The `/tagged` endpoint returns at most 20 posts per request, so fetching 500 posts requires ~25 API calls with 0.5s pauses between them (~15 seconds per tag)
- Tumblr's notes endpoint returns the first ~50 notes per post. For posts with hundreds of notes, the likes/reblogs/replies breakdown is a sample, not a complete count — `note_count` remains the authoritative total
- `total_notes` from Tumblr occasionally differs from a manual tally of the notes list by 1-2, due to a `"posted"` note type included in Tumblr's count that isn't a like, reblog, or reply

---

## Roadmap

- [ ] Web interface (Flask) with side-by-side tag comparison UI
- [ ] Display top post image for each tag
- [ ] Deploy to a public URL