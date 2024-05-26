import pygame


def setup_screen(screen, settings):
    screen.fill("white")

    # Prepare static elements
    font = pygame.font.SysFont(settings.font_family, 36)
    text = font.render("Algorithm Visualiser", True, "black")
    text_rect = text.get_rect()
    text_rect.center = (settings.screen_width // 2, 30)

    screen.blit(text, text_rect)
