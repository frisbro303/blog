import ast, os
from shared import head, nav

def read_meta(path):
    with open(path) as f:
        tree = ast.parse(f.read())
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == "__post__":
                    return ast.literal_eval(node.value)
    return {}

def discover_posts():
    posts = []
    for f in sorted(os.listdir("posts"), reverse=True):
        if not f.endswith(".py"):
            continue
        slug = f[:-3]
        meta = read_meta(f"posts/{f}")
        posts.append({
            "slug":    slug,
            "title":   meta.get("title", slug.replace("-", " ").title()),
            "date":    meta.get("date", ""),
            "excerpt": meta.get("excerpt", ""),
        })
    return posts

def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(content)

def post_items():
    rows = []
    for p in discover_posts():
        excerpt = f'<span class="excerpt">{p["excerpt"]}</span>' if p["excerpt"] else ""
        rows.append(f"""      <li>
        <a href="posts/{p['slug']}.html">
          <span class="title">{p['title']}</span>
          {excerpt}
          <span class="date">{p['date']}</span>
        </a>
      </li>""")
    return "\n".join(rows)

INDEX = f"""<!DOCTYPE html>
<html lang="en">
<head>
{head("The Endless Quest", home="./", active="posts")}
  <style>
    .hero {{ max-width: 640px; margin: 5rem auto 4rem; padding: 0 1.5rem; }}
    .hero h2 {{ font-size: 1.05rem; font-weight: 400; font-style: italic; color: var(--muted); margin-bottom: 0.75rem; }}
    .hero p {{ font-size: 1.25rem; line-height: 1.75; }}
    .section {{ max-width: 640px; margin: 0 auto; padding: 0 1.5rem 6rem; }}
    .section-label {{ font-family: 'JetBrains Mono', monospace; font-size: 0.72rem; color: var(--muted); letter-spacing: 0.08em; text-transform: uppercase; margin-bottom: 1.5rem; }}
    .posts {{ list-style: none; }}
    .posts li {{ border-top: 1px solid var(--border); padding: 1.4rem 0; }}
    .posts li:last-child {{ border-bottom: 1px solid var(--border); }}
    .posts a {{ text-decoration: none; color: inherit; display: block; }}
    .posts a:hover .title {{ text-decoration: underline; text-underline-offset: 3px; }}
    .title {{ font-size: 1.15rem; font-weight: 500; display: block; margin-bottom: 0.3rem; }}
    .excerpt {{ font-style: italic; color: var(--muted); font-size: 1rem; line-height: 1.55; display: block; margin-bottom: 0.5rem; }}
    .date {{ font-family: 'JetBrains Mono', monospace; font-size: 0.7rem; color: #bbb; }}
  </style>
</head>
<body>
<div class="page">
{nav(home="./", active="posts")}
<div class="section">
  <p class="section-label">All posts</p>
  <ul class="posts">
{post_items()}
  </ul>
</div>
</div>
</body>
</html>"""

ABOUT = f"""<!DOCTYPE html>
<html lang="en">
<head>
{head("About — The Endless Quest", home="./", active="about")}
  <style>
    .content {{ max-width: 640px; margin: 5rem auto; padding: 0 1.5rem; }}
    .content h1 {{ font-size: 1.6rem; font-weight: 500; margin-bottom: 2rem; }}
    .content p {{ line-height: 1.8; color: #333; margin-bottom: 1.25rem; }}
    .content p em {{ font-style: italic; color: var(--text); }}
    .links {{ margin-top: 2.5rem; display: flex; gap: 1.5rem; }}
    .links a {{ font-family: 'JetBrains Mono', monospace; font-size: 0.78rem; color: var(--muted); text-decoration: none; letter-spacing: 0.02em; }}
    .links a:hover {{ color: var(--text); }}
  </style>
</head>
<body>
<div class="page">
{nav(home="./", active="about")}
<div class="content">
  <h1>About</h1>
  <p>I'm a researcher interested in <em>mathematics</em> and <em>computing</em>. This blog is where I write up ideas, experiments, and things I find worth sharing.</p>
  <p>Posts are written as interactive Marimo notebooks — you can run and modify the code directly in your browser.</p>
  <p>I'm currently based in Copenhagen.</p>
  <div class="links">
    <a href="mailto:you@example.com">email</a>
    <a href="https://github.com/frisbro303" target="_blank">github</a>
  </div>
</div>
</div>
</body>
</html>"""

write("docs/index.html", INDEX)
write("docs/about.html", ABOUT)
print("Built index.html and about.html")
