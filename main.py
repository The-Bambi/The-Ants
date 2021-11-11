import random
import pygame
from Ant import Ant

screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()
DONE = False
PAUSE = False

test_ant = Ant(200, 200)

while not DONE:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                PAUSE = not PAUSE
            if event.key == pygame.K_ESCAPE:
                DONE = True

    if not PAUSE:
        screen.fill((0,0,0))
        test_ant.move(random.randint(-1,1), random.randint(-1,1))
        test_ant.debug()

        pygame.draw.rect(screen, (200,0,0), pygame.Rect(test_ant.x, test_ant.y, 3, 3))


        pygame.display.flip()
        clock.tick(30)
