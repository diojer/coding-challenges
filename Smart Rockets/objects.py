from imports import *

class Rocket:
    
    def __init__(self):
        self.velocity = Vector2
        self.acceleration = Vector2
        self.position = Vector2
        
    
    def applyForce(self, force):
        self.acceleration += force
    
    def update(self):
        self.velocity += self.acceleration
        self.position += self.velocity
        self.acceleration *= 0
        
    def getDirection(self):
        direction = self.velocity.normalize()
        return direction
    
    def show(self, screen: Surface):
        pygame.draw.line(screen, "white", (self.position), )
        