from models.canvas import Canvas
from models.validate import parse_text

PATH = "data/canvas.json"
OUTPUT_PATH = "data/rendered.png"


def apply_text(text: str, render: bool = True) -> int:
    """Apply lines like '/set x y #RRGGBB|air' to the canvas."""
    c = Canvas(PATH)
    w = c.file.data.settings.width
    h = c.file.data.settings.height
    pixels = parse_text(text, w, h)
    if not pixels:
        return 1
    for px in pixels:
        c.add_pixel(px)
    c.save()
    if render:
        c.render(OUTPUT_PATH)
    return 0
