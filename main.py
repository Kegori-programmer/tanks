import pygame

import controls

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('res/tank.mp3')
pygame.mixer.music.set_volume(0.5)
width = 640
height = 640
# Set up the drawing window
screen = pygame.display.set_mode([width, height])
font = pygame.font.Font('res/font.ttf', 15)
direction = {'x': 0, 'y': 0, 'title': 'idle'}
tank = {'x': width / 2, 'y': height / 2, 'size': 15, 'velocity': 0.25}
pygame.mixer.music.play()

while True:
    # Fill the background with white
    screen.fill((255, 255, 255))
    # Did the user click the window close button?
    for event in pygame.event.get():
        direction = controls.keys(event, direction)

    newPosX = tank['x'] + direction.get('x') * tank['velocity']
    newPosY = tank['y'] + direction.get('y') * tank['velocity']
    if newPosX + tank['size'] < width and newPosX - tank['size'] > 0 and newPosY + tank['size'] < height and newPosY - tank['size'] > 0:
        tank['x'] = newPosX
        tank['y'] += direction.get('y') * tank['velocity']
    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, pygame.Color('blue'), (tank.get('x'), tank.get('y')), tank.get('size'))
    # Draw title
    title = font.render(direction.get('title'), True, pygame.Color('black'))
    directionX = font.render('dirX: ' + str(direction.get('x')), True, pygame.Color('black'))
    directionY = font.render('dirY: ' + str(direction.get('y')), True, pygame.Color('black'))
    positionX = font.render('posX: ' + str(round(tank.get('x'), 2)), True, pygame.Color('black'))
    positionY = font.render('posY: ' + str(round(tank.get('y'), 2)), True, pygame.Color('black'))
    screen.blit(title, (5, 5))
    screen.blit(directionX, (5, 25))
    screen.blit(directionY, (5, 45))
    screen.blit(positionX, (5, 65))
    screen.blit(positionY, (5, 85))
    # Flip the display
    pygame.display.flip()
