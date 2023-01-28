import pygame
from box import Box



def main():
    
    screen_size=[700,700]
    screen=pygame.display.set_mode(screen_size)
    running=True
    ground=Box(sprite=pygame.image.load("./sprites/test_ground.png"), size=(700, 50), pos=(0,screen_size[0]-50))
    test_box=Box(sprite=pygame.image.load("./sprites/test_sprite.png"),size=(50, 200), pos=(0, screen_size[0]-200-50))
    
    while running:
        pygame.time.Clock().tick(30)
        test_box.render(screen)
        ground.render(screen)
        
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
        
        pygame.display.update()
        
main()