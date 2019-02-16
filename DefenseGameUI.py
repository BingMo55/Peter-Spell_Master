import pygame

_FRAME_RATE = 30
_INITIAL_WIDTH = 1024
_INITIAL_HEIGHT = 723
_BACKGROUND_COLOR = pygame.color(255,255,255)



class DefenseGameUI:
    def __init__(self):
        self._running = True
        self._state = None


    def run(self) -> None:
        pygame.init()

        try:
            clock = pygame.time.Clock()
            self.__create_surface((_INITITAL_WIDTH, _INITIAL_HEIGHT))

            while self._running:
                clock.tick(_FRAME_RATE)
        finally:
            pygame.quit()

    def _create_surface(self, size: (int, int)) -> None:
        self._surface = pygame.display.set_mode(size, pygame.RESIZABLE)

    def _draw_frame(self) -> None:
        self._surface.fill(_BACKGROUND_COLOR)
        pygame.display.flip()

    def _frac_x_to_pixel_x(self, frac_x: float) -> int:
        ''' Convert Fractional Coordinate of X to Pixel X Coordinate '''
        return self._frac_to_pixel(frac_x, self._surface.get_width())

    def _frac_x_to_pixel_x(self, frac_y: float) ->int:
        ''' Convert Fractional Coordinate of Y to Pixel Y Coordinate '''
        return self._frac_to_pixel(frac_y, self._surface.get_height())

    def _frac_to_pixel(self, frac: float, max_pixel: int) -> int:
        return int(frac*max_pixel)


if __name__ == '__main__':
    DefenseGameUI.run()
        
