"""All methods or functions imported and defined here

Use it in:
```
from all import *
```
"""

# Pygame
import pygame
from pygame.locals import *

# System
import os
import sys

# Typing
import typing
import extend_types
import enums

# Time
def second2frame(seconds:int, fps:int=60):
    return seconds*1000*fps
