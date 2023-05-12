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

  
    pygame.draw.rect(Display, (173,216,230), pygame.Rect(0, 0, 500, 400))
    pygame.draw.rect(Display, (0,255,0), pygame.Rect(0, 400, 500, 400))
  
    pygame.draw.circle(Display, (255,255,0), (500, 0), 75)
    pygame.draw.rect(Display, (150,75,0), pygame.Rect(100, 200, 300, 200))
    pygame.draw.polygon(Display, (0,0,139), [(100, 200), (400, 200), (250,50)])
    
    
   
    #pygame.draw.line(Display, (0, 0, 255), (250, 0), (250, 500))
    #pygame.draw.line(Display, (0, 0, 255), (0, 250), (500, 250))
  
    pygame.display.flip()
    Clock.tick(FPS)