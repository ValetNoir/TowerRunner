import pygame
from box import Box



def main():
    
    screen_size=[700,700]
    screen=pygame.display.set_mode(screen_size)
    running=True
    test_box=Box(sprite=pygame.image.load("./sprites/test_sprite.png"),size=(50, 200), pos=(screen_size[0]/2, screen_size[0]/2))
    while running:
        test_box.render(screen)
        
        for event in pygame.event.get():
            if event == pygame.QUIT:
                running=False
        
main()