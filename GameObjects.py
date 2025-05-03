import pygame
import random as rand

class Asteroid:
    def __init__(self, word, speed):
        self.word = word
        self.speed = speed
        self.asteroid_surface = pygame.transform.scale(pygame.image.load('Graphics/asteroid.png'), (100, 100)).convert_alpha()
        self.asteroid_surface.set_colorkey((255, 255, 255))
        self.asteroid_rect = self.asteroid_surface.get_rect()
        self.asteroid_text = pygame.font.Font(None, 50).render(word, True, "white")
        self.true_loc : list[float] = [0, 0]

    # Pick coordinates outside the screen for the asteroid to spawn
    # Then create rect for better blit
    def spawn(self):
        x = None
        y = None
        first = rand.randint(1,4)
        if first == 1:
            x = rand.randint(-100, 1380)
            y = 800
        elif first == 2:
            x = rand.randint(-100, 1380)
            y = -100
        elif first == 3:
            x = -100
            y = rand.randint(-100, 900)
        elif first == 4:
            x = 1380
            y = rand.randint(-100, 900)
        self.asteroid_rect = self.asteroid_surface.get_rect(center=(x, y))
        self.true_loc = [self.asteroid_rect.centerx, self.asteroid_rect.centery]
        asteroids.append(self)

    def explode(self):
        asteroids.remove(self)

asteroids: list[Asteroid] = []
hearts_dict: dict[pygame.Surface, pygame.Rect] = {}
class Scoreboard:
    def __init__(self, hearts):
        self.hearts = hearts
        self.full_hearts = hearts
        self.score = 0
        self.change_hearts(self.hearts, self.full_hearts)

    def change_hearts(self, hearts, full_hearts):
        hearts_dict.clear()
        self.full_hearts = full_hearts
        x = 980
        y = 50
        max_x = 1280
        for i in range(self.full_hearts):
            heart_surf = pygame.transform.scale(pygame.image.load('Graphics/Heart_Full.png'), (100, 100)).convert()
            heart_rect = heart_surf.get_rect(center=(x, y))
            hearts_dict[heart_surf] = heart_rect
            x += 110
            if x >= max_x:
                x = 980
                y += 50
        hearts -= full_hearts
        for i in range(hearts):
            heart_surf = pygame.transform.scale(pygame.image.load('Graphics/Empty_Heart.png'), (100, 100)).convert_alpha()
            heart_surf.set_colorkey((255, 255, 255))
            heart_rect = heart_surf.get_rect(center=(x, y))
            hearts_dict[heart_surf] = heart_rect
            x += 110
            if x >= max_x:
                x = 980
                y += 50