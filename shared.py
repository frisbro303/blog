NAV_STYLE = """
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,500;1,400&family=JetBrains+Mono:wght@400&display=swap">
<style>
  :root {{
    --bg: #fafaf8;
    --text: #1a1a1a;
    --muted: #777;
    --border: #e5e5e2;
  }}

  body {{
    background: var(--bg);
    font-family: 'EB Garamond', serif;
  }}

  nav {{
    border-bottom: 1px solid var(--border);
    padding: 0 2rem;
    display: grid;
    grid-template-columns: 1fr auto 1fr;
    align-items: center;
    height: 56px;
    background: var(--bg);
  }}

  nav .name {{
    font-size: 1.1rem;
    font-weight: 500;
    color: var(--text);
    text-decoration: none;
  }}

  nav .name:hover {{ text-decoration: underline; text-underline-offset: 3px; }}

  nav ul {{
    list-style: none;
    display: flex;
    gap: 2rem;
  }}

  nav ul a {{
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.78rem;
    color: var(--muted);
    text-decoration: none;
    letter-spacing: 0.02em;
  }}

  nav ul a:hover, nav ul a.active {{ color: var(--text); }}
</style>
"""

def nav(home="./", active="posts"):
    def link(page, label, href):
        cls = ' class="active"' if active == page else ''
        return f'<li><a href="{href}"{cls}>{label}</a></li>'

    return NAV_STYLE + f"""
<nav>
  <a class="name" href="{home}">Your Name</a>
  <ul>
    {link("posts", "posts", home)}
    {link("about", "about", home + "about.html")}
  </ul>
</nav>
"""
