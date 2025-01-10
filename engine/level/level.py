import pygame
from typing import List

class level_class:
    def __init__(self, size:tuple[int, int], floor_dir:str, wall_dir:str, ceiling_dir:str):
        self.size = size
        # get data from image
        def get_data(surface:pygame.Surface):
            data = []
            for y in range(self.size[1]):
                for x in range(self.size[0]):
                    if surface.get_at((x, y)) == (255, 255, 255):
                        data.append(1)
                    else:
                        data.append(0)
            return data
        
        surface_floor = pygame.image.load(floor_dir).convert()
        self.floor = get_data(surface_floor)

        surface_wall = pygame.image.load(wall_dir)
        self.wall = get_data(surface_wall)

        surface_ceiling = pygame.image.load(ceiling_dir)
        self.ceiling = get_data(surface_ceiling)

    def index_to_X(self, index: int) -> int:
        return index % self.size[0]

    def index_to_Y(self, index: int) -> int:
        return index // self.size[0]

    def index_to_XY(self, index: int) -> tuple[int, int]:
        return (self.index_to_X(index), self.index_to_Y(index))

    # the position tule must contain int's or it will return an float value
    def XY_to_index(self, position:tuple[int, int]) -> int:
        return position[0] + (position[1] * self.size[0])