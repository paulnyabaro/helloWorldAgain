import pygame
from collections import namedtuple

Colour = namedtuple("Colour", ["red", "green", "blue"])

BACKGROUND_COLOUR = Colour(red=36, green=188, blue=168)
RECTANGLE_COLOUR = Colour(red=255, green=255, blue=255)

pygame.init()

pygame.display.set_caption('My first pygame')
screen = pygame.display.set_mode([640, 480])
screen.fill(BACKGROUND_COLOUR)

pygame.draw.rect(screen, RECTANGLE_COLOUR, [0, 0, 100, 50])

pygame.display.update()

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


main()
