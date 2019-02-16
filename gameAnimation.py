import pygame

_ZOMBIE_SPEED = 0.01
_ZOMBIE_WIDTH = 0.10
_ZOMBIE_HEIGHT = 0.10
_x = 50
_y = 0


class Zombie(pygame.sprite.Sprite):
    def __init__(self):
        super(Zombie, self).__init__()
        self._width = _ZOMBIE_WIDTH
        self._height = _ZOMBIE_HEIGHT
        self._speed = _ZOMBIE_SPEED
        self.top_left_x = 1 - self._width / 2
        self.top_left_y = 0.7 - self._height / 2
        self._word = None
        self.images = []
        self.images.append(pygame.image.load('images/walk1.jpg'))
        self.images.append(pygame.image.load('images/walk2.jpg'))
        self.images.append(pygame.image.load('images/walk3.jpg'))
        self.images.append(pygame.image.load('images/walk4.jpg'))
        self.index = 0
        self.image = self.images[self.index]
        self._x = 1000

    def update(self):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0

        self.image = self.images[self.index]
        global _x
        self._x -= _x
        if self._x < 0:
            self._x = 1000
        self.rect = pygame.Rect(self._x, _y, self._width, self._height)

    def top_left(self) -> (float, float):
        ''' Return Position of the zombie in a tuple '''
        return (self.top_left_x, self.top_left_y)

    def getWidth(self) -> float:
        ''' Get Width '''
        return self._width

    def getHeight(self) -> float:
        ''' Get Height '''
        return self._height

    def getWord(self) -> str:
        ''' Get Word '''
        return self._word

    def move_left(self) -> None:
        ''' Zombie Move to Left '''
        self._move(-self._speed)

    def changeSpeed(self, newSpeed):
        ''' Change Speed '''
        self._speed = newSpeed

    def changeWord(self, newWord):
        ''' Change Word '''
        self._word = newWord

    def _move(self, delta_x: float) -> None:
        ''' Zombie Move (Private Function)'''
        tl_x = self.top_left_x
        new_x = tl_x + delta_x
        self.top_left_x = new_x


def _frac_x_to_pixel_x(self, frac_x: float) -> int:
    ''' Convert Fractional Coordinate of X to Pixel X Coordinate '''
    return frac_to_pixel(frac_x, self._surface.get_width())


def _frac_y_to_pixel_y(self, frac_y: float) -> int:
    ''' Convert Fractional Coordinate of Y to Pixel Y Coordinate '''
    return frac_to_pixel(frac_y, self._surface.get_height())


def _frac_to_pixel(self, frac: float, max_pixel: int) -> int:
    return int(frac * max_pixel)


# x = Zombie()
#
# print(x.getWidth())
def main():
    pygame.init()  # init pygame
    screen = pygame.display.set_mode((1024, 768))
    my_sprite = Zombie()
    my_group = pygame.sprite.Group(my_sprite)  # create group
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        my_group.update()  # call sprite's update

        screen.fill((255, 255, 255))

        my_group.draw(screen)  # draw sprite onto screen
        pygame.display.update()  # update screen
        clock.tick(10)


if __name__ == '__main__':
    main()

