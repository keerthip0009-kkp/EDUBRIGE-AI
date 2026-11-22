"""Builds a single self-contained index.html (CSS + JS inlined) for GitHub Pages from auth_component/."""
from pathlib import Path
src = Path("auth_component")
html = (src/"index.html").read_text(encoding="utf-8")
css = (src/"css/style.css").read_text(encoding="utf-8")
js = (src/"js/script.js").read_text(encoding="utf-8")

# --- standalone (GitHub Pages) mode: no Streamlit parent frame, so never pretend to authenticate ---
js = js.replace(
"  const post = (type, extra) => parent.postMessage(",
"  const STANDALONE = window.parent === window;   // true on GitHub Pages / when opened directly\n"
"  const post = (type, extra) => STANDALONE ? null : parent.postMessage(")
js = js.replace(
"    send(action, payload = {}) { setValue(action, payload); },",
"    send(action, payload = {}) { if (!STANDALONE) setValue(action, payload); },")
js = js.replace(
"    call(action, payload = {}) {\n      return new Promise(resolve => {",
"    call(action, payload = {}) {\n"
"      if (STANDALONE) return new Promise(resolve => setTimeout(() => resolve({ ok: false, error: window.EDUBRIDGE_APP_URL\n"
"        ? 'This page is a preview. Use the live app button to sign in.'\n"
"        : 'Preview only: sign-in needs the EduBridge backend, which is not connected to this page yet.' }), 600));\n"
"      return new Promise(resolve => {")
assert js.count("STANDALONE") >= 4

banner_css = """
.preview-bar{position:fixed;left:50%;bottom:16px;transform:translateX(-50%);z-index:50;display:flex;gap:12px;align-items:center;flex-wrap:wrap;justify-content:center;
 padding:10px 16px;border-radius:999px;background:rgba(16,20,48,.85);backdrop-filter:blur(12px);border:1px solid var(--line);font-size:.85rem;color:var(--muted);max-width:92vw}
.preview-bar a{color:#04050d;background:linear-gradient(135deg,var(--cyan),var(--purple));padding:6px 14px;border-radius:999px;font-weight:700;text-decoration:none}
"""
banner_html = """
<div class="preview-bar" id="previewBar" hidden>
  <span>Public preview of the EduBridge AI sign-in experience.</span>
  <a id="launchApp" href="#" target="_blank" rel="noopener" hidden>Open the live app &rarr;</a>
</div>
<script>
/* ===== CONFIG: after deploying the Streamlit app, paste its URL between the quotes, e.g. "https://edubridge-ai.streamlit.app" ===== */
window.EDUBRIDGE_APP_URL = "";
</script>
"""
banner_js = """
<script>
(() => {
  if (window.parent !== window) return;               // inside Streamlit: no banner
  const bar = document.getElementById('previewBar'), a = document.getElementById('launchApp');
  bar.hidden = false;
  if (window.EDUBRIDGE_APP_URL) { a.href = window.EDUBRIDGE_APP_URL; a.hidden = false; }
})();
</script>
"""
html = html.replace('<link rel="stylesheet" href="css/style.css">', "<style>\n"+css+banner_css+"\n</style>")
html = html.replace('<script src="js/script.js"></script>', banner_html+"<script>\n"+js+"\n</script>"+banner_js)
assert "css/style.css" not in html and "js/script.js" not in html
html = html.replace("<title>EduBridge AI — Sign in</title>", "<title>EduBridge AI — Learn · Match · Grow</title>")
Path("index.html").write_text(html, encoding="utf-8")
print("index.html", len(html)//1024, "KB")
