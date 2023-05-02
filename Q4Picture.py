import pygame, sys

pygame.init()

Display = pygame.display.set_mode((500,500))

Clock = pygame.time.Clock()
FPS = 60

while True:
    Display.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Code to render stuff
    pygame.draw.circle(Display, (255,0,0), (250, 200), 50)
    pygame.draw.line(Display, (0, 0, 255), (250, 0), (250, 500))
  
    pygame.display.flip()
    Clock.tick(FPS)