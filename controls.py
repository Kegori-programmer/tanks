import pygame


def keys(event, position):
    if event.type == pygame.QUIT:
        exit()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            position['title'] = 'up'
            position['x'] = 0
            position['y'] = 1
        elif event.key == pygame.K_DOWN:
            position['title'] = 'down'
            position['x'] = 0
            position['y'] = -1
        elif event.key == pygame.K_LEFT:
            position['title'] = 'left'
            position['x'] = -1
            position['y'] = 0
        elif event.key == pygame.K_RIGHT:
            position['title'] = 'right'
            position['x'] = 1
            position['y'] = 0
    return position
