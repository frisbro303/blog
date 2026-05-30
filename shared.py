FONTS = """
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,500;1,400&family=JetBrains+Mono:wght@400&display=swap">
"""

NAV_CSS = """
<style>
  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
  :root {
    --bg: #ffffff;
    --page-bg: #f5f5f5;
    --text: #1a1a1a;
    --muted: #777;
    --border: #e5e5e2;
  }
  body {
    background: var(--page-bg);
    color: var(--text);
    font-family: 'EB Garamond', serif;
    min-height: 100vh;
  }
  .page {
    max-width: 800px;
    margin: 0 auto;
    background: var(--bg);
    min-height: 100vh;
  }
  nav {
    border-bottom: 1px solid var(--border);
    padding: 1.25rem 2rem 1rem;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0.75rem;
    background: var(--bg);
  }
  nav a.name {
    font-size: 1.4rem;
    font-weight: 500;
    color: var(--text);
    text-decoration: none;
    letter-spacing: -0.01em;
  }
  nav a.name:hover { text-decoration: underline; text-underline-offset: 3px; }
  nav ul {
    list-style: none;
    display: flex;
    gap: 2rem;
  }
  nav ul a {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.78rem;
    color: var(--muted);
    text-decoration: none;
    letter-spacing: 0.02em;
  }
  nav ul a:hover, nav ul a.active { color: var(--text); }
</style>
"""

def nav(home="./", active=None):
    def link(page, label, href):
        cls = ' class="active"' if active == page else ""
        return f'<li><a href="{href}"{cls}>{label}</a></li>'
    return f"""<nav>
  <a class="name" href="{home}">The Endless Quest</a>
  <ul>
    {link("posts", "posts", home)}
    {link("about", "about", home + "about.html")}
  </ul>
</nav>"""

def head(title, home="./", active=None):
    return f"""  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  {FONTS}
  {NAV_CSS}"""
