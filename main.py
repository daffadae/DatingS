import pygame
pygame.init()
scenes = {}
from bootup import *
from scenes.titlescreen import *
from scenes.game import *

screen = pygame.display.set_mode((805, 886))

TitleScreen = TitleScene(screen)
scenes["Title"] = TitleScreen
GameScene = GameScene(screen)
scenes["Game"] = GameScene

Game = CreateGame(screen, "Dating sim", 1000, 800, 30, TitleScreen, scenes)