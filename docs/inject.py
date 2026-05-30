import sys

HEADER = """
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,500;1,400&family=JetBrains+Mono:wght@400&display=swap">
<style>
  :root {
    --bg: #fafaf8; --text: #1a1a1a; --muted: #666; --border: #e8e8e4;
  }
  #blog-nav {
    display: flex; justify-content: space-between; align-items: center;
    padding: 1.25rem 2.5rem; border-bottom: 1px solid var(--border);
    background: var(--bg); position: sticky; top: 0; z-index: 10000;
    font-family: 'EB Garamond', serif;
  }
  #blog-nav a.nav-name { font-size: 1.05rem; font-weight: 500; text-decoration: none; color: var(--text); }
  #blog-nav .nav-links { display: flex; gap: 2rem; }
  #blog-nav .nav-links a { font-size: 0.95rem; color: var(--muted); text-decoration: none; transition: color 0.15s; }
  #blog-nav .nav-links a:hover { color: var(--text); }
</style>
<div id="blog-nav">
  <a class="nav-name" href="/">Your Name</a>
  <div class="nav-links">
    <a href="/">Posts</a>
    <a href="/about.html">About</a>
  </div>
</div>
"""

path = sys.argv[1]
with open(path) as f:
    html = f.read()

html = html.replace("<body>", f"<body>{HEADER}", 1)

with open(path, "w") as f:
    f.write(html)
