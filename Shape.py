import numpy as np

class Shape:
    habitat_matrix = None
    x = None
    y = None
    w = None
    h = None
    r = None
    g = None
    b = None

    def __init__(self, x, y, w, h, r, g, b, habitat_w, habitat_h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.r = r
        self.g = g
        self.b = b

    def get_color_in_hex_str(self):
        color_in_hex = hex(self.r) + hex(self.g) + hex(self.b)
        color_in_hex = f"{color_in_hex.strip('0x')}"
        return color_in_hex
