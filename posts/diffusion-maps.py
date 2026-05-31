import marimo

__generated_with = "0.23.8"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    title = "Diffusion Maps"
    excerpt = "Exploring diffusion maps as a tool for non-linear dimensionality reduction."
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Diffusion Maps
    """)
    return


if __name__ == "__main__":
    app.run()
