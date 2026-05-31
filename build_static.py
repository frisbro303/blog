import ast, os, subprocess
from shared import head, nav

def read_var(path, var):
    with open(path) as f:
        tree = ast.parse(f.read())
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == var:
                    return ast.literal_eval(node.value)
    return None

def git_date(filename):
    r = subprocess.run(
        ["git", "log", "--follow", "--format=%as", "-1", f"posts/{filename}"],
        capture_output=True, text=True
    )
    return r.stdout.strip()

def discover_posts():
    posts = []
    for f in sorted(os.listdir("posts"), reverse=True):
        if not f.endswith(".py"):
            continue
        slug = f[:-3]
        title   = read_var(f"posts/{f}", "title") or slug.replace("-", " ").title()
        excerpt = read_var(f"posts/{f}", "excerpt") or ""
        posts.append({
            "slug":    slug,
            "title":   title,
            "date":    git_date(f),
            "excerpt": excerpt,
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
    .section {{ max-width: 640px; margin: 0 auto; padding: 2rem 1.5rem 6rem; }}
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
    .content {{ max-width: 640px; margin: 0 auto; padding: 2rem 1.5rem 6rem; }}
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
  <p>I'm a researcher interested in <em>mathematics</em> and <em>computing</em>. This blog is where I write up ideas, experiments, and things I find worth sharing.</p>
  <div class="links">
    <a href="mailto:felix@granum.quest">email</a>
    <a href="https://github.com/frisbro303" target="_blank">github</a>
  </div>
</div>
</div>
</body>
</html>"""

write("docs/index.html", INDEX)
write("docs/about.html", ABOUT)
print("Built index.html and about.html")
