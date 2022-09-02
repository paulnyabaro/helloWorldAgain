import pygame

pygame.init()

pygame.display.set_caption('My first pygame')
screen = pygame.display.set_mode([640, 480])
screen.fill([73, 29, 43])

pygame.display.update()

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


main()
