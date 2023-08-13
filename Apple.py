import arcade
import random

HEIGHT = 600
WIDTH = 600

class Apple(arcade.Sprite):

    def __init__(self,radius):
        self.apple = arcade.SpriteCircle(radius, arcade.color.LAPIS_LAZULI)
        self.apple.center_x = random.randint(0,WIDTH)
        self.apple.center_y = random.randint(0,HEIGHT)