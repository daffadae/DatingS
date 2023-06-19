import pygame

game_objects = {}
default_font = pygame.font.SysFont('Arial.ttf', 32)

def check_bounds(tuple1, tuple2):
    if tuple1[0] >= tuple2[0] and tuple1[1] >= tuple2[1] and tuple1[0] <= tuple2[0] + tuple2[2] and tuple1[1] <= tuple2[1] + tuple2[3]:
        return True
    return False

class text():
    def __init__(self, scene, name: str, text: str, position: tuple[int, int], font: pygame.font.Font = default_font, color: tuple[int, int, int] = (0, 0, 0), background_color: tuple[int, int, int] = None, anchor: str = "NW"):
        self.name = name
        self.visibility = 1
        self.scene = scene
        self.text = text
        self.position = position
        self.font = font
        self.color = color
        self.background_color = background_color
        self.anchor = anchor
        game_objects[scene].append(self)

    def calculate_anchor(self):
        text_render = self.font.render(self.text, False, (0,0,0))
        rect = list(self.position)
        if self.anchor == "C":
            rect[0] = rect[0] - text_render.get_rect().center[0]
            rect[1] = rect[1] - text_render.get_rect().center[1]
        elif self.anchor == "N":
            rect[0] = rect[0] - text_render.get_rect().center[0]
        elif self.anchor == "S":
            rect[0] = rect[0] - text_render.get_rect().center[0]
            rect[1] = rect[1] - text_render.get_rect().midbottom[1]
        elif self.anchor == "W":
            rect[1] = rect[1] - (text_render.get_rect().center[1])
        elif self.anchor == "E":
            rect[1] = rect[1] - text_render.get_rect().center[1]
            rect[0] = rect[0] - text_render.get_rect().right
        elif self.anchor == "NE":
            rect[0] = rect[0] - text_render.get_rect().right
        elif self.anchor == "SE":
            rect[0] = rect[0] - text_render.get_rect().right
            rect[1] = rect[1] - text_render.get_rect().midbottom[1]
        elif self.anchor == "SW":
            rect[1] = rect[1] - text_render.get_rect().midbottom[1]

        return tuple(rect)
    
    def render(self, screen):
        text_render = self.font.render(self.text, True, self.color, self.background_color)
        screen.blit(text_render, self.calculate_anchor())

    def destroy(self):
        def nothing(screen):
            pass
        self.render = nothing
        
        del self

    def get_text_size(self):
        text_render = self.font.render(self.text, False, (0,0,0))
        return text_render.get_rect()

    def set_anchor(self, new_anchor):
        self.anchor = new_anchor

class rectangle():
    def __init__(self, scene, name: str, rect: tuple[int, int, int, int] = [0, 0, 50, 50], color: tuple[int, int, int] = [0, 0, 0], fill: int = 0, visible: bool = True):
        self.name = name
        self.visibility = 1
        self.scene = scene
        self.rect = rect
        self.color = color
        self.fill = fill
        self.visible = visible
        game_objects[scene].append(self)

    def render(self, screen):
        if self.visible:
            pygame.draw.rect(screen, self.color, pygame.Rect(self.rect), self.fill)

    def onclick(self):
        pass

class image():
    def __init__(self, scene, name: str, image_path: str, position: tuple[int, int], anchor = "C", visible: bool = True):
        self.name = name
        self.visibility = 1
        self.scene = scene
        self.image_path = image_path
        self.position = position
        self.img = pygame.image.load(image_path).convert_alpha()
        self.anchor = anchor
        self.visible = visible

        game_objects[scene].append(self)

    def calculate_anchor(self):
        rect = list(self.position)
        if self.anchor == "C":
            rect[0] = rect[0] - self.img.get_rect().center[0]
            rect[1] = rect[1] - self.img.get_rect().center[1]
        elif self.anchor == "N":
            rect[0] = rect[0] - self.img.get_rect().center[0]
        elif self.anchor == "S":
            rect[0] = rect[0] - self.img.get_rect().center[0]
            rect[1] = rect[1] - self.img.get_rect().midbottom[1]
        elif self.anchor == "W":
            rect[1] = rect[1] - self.img.get_rect().center[1]
        elif self.anchor == "E":
            rect[1] = rect[1] - self.img.get_rect().center[1]
            rect[0] = rect[0] - self.img.get_rect().right
        elif self.anchor == "NE":
            rect[0] = rect[0] - self.img.get_rect().right
        elif self.anchor == "SE":
            rect[0] = rect[0] - self.img.get_rect().right
            rect[1] = rect[1] - self.img.get_rect().midbottom[1]
        elif self.anchor == "SW":
            rect[1] = rect[1] - self.img.get_rect().midbottom[1]
        return tuple(rect)

    def render(self, screen):
        if self.visible:
            screen.blit(self.img, self.calculate_anchor())

    def reload_image(self):
        self.img = pygame.image.load(self.image_path).convert_alpha()