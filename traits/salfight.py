from random import randint

from classes.Collider import Collider
from random import randint

class SalFight:
    def __init__(self, entity, level):
        self.direction = -1 if randint(0, 1) == 0 else 1
        self.entity = entity
        self.collDetection = Collider(self.entity, level)
        self.speed = 1
        self.entity.vel.x = self.speed * self.direction
        self.level = level
        
    def update(self):
        if self.entity.rect.x > 1700:
            self.direction = -1
        if self.entity.rect.x < 1340:
            self.direction = 1
        if randint(0, 20) == 3:
            self.speed = randint(1, 3)
        self.entity.vel.x = self.speed * self.direction
        self.moveEntity()

    def moveEntity(self):
        self.entity.rect.y += self.entity.vel.y
        self.collDetection.checkY()
        self.entity.rect.x += self.entity.vel.x
        self.collDetection.checkX()
