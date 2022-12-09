from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import DEFAULT_TYPE, BIRD


class Bird(Obstacle):

    def __init__(self, image):
        self.bird_run = {DEFAULT_TYPE: BIRD}
        self.type = 1
        super().__init__(image, self.type)
        self.rect.y = 325
        self.index = 0

    
    def draw(self, screen):
        if self.index >=9:
            self.index = 0
        screen.blit(self.image[self.index//5], self.rect)
        self.index +=1