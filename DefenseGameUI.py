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

        # current method of choosing zombie = mod by 2 where 0=pink, 1=green
        self._nextZombie = 0
        self.mainMenuEnable = True


        # Images
        self.bg = pygame.image.load('images/background.png')
        self.castle = pygame.image.load('images/castle/castle.png')
        self.menubg = pygame.image.load('images/homeBackground.png')
        self.thunderCloud = pygame.image.load('images/thunder.png')
        self.textBox = pygame.image.load('images/rectangle.png')

        self._peterImages = [pygame.image.load('images/peter/peter1.png'), \
                       pygame.image.load('images/peter/peter2.png'),\
                       pygame.image.load('images/peter/peter3.png'), \
                       pygame.image.load('images/peter/peter4.png')]


        self._zombieImages = [pygame.image.load('images/walk1.png'),\
                              pygame.image.load('images/walk2.png'),\
                              pygame.image.load('images/walk3.png'),\
                              pygame.image.load('images/walk4.png')]

        self._greenZombieImages = [
                    pygame.image.load('images/green1.png'),\
                    pygame.image.load('images/green2.png'),\
                    pygame.image.load('images/green3.png'),\
                    pygame.image.load('images/green4.png')]
        #static menu animations init
        self.zombieSprite = staticZombieMovement()
        self.zombieStatic = pygame.sprite.Group(self.zombieSprite)

        self.peterSprite = staticPeterMovement()
        self.peterRotate = pygame.sprite.Group(self.peterSprite)


    def run(self) -> None:
        pygame.init()

        try:
            clock = pygame.time.Clock()
            self._create_surface((_INITIAL_WIDTH, _INITIAL_HEIGHT))

            count = 0
            while self._running:
                clock.tick(_FRAME_RATE)
                if not self.mainMenuEnable:
                    if count % 50 == 0:
                        self._state.loadZombie()
                        self._state._zombies[-1].zombieColor = self._nextZombie % 2
                        self._nextZombie += 1
                    self._state.zombieInvade()

                if self._state.isAlive():
                    self._draw_frame()
                    self._handle_events()
                    count += 1
                else:
                    self._running = False
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
            else:
                stringKey = pygame.key.name(event.key)
                self._state.check_character(stringKey)



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
            self._draw_cloud()
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

        # 0 = pink, 1 = green -> can make cleaner way of choosing zombies
        if z.zombieColor == 0:
            zombieImage = self._zombieImages[z.chooseImageIndex(self._zombieImages)]
        else:
            zombieImage = self._greenZombieImages[z.chooseImageIndex(self._greenZombieImages)]

        # can remove cuz zombies not scaling -> move to createsurface
        sendImage = pygame.transform.scale(zombieImage,(width_pixel, height_pixel))

        # WORD RECTANGLE
        # wordRectangle = pygame.Rect(top_left_pixel_x,top_left_pixel_y+20)
        self._draw_text(z,top_left_pixel_x,top_left_pixel_y)
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

        basicfont = pygame.font.Font("cheddar_jack.ttf", 48)
        word = "Press Spacebor to Begin"
        text = basicfont.render(word, True, (44, 78, 115))
        textrect = text.get_rect()
        textrect.centerx = self._surface.get_rect().centerx
        textrect.centery = self._surface.get_rect().centery+300
        self.menubg = pygame.transform.scale(self.menubg,(1024,723))
        self._surface.blit(self.menubg,(0,0))
        self._surface.blit(text, textrect)

        #animate static
        self.zombieStatic.update()
        self.zombieStatic.draw(self._surface)
        self.peterRotate.update()
        self.peterRotate.draw(self._surface)
        pygame.display.flip()

    def _draw_text(self,z,x,y):
        self.textBox = pygame.transform.scale(self.textBox, (170, 50))
        basicfont = pygame.font.Font("Poppins.ttf", 25)
        word = z.getWordProblem().word()
        text = basicfont.render(word, True, (0, 0, 0), (255,255,255))
        textrect = text.get_rect()
        textrect.centerx = x + 55
        textrect.centery = y - 30
        self._surface.blit(self.textBox, (x - 30, y - 55))
        self._surface.blit(text, textrect)

    def _draw_cloud(self):
        self.thunderCloud = pygame.transform.scale(self.thunderCloud, (310, 120))
        basicfont = pygame.font.Font("ARCADECLASSIC.ttf", 35)
        word = self._state._inputStr
        text = basicfont.render(word, True, (255, 255, 255))
        textrect = text.get_rect()
        textrect.centerx = self._surface.get_rect().centerx + 30
        textrect.centery = 150
        self._surface.blit(self.thunderCloud, (400,60))
        self._surface.blit(text, textrect)


class staticZombieMovement(pygame.sprite.Sprite):
    def __init__(self):
        super(staticZombieMovement, self).__init__()
        self.images = []
        self.images.append(pygame.image.load('images/walk1.png'))
        self.images.append(pygame.image.load('images/walk2.png'))
        self.images.append(pygame.image.load('images/walk3.png'))
        self.images.append(pygame.image.load('images/walk4.png'))
        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(700, 500, 50, 50)

    def update(self):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0

        self.image = self.images[self.index]
        self.image = pygame.transform.scale(self.image,(200,200))

class staticPeterMovement(pygame.sprite.Sprite):
    def __init__(self):
        super(staticPeterMovement,self).__init__()
        self.images = []
        self.images.append(pygame.image.load('images/peter/peter1.png'))
        self.images.append(pygame.image.load('images/peter/peter2.png'))
        self.images.append(pygame.image.load('images/peter/peter3.png'))
        self.images.append(pygame.image.load('images/peter/peter4.png'))
        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(120,550, 50, 50)

    def update(self):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0

        self.image = self.images[self.index]
        self.image = pygame.transform.scale(self.image, (150, 150))


if __name__ == '__main__':
    DefenseGameUI().run()
