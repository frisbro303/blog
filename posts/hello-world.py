__post__ = {
    "title": "Hello World",
    "date": "2026-05-30",
    "excerpt": "A first post to test the setup.",
}

import marimo


__generated_with = "0.23.8"
app = marimo.App(css_file="blog.css")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Hello World
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    $$
    \sum_{i=1} x_{i}
    $$
    """)
    return


if __name__ == "__main__":
    app.run()
