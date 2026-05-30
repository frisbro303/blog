import sys

NAV = """
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,500;1,400&family=JetBrains+Mono:wght@400&display=swap">
<style>
  #blog-nav {
    font-family: 'EB Garamond', serif;
    background: #fafaf8;
    border-bottom: 1px solid #e5e5e2;
    padding: 0 2rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
    height: 56px;
    position: sticky;
    top: 0;
    z-index: 9999;
  }
  #blog-nav a.name {
    font-size: 1.1rem;
    font-weight: 500;
    color: #1a1a1a;
    text-decoration: none;
  }
  #blog-nav ul {
    list-style: none;
    display: flex;
    gap: 2rem;
  }
  #blog-nav ul a {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.78rem;
    color: #777;
    text-decoration: none;
    letter-spacing: 0.02em;
  }
  #blog-nav ul a:hover { color: #1a1a1a; }
</style>
<nav id="blog-nav">
  <a class="name" href="../">Your Name</a>
  <ul>
    <li><a href="../">posts</a></li>
    <li><a href="../about.html">about</a></li>
  </ul>
</nav>
<div style="height: 2.5rem !important;"></div>
"""

path = sys.argv[1]
with open(path) as f:
    html = f.read()

html = html.replace("<body>", f"<body>{NAV}", 1)

with open(path, "w") as f:
    f.write(html)
