import sys, os
from shared import head, nav

name  = sys.argv[1]
title = name.replace("-", " ").title()

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
{head(title, home="../")}
  <style>
    body {{ display: flex; flex-direction: column; min-height: 100vh; }}
    .page {{ max-width: 800px; margin: 0 auto; background: #ffffff; display: flex; flex-direction: column; flex: 1; width: 100%; }}
    nav  {{ flex-shrink: 0; }}
    .wrap {{ flex: 1; display: flex; flex-direction: column; padding-top: 2rem; }}
    iframe {{ flex: 1; min-height: 80vh; width: 100%; border: none; }}
  </style>
</head>
<body>
<div class="page">
{nav(home="../")}
<div class="wrap">
<iframe
  src="_raw/{name}.html"
  sandbox="allow-scripts allow-same-origin allow-downloads allow-popups allow-forms"
  allow="microphone"
  allowfullscreen
  loading="lazy"
></iframe>
</div>
</div>
</body>
</html>"""

os.makedirs("docs/posts", exist_ok=True)
with open(f"docs/posts/{name}.html", "w") as f:
    f.write(html)
