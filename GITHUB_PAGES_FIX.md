# GitHub Pages CSS fix

The root `index.html` now loads the assets from their actual repository locations:

- `auth_component/css/style.css`
- `auth_component/js/script.js`

Publish the repository root on the `main` branch in GitHub Pages settings. The site is a static front-end preview; Python features and server-backed sign-in require the Streamlit deployment (`app.py`) and configured backend/secrets.

After committing, wait for Pages to finish deploying, then hard-refresh the site with Ctrl+Shift+R.
