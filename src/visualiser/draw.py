import pygame


def setup_screen(screen, settings):
    screen.fill("white")
    draw_static_elements(screen, settings)


def draw_static_elements(screen, settings):
    """Draw static UI elements."""
    font = pygame.font.SysFont(settings.font_family, 36)
    text = font.render("Algorithm Visualiser", True, "black")
    text_rect = text.get_rect()
    text_rect.center = (settings.screen_width // 2, 30)
    screen.blit(text, text_rect)


def draw_bars(screen, data, settings, highlight_indexes=None):
    screen.fill("white")

    bar_padding = settings.bar_padding
    bar_width = (settings.screen_width - (len(data) + 1) * bar_padding) / len(data)
    max_value = max(data)
    scale_factor = (settings.screen_height - 100) / max_value

    highlight_indexes = highlight_indexes or {}

    # Draw individual bars
    for i, value in enumerate(data):
        x = bar_padding + i * (bar_width + bar_padding)
        y = settings.screen_height - (value * scale_factor)
        height = value * scale_factor

        color = highlight_indexes.get(i, settings.bar_color)
        pygame.draw.rect(screen, color, (x, y, bar_width, height))

    draw_static_elements(screen, settings)


def draw_step_count(screen, step_count, settings):
    font = pygame.font.SysFont(settings.font_family, 24)
    text = font.render(f"Steps: {step_count}", True, "black")
    text_rect = text.get_rect()
    text_rect.topleft = (10, 10)
    screen.blit(text, text_rect)
