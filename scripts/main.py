import typer
from models.canvas import Canvas, Pixel

PATH = "data/canvas.json"
OUTPUT_PATH = "data/rendered.png"

c = Canvas(PATH)

app = typer.Typer()


@app.command()
def draw(color: str, x: int, y: int):
    c.add_pixel(Pixel(x=x, y=y, color=color))


@app.command()
def process_string(text: str):
    """
    Procesa input estilo: "/set x y color"
    Ejemplo:
        /set 10 5 #ff0000
    """
    lines = text.strip().split("\n")
    success, failed = 0, 0

    for line in lines:
        if not line.startswith("/set"):
            print(f"❌ Invalid command: {line}")
            failed += 1
            continue

        parts = line.split()
        if len(parts) != 4:
            print(f"❌ Wrong format: {line}")
            failed += 1
            continue

        _, x_str, y_str, color = parts
        try:
            pixel = Pixel(x=int(x_str), y=int(y_str), color=color)
            c.add_pixel(pixel)
            print(f"✅ Added pixel {pixel}")
            success += 1
        except Exception as e:
            print(f"❌ Error parsing {line}: {e}")
            failed += 1
    c.save()

    typer.echo(f"Finished. Success: {success}, Failed: {failed}")


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
