import sys

name = sys.argv[1]
out  = sys.argv[2]

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{name}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,500;1,400&family=JetBrains+Mono:wght@400&display=swap">
  <style>
    *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}

    :root {{
      --bg: #fafaf8;
      --text: #1a1a1a;
      --muted: #777;
      --border: #e5e5e2;
    }}

    body {{
      background: var(--bg);
      font-family: 'EB Garamond', serif;
      display: flex;
      flex-direction: column;
      height: 100vh;
    }}

    nav {{
      border-bottom: 1px solid var(--border);
      padding: 0 2rem;
      display: grid;
      grid-template-columns: 1fr auto 1fr;
      align-items: center;
      height: 56px;
      flex-shrink: 0;
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

    nav ul a:hover {{ color: var(--text); }}

    iframe {{
      flex: 1;
      width: 100%;
      border: none;
    }}
  </style>
</head>
<body>
  <nav>
    <a class="name" href="../">Your Name</a>
    <ul>
      <li><a href="../">posts</a></li>
      <li><a href="../about.html">about</a></li>
    </ul>
  </nav>
  <iframe
    src="_raw/{name}.html"
    sandbox="allow-scripts allow-same-origin allow-downloads allow-popups allow-forms"
    allow="microphone"
    allowfullscreen
    loading="lazy"
  ></iframe>
</body>
</html>"""

with open(out, "w") as f:
    f.write(html)
