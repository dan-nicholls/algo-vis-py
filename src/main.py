import pygame
import sys
from settings import Settings
from visualiser.draw import setup_screen, draw_bars


def main():
    pygame.init()

    settings = Settings()

    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Algorithm Visualiser")

    # Check algorithm from user
    values = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500]
    # values = [4] * 100
    # values = [1, 3, 5]
    # values = [1, 3, 5, 50, 76, 100]

    setup_screen(screen, settings)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        draw_bars(screen, values, settings)
        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
