import sys
from shared import nav

name = sys.argv[1]
out  = sys.argv[2]

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{name}</title>
  {nav(home="../")}
  <style>
    body {{ display: flex; flex-direction: column; height: 100vh; }}
    nav  {{ flex-shrink: 0; }}
    iframe {{ flex: 1; width: 100%; border: none; }}
  </style>
</head>
<body>
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
