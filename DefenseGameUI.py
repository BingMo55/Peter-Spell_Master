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
        self.my_sprite = self._state.zombie()
        self.my_group = pygame.sprite.Group(self.my_sprite)

        # Images
        self._zombieImages = [pygame.image.load('images/walk1.png'),\
                              pygame.image.load('images/walk2.png'),\
                              pygame.image.load('images/walk3.png'),\
                              pygame.image.load('images/walk4.png')]


    def run(self) -> None:
        pygame.init()

        try:
            clock = pygame.time.Clock()
            self._create_surface((_INITIAL_WIDTH, _INITIAL_HEIGHT))

            while self._running:
                clock.tick(_FRAME_RATE)
                self._draw_frame()
                self._handle_events()
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

    def _create_surface(self, size: (int, int)) -> None:
        self._surface = pygame.display.set_mode(size, pygame.RESIZABLE)

    def _draw_frame(self) -> None:
        self._surface.fill(_BACKGROUND_COLOR)
        self._draw_zombie()
        self.my_group.draw(self._surface)
        pygame.display.flip()



    def _draw_zombie(self) -> None:
        zombie_x, zombie_y =  self._state.zombie().top_left()
        widthFrac = self._state.zombie().getWidth()
        heightFrac = self._state.zombie().getHeight()
        top_left_pixel_x = self._frac_x_to_pixel_x(zombie_x)
        top_left_pixel_y = self._frac_y_to_pixel_y(zombie_y)
        width_pixel = self._frac_x_to_pixel_x(widthFrac)
        height_pixel = self._frac_y_to_pixel_y(heightFrac)

        zombieRectangle = pygame.Rect(top_left_pixel_x, top_left_pixel_y, width_pixel, height_pixel)
        zombieImage = self._zombieImages[self._state.zombie().chooseImageIndex(self._zombieImages)]
        sendImage = pygame.transform.scale(zombieImage,(width_pixel, height_pixel))

        self.my_group.update(sendImage, zombieRectangle, top_left_pixel_x)


    def _frac_x_to_pixel_x(self, frac_x: float) -> int:
        ''' Convert Fractional Coordinate of X to Pixel X Coordinate '''
        return self._frac_to_pixel(frac_x, self._surface.get_width())

    def _frac_y_to_pixel_y(self, frac_y: float) ->int:
        ''' Convert Fractional Coordinate of Y to Pixel Y Coordinate '''
        return self._frac_to_pixel(frac_y, self._surface.get_height())

    def _frac_to_pixel(self, frac: float, max_pixel: int) -> int:
        return int(frac*max_pixel)


if __name__ == '__main__':
    DefenseGameUI().run()
