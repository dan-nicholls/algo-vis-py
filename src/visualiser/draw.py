import pygame


def setup_screen(screen, settings):
    screen.fill("white")

    # Prepare static elements
    font = pygame.font.SysFont(settings.font_family, 36)
    text = font.render("Algorithm Visualiser", True, "black")
    text_rect = text.get_rect()
    text_rect.center = (settings.screen_width // 2, 30)

    screen.blit(text, text_rect)


def draw_bars(screen, data, settings):
    bar_padding = settings.bar_padding
    bar_width = (settings.screen_width - (len(data) + 1) * bar_padding) / len(data)
    max_value = max(data)
    scale_factor = (settings.screen_height - 100) / max_value

    # Draw individual bars
    for i, value in enumerate(data):
        x = bar_padding + i * (bar_width + bar_padding)
        y = settings.screen_height - (value * scale_factor)
        height = value * scale_factor

        pygame.draw.rect(screen, settings.bar_color, (x, y, bar_width, height))
