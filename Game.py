from Apple import * 
import arcade
import random

SPEED_X = 3.0
SPEED_Y = 3.0

APPLE_SPEED = 1.5

class Game(arcade.Window, arcade.Sprite):
    
    def __init__(self,width,height,title,color):
        super().__init__(width,height,title)
        arcade.set_background_color(color)

        self.width = width
        self.height = height

        self.player = None

    def setup(self):
        self.player_list = arcade.SpriteList()
        self.apple_list = arcade.SpriteList()
        self.player = arcade.SpriteCircle(30, arcade.color.GUPPIE_GREEN)
        self.player.center_x = 300
        self.player.center_y = 300

        self.player_list.append(self.player)

        self.apples()

        self.score = 0
        self.level = 1

    def apples(self):
        i = 0

        while i < 15:
            self.obs = Apple(15)
            self.apple_list.append(self.obs.apple)
            i += 1

        self.apple_movement()

    def on_draw(self):
        arcade.start_render()
        self.player_list.draw()
        self.apple_list.draw()

        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 15)

        output = f"Level: {self.level}"
        arcade.draw_text(output, 10, 35, arcade.color.WHITE, 15)


    def on_update(self, delta_time):
        self.player.update()
        self.apple_list.update()
        self.check_position_player()
        self.check_collision()
        self.check_apple_collision_with_edges()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.W:
            self.player.change_y = SPEED_Y
        elif key == arcade.key.S:
            self.player.change_y = -SPEED_Y
        elif key == arcade.key.D:
            self.player.change_x = SPEED_X
        elif key == arcade.key.A:
            self.player.change_x = -SPEED_X

    def on_key_release(self, key, modifiers):
        if key == arcade.key.W or key == arcade.key.S:
            self.player.change_y = 0
        elif key == arcade.key.A or key == arcade.key.D:
            self.player.change_x = 0

    def check_position_player(self):
        if self.player.center_x > WIDTH:
            self.player.center_x = 0

        elif self.player.center_y > HEIGHT:
            self.player.center_y = 0

        elif self.player.center_x < 0:
            self.player.center_x = WIDTH

        elif self.player.center_y < 0:
            self.player.center_y = HEIGHT

    def check_apple_collision_with_edges(self):
        for apple in self.apple_list:
            if apple.center_x > WIDTH or apple.center_x < 0:
                apple.change_x = -apple.change_x

            elif apple.center_y > HEIGHT or apple.center_y < 0:
                apple.change_y = -apple.change_y

    def apple_movement(self):
        for apple in self.apple_list:

            x = random.uniform(-APPLE_SPEED, APPLE_SPEED)
            y = random.uniform(-APPLE_SPEED, APPLE_SPEED)

            while -0.5 <= x < 0.5 or -0.5 <= y <= 0.5:
                x = random.uniform(-APPLE_SPEED, APPLE_SPEED)
                y = random.uniform(-APPLE_SPEED, APPLE_SPEED)

            apple.change_x = x
            apple.change_y = y

    def check_collision(self):
        for self.player in self.player_list:
            apples = arcade.check_for_collision_with_list(self.player, self.apple_list)

            for apple in apples:
                apple.remove_from_sprite_lists()
                self.score += 1

            if self.apple_list.__len__() == 0:
                self.level += 1
                self.apples()
                self.apple_list.draw()

def main():
    game = Game(WIDTH,HEIGHT,'Circle.io', arcade.color.ROSE)
    game.setup()
    arcade.run()

if __name__ == '__main__':
    main()