import pygame

import controls

pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])
font = pygame.font.Font('res/font.ttf', 25)

position = {'x': 0, 'y': 0, 'title': ''}

while True:
    # Fill the background with white
    screen.fill((255, 255, 255))
    # Did the user click the window close button?
    for event in pygame.event.get():
        position = controls.keys(event, position)
    # Draw a solid blue circle in the center
    # pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
    title = font.render(str(position['title']), True, pygame.Color('black'))
    x = font.render('x: ' + str(position['x']), True, pygame.Color('black'))
    y = font.render('y: ' + str(position['y']), True, pygame.Color('black'))
    screen.blit(title, (100, 100))
    screen.blit(x, (100, 125))
    screen.blit(y, (100, 150))
    # Flip the display
    pygame.display.flip()
