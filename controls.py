import pygame


def keys_down(x, y, title):
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                return 0, -1, 'up'
            elif event.key == pygame.K_DOWN:
                return 0, 1, 'down'
            elif event.key == pygame.K_LEFT:
                return -1, 0, 'left'
            elif event.key == pygame.K_RIGHT:
                return 1, 0, 'right'
    return x, y, title


def keys_pressed():
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        return 0, -1, 'up'
    if pressed[pygame.K_DOWN]:
        return 0, 1, 'down'
    if pressed[pygame.K_LEFT]:
        return -1, 0, 'left'
    if pressed[pygame.K_RIGHT]:
        return 1, 0, 'right'
    return 0, 0, 'idle'
