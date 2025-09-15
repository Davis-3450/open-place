import typer
from models.canvas import Canvas, Pixel

PATH = "data/canvas.json"
OUTPUT_PATH = "data/rendered.png"

c = Canvas(PATH)

app = typer.Typer()


@app.command()
def draw(color: str, x: int, y: int):
    c.add_pixel(Pixel(x=x, y=y, color=color))
    c.save()


@app.command()
def render():
    c.render(OUTPUT_PATH)


@app.command()
def save():
    c.save()


@app.command()
def validate():
    c.validate()


if __name__ == "__main__":
    app()
