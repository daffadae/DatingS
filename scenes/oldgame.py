import pygame
from scene import *
import utils
import json
import random
import textwrap
wrapper = textwrap.TextWrapper(width = 50)

class GameScene(Scene):
    def __init__(self, screen):
        super().__init__("Game")
        self.screen = screen

        game_path_file = open('game_path.json')
        self.game_path = json.load(game_path_file)
        game_path_file.close()

        self.font = pygame.font.Font('assets/gadaj_font.otf', 26)

        self.slide_index = 0
        self.slide = self.game_path[self.slide_index]
        self.background_img = utils.image("Game", "Slide", f'assets/{self.slide[1]}', (0, 0), anchor = "NW")
        self.choice_img = utils.image("Game", "Choices", f'assets/choices.png', (0, 0), anchor = "NW", visible = False)
        self.choosing = False
        self.TextPrompts = []
        self.options = []
        self.score = 0
        self.lastType = "good"


    def render(self, screen):
        screen.fill((40,40,40))
        pass

    def process_input(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                self.slide_index = min(self.slide_index + 1, len(self.game_path)-1)
                next = self.game_path[self.slide_index]
                self.slide = next
                if self.choosing:
                    #Option 1
                    #(64, 196) - (768, 299)

                    #Option 2
                    #(62, 326) - (766, 426)

                    #Option 3
                    #(62, 453) - (767, 553)
                    mouse_pos = pygame.mouse.get_pos()
                    
                    option = None
                    if utils.check_bounds(mouse_pos, (64, 196, 704, 103)):
                        option = 0
                    if utils.check_bounds(mouse_pos, (62, 326, 704, 100)):
                        option = 1
                    if utils.check_bounds(mouse_pos, (64, 453, 704, 103)):
                        option = 2

                    
                    
                    if option != None:
                        for TextPrompt in self.TextPrompts:
                            TextPrompt.destroy()
                        self.choice_img.visible = False
                        print(self.options[option])
                        self.lastType = self.options[option]
                        if self.options[option] == "good":
                            self.score += 1
                        elif self.options[option] == "bad":
                            self.score -= 1
                        print(self.score)
                        self.choosing = False

                if next[0] == "image" and not self.choosing:
                    self.background_img.image_path = f'assets/{self.slide[1]}'
                    self.background_img.reload_image()
                if next[0] == "answers" and not self.choosing:
                    self.choice_img.visible = True
                    self.choosing = True
                    options = {"good": wrapper.wrap(self.slide[1]["good"]), "neutral": wrapper.wrap(self.slide[1]["neutral"]), "bad": wrapper.wrap(self.slide[1]["bad"])}
                    keys =  list(options.items())
                    random.shuffle(keys)
                    options = dict(keys)
                    self.options = list(options.keys())
                    for optionindex, option in enumerate(options): #125 Y difference
                        for index, text in enumerate(options[option]):
                            length = len(options[option])
                            
                            if length == 1:
                                optiontext = utils.text("Game", "Option1Text", text, (422, (252 + 125 * (optionindex))), font = self.font, color = (214, 216, 177), anchor = "C")
                                self.TextPrompts.append(optiontext)
                            else:
                                if index < length / 2:
                                    optiontext = utils.text("Game", "Option1Text", text, (422, (252 + 125 * (optionindex)) - ((index + 1) * 14)), font = self.font, color = (214, 216, 177), anchor = "C")
                                    self.TextPrompts.append(optiontext)
                                else:
                                    optiontext = utils.text("Game", "Option1Text", text, (422, (252 + 125 * (optionindex)) + ((index + 1) * 10)), font = self.font, color = (214, 216, 177), anchor = "C")
                                    self.TextPrompts.append(optiontext)
                if next[0] == "response" and not self.choosing:
                    self.background_img.image_path = f'assets/{self.slide[1][self.lastType]}'
                    self.background_img.reload_image()


"""
    ["image", "slides/3.jpg"],

    ["answers", {
        "good": "I think I was abducted by aliens in my dream",
        "neutral": "Once, street cats began to follow me, there were about 6 of them.",
        "bad": "One day I bought a really tasty lunch at the university cafeteria."
    }],

    ["response", {
        "good": "slides/arrival.png",
        "neutral": "slides/talking1.png",
        "bad": "slides/waiting.png"
    }],
"""