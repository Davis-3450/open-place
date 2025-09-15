from enum import Enum


# pastel colors
class Color(str, Enum):
    """Default color palette"""

    # Colors  | Catpuccin
    RED = "#ffadad"
    BROWN = "#dc9f8f" #fix
    ORANGE = "#ffd6a5"
    YELLOW = "#fdffb6"
    GREEN = "#caffbf"
    CYAN = "#9bf6ff"
    BLUE = "#a0c4ff"
    PINK = "#fcb6ff"
    PURPLE = "#bdb2ff"
    
    # Monochrome
    BLACK = "#000000"
    WHITE = "#ffffff"
    GRAY = "#808080"