import pygame
from scene import *

class CreateGame():
    def __init__(self, screen, title: str, width: int, height: int, fps: int, starting_scene: Scene, scene_list: list):
        
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.active_scene = starting_scene

        pygame.display.set_caption(title)
        self.title = title

        while self.active_scene != None:
            pressed_keys = pygame.key.get_pressed()

            filtered_events = []
            for event in pygame.event.get():
                quit_attempt = False
                if event.type == pygame.QUIT:
                    quit_attempt = True
                elif event.type == pygame.KEYDOWN:
                    alt_pressed = pressed_keys[pygame.K_LALT] or \
                                  pressed_keys[pygame.K_RALT]
                    if event.key == pygame.K_F4 and alt_pressed:
                        quit_attempt = True

                if quit_attempt:
                    self.active_scene.terminate()
                else:
                    filtered_events.append(event)

            self.active_scene.process_input(filtered_events, pressed_keys)
            self.active_scene.update()
            self.active_scene.render(self.screen)
            self.active_scene.render_objects(self.screen)
            self.active_scene.process_buttons(filtered_events)
            
            if type(self.active_scene.next) == str:
                self.active_scene.next = scene_list[self.active_scene.next]
            self.active_scene = self.active_scene.next
        
            pygame.display.flip()
            self.clock.tick(fps)

    def rename_window(self, name: str):
        self.title = name
        pygame.display.set_caption(name)

    def set_icon(self, icon: str):
        pygame.display.set_icon(icon)