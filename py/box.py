import pygame
class Box:
    def __init__(self, sprite, size, pos=[0,0]):
        self.sprite=sprite
        rect=pygame.Rect(left_top=pos, width_height=size)
        self.click_box=rect
        self.pos=pos
        
    def move(self, vec):
        self.pos[0]+=vec[0]
        self.pos[1]+=vec[1]
        self.click_box.move(vec[0],vec[1])
    
    def is_clicked(self, mouse, is_mouse_down):
        return self.click_box.collidepoint(mouse[0], mouse[1]) and is_mouse_down
    
    def render(self, screen:pygame.Surface):
        screen.blit(self.sprite, self.pos)