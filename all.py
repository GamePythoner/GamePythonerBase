"""All methods or functions imported and defined here

Use it in:
```
from all import *
```
"""

# Typing
import typing
import extend_types
import enums

# Other file
import __init__
import scene

# Pygame
import pygame
from pygame.locals import *

def image2surf(image:extend_types.AvaliableImage, imageType=enums.ImageType) -> pygame.Surface:
    match imageType:
        case enums.ImageType.PATH:
            return pygame.image.load(image)
        case enums.ImageType.BINARY:
            return pygame.image.load(image, "file")
        case enums.ImageType.SURFACE:
            return image

# System
import os
import sys

# Typing
import typing
import extend_types
import enums

# Time
def second2frame(seconds:int, fps:int=60):
    return seconds*fps
