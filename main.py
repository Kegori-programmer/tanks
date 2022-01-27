import pygame

import controls
from TankClass import Tank


pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('res/tank.mp3')
pygame.mixer.music.set_volume(0.01)
# pygame.mixer.music.play()
width = 640
height = 640
# Set up the drawing window
screen = pygame.display.set_mode([width, height])
# Font
font = pygame.font.Font('res/small_pixel-7.ttf', 20)
# tank = {'x': width / 2, 'y': height / 2, 'size': 15, 'velocity': 0.25}
tank = Tank(width / 2, height / 2, 15, 0.25)
x, y, title = 0, 0, 'idle'

while True:
    # x, y, title = controls.keys_down(x, y, title)
    x, y, title = controls.keys_pressed()
    newPosX = tank.x + x * tank.velocity
    newPosY = tank.y + y * tank.velocity
    if newPosX + tank.size < width and newPosX - tank.size > 0 and newPosY + tank.size < height and newPosY - tank.size > 0:
        tank.x = newPosX
        tank.y = newPosY
    # Fill the background with white
    screen.fill((255, 255, 255))
    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, pygame.Color('blue'), (tank.x, tank.y), tank.size)
    # Draw title
    posTitle = font.render(f'stat: {title}', True, pygame.Color('black'))
    directionX = font.render('dirX: ' + str(x), True, pygame.Color('black'))
    directionY = font.render('dirY: ' + str(y), True, pygame.Color('black'))
    positionX = font.render('posX: ' + str(round(tank.x, 2)), True, pygame.Color('black'))
    positionY = font.render('posY: ' + str(round(tank.y, 2)), True, pygame.Color('black'))
    screen.blit(posTitle, (5, 5))
    screen.blit(directionX, (5, 25))
    screen.blit(directionY, (5, 45))
    screen.blit(positionX, (5, 65))
    screen.blit(positionY, (5, 85))
    # Flip the display
    pygame.display.flip()
