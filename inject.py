import sys, os
from shared import head, nav

name  = sys.argv[1]
title = name.replace("-", " ").title()

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
{head(title, home="../")}
  <style>
    body {{ display: flex; flex-direction: column; height: 100vh; }}
    nav  {{ flex-shrink: 0; }}
    iframe {{ flex: 1; width: 100%; border: none; }}
  </style>
</head>
<body>
{nav(home="../")}
<iframe
  src="_raw/{name}.html"
  sandbox="allow-scripts allow-same-origin allow-downloads allow-popups allow-forms"
  allow="microphone"
  allowfullscreen
  loading="lazy"
></iframe>
</body>
</html>"""

os.makedirs("docs/posts", exist_ok=True)
with open(f"docs/posts/{name}.html", "w") as f:
    f.write(html)
