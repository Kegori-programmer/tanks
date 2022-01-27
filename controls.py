import pygame


def keys(event, result):

    if event.type == pygame.QUIT:
        exit()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            result = 'left'
        elif event.key == pygame.K_RIGHT:
            result = 'right'
        elif event.key == pygame.K_DOWN:
            result = 'down'
        elif event.key == pygame.K_UP:
            result = 'up'
    return result
