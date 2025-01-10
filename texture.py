import pygame, moderngl
from typing import Dict

class texture_class:
    def __init__(self, engine):
        self.engine = engine
        self.ctx: moderngl.Context = self.engine.ctx
        self.textures: Dict[str, moderngl.Texture] = {}

    # default texture
    def load_texture(self, texture_name: str, path: str):
        texture = pygame.image.load(path).convert()
        texture = pygame.transform.flip(texture, flip_x=False, flip_y=True)
        texture = self.ctx.texture(size=texture.get_size(), components=3, data=pygame.image.tostring(texture, "RGB"))
        # mipmaps
        texture.filter = (moderngl.LINEAR_MIPMAP_LINEAR, moderngl.LINEAR)
        texture.build_mipmaps()
        texture.anisotropy = 32.0
        
        self.textures[texture_name] = texture
    
    def destroy(self):
        [tex.release() for tex in self.textures.values()]

    def get_texture(self, texture_name: str) -> moderngl.Texture:
        return self.textures[texture_name]