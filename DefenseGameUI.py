import pygame
import DefenseGameState

_FRAME_RATE = 10
_INITIAL_WIDTH = 1024
_INITIAL_HEIGHT = 723
_BACKGROUND_COLOR = pygame.Color(255, 255, 255)

class DefenseGameUI:
    def __init__(self):
        self._running = True
        self._state = DefenseGameState.DefenseGameState()

        # Sprites
        self._state.loadZombie()

        # Images
        self.bg = pygame.image.load('images/background.png')
        self.castle = pygame.image.load('images/castle.png')
        self.mainMenuEnable = True
        self._zombieImages = [pygame.image.load('images/walk1.png'),\
                              pygame.image.load('images/walk2.png'),\
                              pygame.image.load('images/walk3.png'),\
                              pygame.image.load('images/walk4.png')]

        


    def run(self) -> None:
        pygame.init()

        try:
            clock = pygame.time.Clock()
            self._create_surface((_INITIAL_WIDTH, _INITIAL_HEIGHT))

            count = 0
            while self._running:
                clock.tick(_FRAME_RATE)
                if count % 50 == 0:
                    self._state.loadZombie()
                self._draw_frame()
                self._handle_events()
                count += 1
        finally:
            pygame.quit()

    def _handle_events(self) -> None:
        for event in pygame.event.get():
            self._handle_event(event)

    def _handle_event(self, event) -> None:
        if event.type == pygame.QUIT:
            self._running = False
        elif event.type == pygame.VIDEORESIZE:
            self._create_surface(event.size)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if self.mainMenuEnable:
                    self.mainMenuEnable = False
        elif event.type == pygame.KEYDOWN:
            stringKey = pygame.key.name(event.key)
            print(stringKey)



    def _create_surface(self, size: (int, int)) -> None:
        self._surface = pygame.display.set_mode(size)
        # resizing not implemented completely
        bg_x = self._frac_x_to_pixel_x(1024 / self._surface.get_width())
        bg_y = self._frac_y_to_pixel_y(750 / self._surface.get_height())
        
        self.bg = pygame.transform.scale(self.bg,(bg_x, bg_y))

        castle_x = 300 / self._surface.get_width()
        castle_y = 400 / self._surface.get_height()
        x = self._frac_x_to_pixel_x(castle_x)
        y = self._frac_y_to_pixel_y(castle_y)
        self.castle = pygame.transform.scale(self.castle, (x, y))
        

    def _draw_frame(self) -> None:
        if self.mainMenuEnable:
            self._draw_mainMenu()
        else:
            self._surface.blit(self.bg,(0,0))
            self._surface.blit(self.castle,(0,220))
            self._draw_zombies()
            pygame.display.flip()

    def _draw_zombies(self) -> None:
        for z in self._state.getZombies():
            self._draw_zombie(z)
  

    def _draw_zombie(self, z) -> None:
        zombie_x, zombie_y =  z.top_left()
        widthFrac = z.getWidth()
        heightFrac = z.getHeight()
        top_left_pixel_x = self._frac_x_to_pixel_x(zombie_x)
        top_left_pixel_y = self._frac_y_to_pixel_y(zombie_y)
        width_pixel = self._frac_x_to_pixel_x(widthFrac)
        height_pixel = self._frac_y_to_pixel_y(heightFrac)

        zombieRectangle = pygame.Rect(top_left_pixel_x, top_left_pixel_y, width_pixel, height_pixel)
        zombieImage = self._zombieImages[z.chooseImageIndex(self._zombieImages)]
        sendImage = pygame.transform.scale(zombieImage,(width_pixel, height_pixel))

        z.update()
        self._surface.blit(sendImage, zombieRectangle)

    def _frac_x_to_pixel_x(self, frac_x: float) -> int:
        ''' Convert Fractional Coordinate of X to Pixel X Coordinate '''
        return self._frac_to_pixel(frac_x, self._surface.get_width())

    def _frac_y_to_pixel_y(self, frac_y: float) ->int:
        ''' Convert Fractional Coordinate of Y to Pixel Y Coordinate '''
        return self._frac_to_pixel(frac_y, self._surface.get_height())

    def _frac_to_pixel(self, frac: float, max_pixel: int) -> int:
        return int(frac*max_pixel)

    def _draw_mainMenu(self):
        self._surface.fill(_BACKGROUND_COLOR)
        basicfont = pygame.font.SysFont(None, 48)
        text = basicfont.render('Space to start game!', True, (255, 0, 0), (255, 255, 255))
        textrect = text.get_rect()
        textrect.centerx = self._surface.get_rect().centerx
        textrect.centery = self._surface.get_rect().centery
        self._surface.blit(text, textrect)
        pygame.display.flip()

if __name__ == '__main__':
    DefenseGameUI().run()
