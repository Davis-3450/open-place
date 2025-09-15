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

    def save(self, path: str):
        with open(path, "w") as f:
            f.write(self.model_dump_json())


class CanvasFile(BaseModel):
    data: Data


class Canvas:
    def __init__(self, path: str):
        self.path = Path(path)
        self.data = self._load()

    def save(self):
        self.data.save(self.path)

    def add_pixel(self, pixel: Pixel):
        self.data.canvas.append(pixel)
