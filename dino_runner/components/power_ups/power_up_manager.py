from dino_runner.components.power_ups.shield import Shield
import random
import pygame

class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.points = 0
        self.when_appears = 0
        self.sound_run = pygame.mixer.Sound("sounds/run.mp3")


    def update(self, points, game_speed, player):
        self.generate_power_ups(points)
        for power_up in self.power_ups:
            power_up.update(game_speed, self.power_ups)
            if(player.dinosaur_rect.colliderect(power_up.rect)):
                power_up.start_time = pygame.time.get_ticks()
                player.shield = True

                self.sound_run.play()
                
                player.type = power_up.type 
                power_up.star_time = pygame.time.get_ticks()
                time_random = random.randrange(5,8)
                player.shiel_time_up = power_up.start_time + (time_random * 1000)


                if player.shiel_time_up <= 0:
                    self.sound_run.stop()
                self.power_ups.remove(power_up)
                
               
                

    def generate_power_ups(self, points):
        self.points = points
        
            
        if len(self.power_ups) == 0:
            if self.when_appears == self.points:
                self.when_appears = random.randint(self.when_appears+200, self.when_appears +500)
                self.power_ups.append(Shield())
                
    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset_power_up(self, points):
        self.power_ups = []
        self.points = points
        self.when_appears = random.randint(200, 300) + self.points