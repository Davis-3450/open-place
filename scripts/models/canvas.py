from pathlib import Path

from PIL import Image
from pydantic import BaseModel, Field

# from pydantic_extra_types.color


class Pixel(BaseModel):
    x: int = Field(ge=0)
    y: int = Field(ge=0)
    color: str  # Idea: maybe implement default to #
    ## maybe usernamee later


class Settings(BaseModel):
    width: int = Field(ge=0)
    height: int = Field(ge=0)


class Data(BaseModel):
    """Canvas model"""

    canvas: list[Pixel] = []
    settings: Settings


class CanvasFile(BaseModel):
    data: Data

    def save(self, path: str | Path):
        Path(path).write_text(self.model_dump_json(indent=2), encoding="utf-8")


class Canvas:
    def __init__(self, path: str):
        self.path = Path(path)
        self.file = self._load()

    def save(self):
        self.file.save(self.path)

    def add_pixel(self, pixel: Pixel):
        self.file.data.canvas.append(pixel)

    def render(self, out_path: str = "canvas.png", scale: int = 8):
        w, h = self.file.data.settings.width, self.file.data.settings.height
        img = Image.new("RGB", (w, h), (255, 255, 255))

        for px in self.file.data.canvas:
            if 0 <= px.x < w and 0 <= px.y < h:
                color = tuple(int(px.color[i : i + 2], 16) for i in (1, 3, 5))
                img.putpixel((px.x, px.y), color)

        if scale > 1:
            img = img.resize((w * scale, h * scale), Image.NEAREST)

        img.save(out_path)
        print(f"successfully rendered {out_path} ({w}x{h}, scale {scale} x)")

    def validate(self):
        pass

    def _load(self) -> CanvasFile:
        text = self.path.read_text(encoding="utf-8")
        return CanvasFile.model_validate_json(text)
