import pygame, sys


class Game:
    def __init__(self) -> None:
        self.running = True
        pygame.init()
        self.screen_size: tuple = (1280, 720)
        self.screen = pygame.display.set_mode((self.screen_size[0], self.screen_size[1]))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Smart Rockets")
        
    def run(self):
        while self.running:
            self.screen.fill((0, 0, 0))
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            pygame.display.update()
            self.clock.tick(60) #60fps

Game().run()