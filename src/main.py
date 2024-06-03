import pygame
import sys
from algorithms import BubbleSort, SelectionSort, InsertionSort
from settings import Settings
from visualiser.draw import draw_step_count, setup_screen, draw_bars
import random


def generate_initial_values(size, min_value=1, max_value=100):
    """Generates a list of random integers for the data set."""
    return [random.randint(min_value, max_value) for _ in range(size)]


def main():
    pygame.init()

    settings = Settings()

    screen = pygame.display.set_mode(
        (settings.screen_width, settings.screen_height),
        flags=pygame.DOUBLEBUF,
    )
    pygame.display.set_caption("Algorithm Visualiser")

    # Initialise data values
    values = generate_initial_values(30)

    # Initialise algorithm
    # algorithm = BubbleSort(values)
    # algorithm = SelectionSort(values)
    algorithm = InsertionSort(values)
    algorithm.initialise()

    setup_screen(screen, settings)

    step_count = 0
    is_paused = True

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_r:
                    is_paused = True
                    values = generate_initial_values(30)
                    algorithm.reset(values)
                    step_count = 0
                    setup_screen(screen, settings)
                    continue
                elif event.key == pygame.K_SPACE:
                    is_paused = not is_paused
                    continue

        if not is_paused:
            if not algorithm.is_sorted():
                algorithm.step()
                step_count += 1

        highlight_indexes = {
            # [algorithm.j, algorithm.j + 1]
            # if algorithm.j < algorithm.n - 1 - algorithm.i
            # else []
            algorithm.j: "red",
            algorithm.i: "orange",
            **(
                {algorithm.min_index: "blue"} if hasattr(algorithm, "min_index") else {}
            ),
        }
        draw_bars(screen, algorithm.data, settings, highlight_indexes)
        draw_step_count(screen, step_count, settings)
        pygame.display.flip()
        pygame.time.Clock().tick(settings.frame_rate)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
