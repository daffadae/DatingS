from scene import *
import utils

class GameScene(Scene):
    def __init__(self, screen):
        super().__init__("Game")
        self.screen = screen

        self.background_img = utils.image("Game", "Slide", 'assets/slides/1.jpg', (0, 0), anchor = "NW")
        self.order = 1
        self.option = None
        self.score = 0
    def render(self, screen):
        screen.fill((40,40,40))
        pass

    def process_input(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                print(f"Order: {self.order}\nScore: {self.score}")
                match self.order:
                    case 1:
                        self.background_img.image_path = 'assets/slides/2.jpg'
                        self.background_img.reload_image()
                    case 2:
                        self.background_img.image_path = 'assets/slides/3.jpg'
                        self.background_img.reload_image()
                    case 3:
                        self.background_img.image_path = 'assets/slides/4.jpg'
                        self.background_img.reload_image()
                    case 4:
                        self.background_img.image_path = 'assets/slides/5.jpg'
                        self.background_img.reload_image()
                    case 5:
                        self.background_img.image_path = 'assets/slides/6.jpg'
                        self.background_img.reload_image()
                    case 6:
                        self.background_img.image_path = 'assets/slides/7.jpg'
                        self.background_img.reload_image()
                    case 7:
                        self.background_img.image_path = 'assets/slides/8.jpg'
                        self.background_img.reload_image()
                    case 8:
                        self.background_img.image_path = 'assets/slides/9.jpg'
                        self.background_img.reload_image()
                    case 9:
                        self.background_img.image_path = 'assets/slides/10.jpg'
                        self.background_img.reload_image()
                    case 10:
                        self.background_img.image_path = 'assets/slides/11.jpg'
                        self.background_img.reload_image()
                    case 11:
                        self.background_img.image_path = 'assets/slides/12.jpg'
                        self.background_img.reload_image()
                    case 12:
                        self.background_img.image_path = 'assets/slides/13_(choices).jpg'
                        self.background_img.reload_image()
                    case 13:
                        option = None
                        if utils.check_bounds(mouse_pos, (24, 224, 758, 118)):
                            self.background_img.image_path = 'assets/slides/14.1.jpg'
                            self.background_img.reload_image()
                            self.score -= 1
                        elif utils.check_bounds(mouse_pos, (24, 366, 762, 122)):
                            self.background_img.image_path = 'assets/slides/14.2.1.jpg'
                            self.background_img.reload_image()
                            self.order = 99
                            self.score += 1
                        elif utils.check_bounds(mouse_pos, (24, 509, 764, 120)):
                            self.background_img.image_path = 'assets/slides/14.3.jpg'
                            self.background_img.reload_image()
                        else:
                            self.order -= 1
                    case 100:
                        self.background_img.image_path = 'assets/slides/14.2.2.jpg'
                        self.background_img.reload_image()
                        self.order = 13
                    case 14:
                        self.background_img.image_path = 'assets/slides/15.jpg'
                        self.background_img.reload_image()
                    case 15:
                        self.background_img.image_path = 'assets/slides/16.jpg'
                        self.background_img.reload_image()
                    case 16:
                        self.background_img.image_path = 'assets/slides/17.jpg'
                        self.background_img.reload_image()
                    case 17:
                        self.background_img.image_path = 'assets/slides/18.jpg'
                        self.background_img.reload_image()
                    case 18:
                        self.background_img.image_path = 'assets/slides/19.jpg'
                        self.background_img.reload_image()
                    case 19:
                        self.background_img.image_path = 'assets/slides/20.jpg'
                        self.background_img.reload_image()
                    case 20:
                        self.background_img.image_path = 'assets/slides/21.jpg'
                        self.background_img.reload_image()
                    case 21:
                        self.background_img.image_path = 'assets/slides/22.jpg'
                        self.background_img.reload_image()
                    case 22:
                        self.background_img.image_path = 'assets/slides/23_(choices).jpg'
                        self.background_img.reload_image()
                    case 23:
                        option = None
                        if utils.check_bounds(mouse_pos, (24, 224, 758, 118)):
                            self.background_img.image_path = 'assets/slides/24.1.jpg'
                            self.background_img.reload_image()
                            self.score -= 1
                        elif utils.check_bounds(mouse_pos, (24, 366, 762, 122)):
                            self.background_img.image_path = 'assets/slides/24.2.1.jpg'
                            self.background_img.reload_image()
                            self.order = 100
                            self.score += 1
                        elif utils.check_bounds(mouse_pos, (24, 509, 764, 120)):
                            self.background_img.image_path = 'assets/slides/24.3.1.jpg'
                            self.background_img.reload_image()
                            self.order = 101
                        else:
                            self.order -= 1
                    case 101:
                        self.background_img.image_path = 'assets/slides/24.2.2.jpg'
                        self.background_img.reload_image()
                        self.order = 23
                    case 102:
                        self.background_img.image_path = 'assets/slides/24.3.2.jpg'
                        self.background_img.reload_image()
                        self.order = 23
                    case 24:
                        self.background_img.image_path = 'assets/slides/25.jpg'
                        self.background_img.reload_image()
                    case 25:
                        self.background_img.image_path = 'assets/slides/26.jpg'
                        self.background_img.reload_image()
                    case 26:
                        self.background_img.image_path = 'assets/slides/27.jpg'
                        self.background_img.reload_image()
                    case 27:
                        self.background_img.image_path = 'assets/slides/28.jpg'
                        self.background_img.reload_image()
                    case 28:
                        self.background_img.image_path = 'assets/slides/29.jpg'
                        self.background_img.reload_image()
                    case 29:
                        self.background_img.image_path = 'assets/slides/30.jpg'
                        self.background_img.reload_image()
                    case 30:
                        self.background_img.image_path = 'assets/slides/31.jpg'
                        self.background_img.reload_image()
                    case 31:
                        self.background_img.image_path = 'assets/slides/32_(choices).jpg'
                        self.background_img.reload_image()
                    case 32:
                        option = None
                        if utils.check_bounds(mouse_pos, (24, 224, 758, 118)):
                            self.background_img.image_path = 'assets/slides/33.1.jpg'
                            self.background_img.reload_image()
                        elif utils.check_bounds(mouse_pos, (24, 366, 762, 122)):
                            self.background_img.image_path = 'assets/slides/33.2.1.jpg'
                            self.background_img.reload_image()
                            self.score += 1
                            self.order = 102
                        elif utils.check_bounds(mouse_pos, (24, 509, 764, 120)):
                            self.background_img.image_path = 'assets/slides/33.3.1.jpg'
                            self.background_img.reload_image()
                            self.score -= 1
                            self.order = 104
                        else:
                            self.order -= 1
                    case 103:
                        self.background_img.image_path = 'assets/slides/33.2.2.jpg'
                        self.background_img.reload_image()
                        self.order = 103
                    case 104:
                        self.background_img.image_path = 'assets/slides/33.2.3.jpg'
                        self.background_img.reload_image()
                        self.order = 32
                    case 105:
                        self.background_img.image_path = 'assets/slides/33.3.2.jpg'
                        self.background_img.reload_image()
                        self.order = 32
                    case 33:
                        self.background_img.image_path = 'assets/slides/34.jpg'
                        self.background_img.reload_image()
                    case 34:
                        self.background_img.image_path = 'assets/slides/35.jpg'
                        self.background_img.reload_image()
                    case 35:
                        self.background_img.image_path = 'assets/slides/36.jpg'
                        self.background_img.reload_image()
                    case 36:
                        self.background_img.image_path = 'assets/slides/37.jpg'
                        self.background_img.reload_image()
                    case 37:
                        self.background_img.image_path = 'assets/slides/38.jpg'
                        self.background_img.reload_image()
                    case 38:
                        self.background_img.image_path = 'assets/slides/39.jpg'
                        self.background_img.reload_image()
                    case 39:
                        self.background_img.image_path = 'assets/slides/40.jpg'
                        self.background_img.reload_image()
                    case 40:
                        self.background_img.image_path = 'assets/slides/41.jpg'
                        self.background_img.reload_image()
                    case 41:
                        self.background_img.image_path = 'assets/slides/42.jpg'
                        self.background_img.reload_image()
                    case 42:
                        self.background_img.image_path = 'assets/slides/43.jpg'
                        self.background_img.reload_image()
                    case 43:
                        self.background_img.image_path = 'assets/slides/44.jpg'
                        self.background_img.reload_image()
                    case 44:
                        self.background_img.image_path = 'assets/slides/45.jpg'
                        self.background_img.reload_image()
                    case 45:
                        self.background_img.image_path = 'assets/slides/46.jpg'
                        self.background_img.reload_image()
                    case 46:
                        self.background_img.image_path = 'assets/slides/47.jpg'
                        self.background_img.reload_image()
                    case 47:
                        self.background_img.image_path = 'assets/slides/48.jpg'
                        self.background_img.reload_image()
                    case 48:
                        self.background_img.image_path = 'assets/slides/49.jpg'
                        self.background_img.reload_image()
                    case 49:
                        if self.score == 0:
                            self.background_img.image_path = 'assets/slides/50_neutral.jpg'
                            self.background_img.reload_image()
                        if self.score < 1:
                            self.background_img.image_path = 'assets/slides/50_bad.jpg'
                            self.background_img.reload_image()
                        if self.score > 1:
                            self.background_img.image_path = 'assets/slides/50_good.jpg'
                            self.background_img.reload_image()
                        self.order = 150
                    
                self.order += 1