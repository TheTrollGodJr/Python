import pygame
import sys

pygame.init()

# Set up display
width, height = 1920, 1080
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("ASCII Art Game")

clock = pygame.time.Clock()

# Brightness levels and corresponding characters
asciiChars = "@&%QWMN0BDR8HXAUKGPOV4d9h6PkwqS2Y5Zoen[u1IlIfF}C{jXxY5E2aoyjx5ZneoIuJ7cTzsr!+><;=^_,:'-."

lines = []
for items in asciiChars:
    line = ""
    for i in range(320):
        line = f"{line}{items}"
    lines.append(line)
    print(line)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Game logic goes here

    # ASCII art rendering
    screen.fill((0, 0, 0))  # Clear the screen with a black background
    font_size = 10
    font = pygame.font.SysFont("monospace", font_size)

    '''
    # Draw a horizontal line of the chosen ASCII character
    for i, items in enumerate(lines):
        print(items)
        text = font.render(items, True, (255, 255, 255))
        screen.blit(text, (0,i * 6))
    '''
    
    for i in range(269):
        text = font.render(".", True, (255,255,255))
        screen.blit(text, (50, i * 4))

    pygame.display.flip()

    # Cap the frame rate to 60 fps
    clock.tick(60)
