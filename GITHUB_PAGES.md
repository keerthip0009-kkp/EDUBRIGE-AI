# Get a public link (GitHub Pages)

This repo now has a **self-contained `index.html`** at the root (CSS + JS inlined, no extra files needed), so GitHub Pages can open it directly.

## Steps
1. Create a repo on github.com (e.g. `EduBridge-AI`, public).
2. Upload **everything inside this folder** (including the hidden `.nojekyll` file and the `auth_component/` folder). Easiest: install GitHub Desktop, or on the web use *Add file -> Upload files* and drag all files/folders in.
3. Repo **Settings -> Pages -> Build and deployment**: Source = *Deploy from a branch*, Branch = `main`, folder = `/ (root)` -> Save.
4. Wait ~1 minute. Your link is: `https://<your-github-username>.github.io/<repo-name>/`

## Why the old page looked unstyled
`auth_component/index.html` loads `css/style.css` and `js/script.js`. If those folders are missing or not served, you get plain black-and-white HTML. The root `index.html` avoids this by embedding both.

## What GitHub Pages can and cannot do
GitHub Pages hosts static files only. It shows the EduBridge landing + sign-in screen, but **cannot run `app.py`** (accounts, database, tutors, AI). On Pages, pressing Sign in shows a "preview only" message by design (no fake logins).

## To make the full app live
1. Deploy the repo on https://share.streamlit.io (main file `app.py`; see `STREAMLIT_DEPLOY.md`).
2. Open `index.html`, find `window.EDUBRIDGE_APP_URL = "";` and paste your Streamlit URL, e.g. `"https://edubridge-ai.streamlit.app"`. Commit. An "Open the live app" button then appears on your Pages link.

If you edit anything in `auth_component/`, regenerate the root page with `python build_static.py`.
