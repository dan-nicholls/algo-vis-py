from colors import catpuccin_colors


class Settings:
    def __init__(self):
        self.screen_width = 1920
        self.screen_height = 1080

        self.font_family = "Ubuntu Mono"

        self.bar_max_width = 50
        self.bar_padding = 5

        self.frame_rate = 60
        self.num_values = 100

        # colors
        self.color_bg = catpuccin_colors["crust"]
        self.color_text = catpuccin_colors["text"]
        self.color_bar = catpuccin_colors["text"]
        self.color_bar_highlight_1 = catpuccin_colors["red"]
        self.color_bar_highlight_2 = catpuccin_colors["peach"]
        self.color_bar_highlight_3 = catpuccin_colors["green"]
