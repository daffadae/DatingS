import pygame
import utils

class Scene:
    def __init__(self, name):
        self.name = name
        self.next = self
        utils.game_objects[name] = []
    
    def process_input(self, events, pressed_keys):
        pass

    def update(self):
        pass

    def render(self, screen):
        pass

    def render_objects(self, screen):
        objects = utils.game_objects[self.name]
        for object in objects:
            object.render(screen)

    def process_buttons(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                for object in utils.game_objects[self.name]:
                    if type(object) == utils.rectangle:
                        mouse = pygame.mouse.get_pos()
                        if utils.check_bounds(mouse, object.rect):
                            object.onclick()

    def switch_to_scene(self, next_scene):
        self.next = next_scene
    
    def terminate(self):
        self.switch_to_scene(None)