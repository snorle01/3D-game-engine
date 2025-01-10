from __future__ import annotations

class rect_class:
    def __init__(self, position:tuple[int, int], width, height):
        self.position = position
        self.width = width
        self.height = height

    def colliding_with_rect(self, rect:rect_class):
        x = False
        y = False
        # X
        if self.position[0] < (rect.position[0] + rect.width) and self.position[0] + self.width > rect.position[0]:
            x = True
            
        # Y
        if self.position[1] < (rect.position[1] + rect.height) and self.position[1] + self.height > rect.position[1]:
            y = True

        return x and y