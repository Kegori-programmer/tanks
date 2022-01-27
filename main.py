import pygame
import controls

pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])
font = pygame.font.Font('res/font.ttf', 25)
result = ''
while True:
    # Fill the background with white
    screen.fill((255, 255, 255))
    # Did the user click the window close button?
    for event in pygame.event.get():
        result = controls.keys(event, result)
    # Draw a solid blue circle in the center
    # pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
    title = font.render(str(result), True, pygame.Color('black'))
    screen.blit(title, (100, 100))
    # Flip the display
    pygame.display.flip()
