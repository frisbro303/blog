import marimo

__post__ = {
    "title": "Hello World",
    "date": "2026-05-30",
    "excerpt": "A first post to test the setup.",
}

__generated_with = "0.23.8"
app = marimo.App(width="medium")


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


if __name__ == "__main__":
    app.run()
