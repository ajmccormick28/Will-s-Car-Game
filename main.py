import pygame
import math
#how dare it learn math
import time
true = True
false = False
black = (0,0,0)
windowHeight = 800
acc = 0
vel = 0
windowWidth = 800
pygame.init()
xstart = windowWidth-100
ystart = windowHeight-100
screen = pygame.display.set_mode((windowHeight, windowWidth))
#pygame.image.load('car_sprite')
running = true
pause = false
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = false
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                running = false  
        
            elif event.key==pygame.K_p:
                if pause == true:
                    pause = false
                else:
                    pause = true
            elif event.key==pygame.K_w:
                acc += 1
           
               
            elif event.key==pygame.K_s:
                acc -= 1
    vel += acc
    ystart -= vel
    acc = 0
    screen.fill(black) 
    pygame.draw.circle(screen,(100,100,100),(xstart,ystart),10,0)
    pygame.display.update()
pygame.quit
