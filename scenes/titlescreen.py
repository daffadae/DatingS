import pygame
from scene import *
import utils

class TitleScene(Scene):
    def __init__(self, screen):
        super().__init__("TitleScreen")
        self.screen = screen

        titlefont = pygame.font.SysFont("Trebuchet MS", 102)
        
        utils.image("TitleScreen", "Logo", "assets/icon.png", (screen.get_width() // 2, screen.get_height() // 10 * 2), anchor = "C")
        utils.text(scene = "TitleScreen", name = "TitleText", text = "Dating sim", position = (screen.get_width() // 2, (screen.get_height() // 9) * 4), color = (255,192,203), anchor = "C", font = titlefont)

        buttonfont = pygame.font.SysFont("Arial", 50)
        self.playbuttontext = utils.text("TitleScreen", "PlayButtonText", "PLAY", (screen.get_width() // 2, (screen.get_height() // 9.5) * 5.5), color = (255, 255, 255), anchor = "C", font = buttonfont)
        playbutton = utils.rectangle("TitleScreen", "PlayButton", (self.playbuttontext.calculate_anchor()[0] - 5, self.playbuttontext.calculate_anchor()[1] - 5, self.playbuttontext.get_text_size().size[0] + 10, self.playbuttontext.get_text_size().size[1] + 10), color = (200, 200, 200), fill = 2)
        playbutton.onclick = self.play

    def render(self, screen):
        screen.fill((30,30,30))

    def play(self):
        self.switch_to_scene("Game")