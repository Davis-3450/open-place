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
