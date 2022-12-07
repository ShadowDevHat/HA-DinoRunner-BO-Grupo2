import random
import pygame
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.cactusLarge import CactusLarge
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.birdbb import BirdBB
from dino_runner.utils.constants import (LARGE_CACTUS, SMALL_CACTUS, BIRD) 

class ObstacleManage():
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            cactus_size = random.randint(0,5)
            if cactus_size == 0:
                self.obstacles.append(Cactus(SMALL_CACTUS))
            elif cactus_size == 3:
                self.obstacles.append(Bird(BIRD))
            elif cactus_size == 4:
                self.obstacles.append(BirdBB(BIRD))
            elif cactus_size == 5:
                self.obstacles.append(CactusLarge(LARGE_CACTUS))
        
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.dino.dinosaur_rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                game.playing = False
                break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)