import arcade

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 750
MOVEMENT_SPEED = 5
DEAD_ZONE = 0.02

def TREE(x, y, Black, DarkGreen, HalfDarkGreen, HalfLightGreen, LightGreen, DarkBrown, LightBrown):
    """Draw the silhouette"""
    arcade.draw_point(x, y + 340, Black, 20)
    arcade.draw_point(x, y + 320, Black, 20)
    arcade.draw_point(x, y + 300, Black, 20)
    arcade.draw_point(x, y + 280, Black, 20)
    arcade.draw_point(x + 20, y + 360, Black, 20)
    arcade.draw_point(x + 40, y + 360, Black, 20)
    arcade.draw_point(x + 40, y + 380, Black, 20)
    arcade.draw_point(x + 40, y + 400, Black, 20)
    arcade.draw_point(x + 40, y + 420, Black, 20)
    arcade.draw_point(x + 60, y + 440, Black, 20)
    arcade.draw_point(x + 80, y + 440, Black, 20)
    arcade.draw_point(x + 100, y + 440, Black, 20)
    arcade.draw_point(x + 120, y + 460, Black, 20)
    arcade.draw_point(x + 140, y + 460, Black, 20)
    arcade.draw_point(x + 160, y + 460, Black, 20)
    arcade.draw_point(x + 180, y + 460, Black, 20)
    arcade.draw_point(x + 200, y + 440, Black, 20)
    arcade.draw_point(x + 200, y + 420, Black, 20)
    arcade.draw_point(x + 220, y + 420, Black, 20)
    arcade.draw_point(x + 240, y + 440, Black, 20)
    arcade.draw_point(x + 260, y + 440, Black, 20)
    arcade.draw_point(x + 280, y + 440, Black, 20)
    arcade.draw_point(x + 300, y + 440, Black, 20)
    arcade.draw_point(x + 320, y + 420, Black, 20)
    arcade.draw_point(x + 320, y + 400, Black, 20)
    arcade.draw_point(x + 340, y + 380, Black, 20)
    arcade.draw_point(x + 340, y + 360, Black, 20)
    arcade.draw_point(x + 340, y + 340, Black, 20)
    arcade.draw_point(x + 340, y + 320, Black, 20)
    arcade.draw_point(x + 360, y + 300, Black, 20)
    arcade.draw_point(x + 360, y + 280, Black, 20)
    arcade.draw_point(x + 360, y + 260, Black, 20)
    arcade.draw_point(x + 360, y + 240, Black, 20)
    arcade.draw_point(x + 340, y + 220, Black, 20)
    arcade.draw_point(x + 340, y + 200, Black, 20)
    arcade.draw_point(x + 320, y + 180, Black, 20)
    arcade.draw_point(x + 300, y + 180, Black, 20)
    arcade.draw_point(x + 280, y + 160, Black, 20)
    arcade.draw_point(x + 260, y + 160, Black, 20)
    arcade.draw_point(x + 240, y + 160, Black, 20)
    arcade.draw_point(x + 220, y + 140, Black, 20)
    arcade.draw_point(x + 220, y + 120, Black, 20)
    arcade.draw_point(x + 220, y + 100, Black, 20)
    arcade.draw_point(x + 240, y + 80, Black, 20)
    arcade.draw_point(x + 240, y + 60, Black, 20)
    arcade.draw_point(x + 240, y + 40, Black, 20)
    arcade.draw_point(x + 20, y + 260, Black, 20)
    arcade.draw_point(x + 40, y + 240, Black, 20)
    arcade.draw_point(x + 40, y + 220, Black, 20)
    arcade.draw_point(x + 40, y + 200, Black, 20)
    arcade.draw_point(x + 60, y + 180, Black, 20)
    arcade.draw_point(x + 80, y + 180, Black, 20)
    arcade.draw_point(x + 100, y + 160, Black, 20)
    arcade.draw_point(x + 120, y + 160, Black, 20)
    arcade.draw_point(x + 140, y + 140, Black, 20)
    arcade.draw_point(x + 140, y + 120, Black, 20)
    arcade.draw_point(x + 140, y + 100, Black, 20)
    arcade.draw_point(x + 140, y + 80, Black, 20)
    arcade.draw_point(x + 140, y + 60, Black, 20)
    arcade.draw_point(x + 120, y + 40, Black, 20)
    arcade.draw_point(x + 160, y + 160, Black, 20)
    arcade.draw_point(x + 180, y + 160, Black, 20)
    arcade.draw_point(x + 200, y + 20, Black, 20)
    arcade.draw_point(x + 220, y + 20, Black, 20)
    arcade.draw_point(x + 240, y, Black, 20)
    arcade.draw_point(x + 260, y, Black, 20)
    arcade.draw_point(x + 280, y + 20, Black, 20)
    arcade.draw_point(x + 260, y + 40, Black, 20)
    arcade.draw_point(x + 280, y, Black, 20)
    arcade.draw_point(x + 180, y, Black, 20)
    arcade.draw_point(x + 160, y + 20, Black, 20)
    arcade.draw_point(x + 140, y + 20, Black, 20)
    arcade.draw_point(x + 100, y + 20, Black, 20)
    arcade.draw_point(x + 100, y, Black, 20)
    arcade.draw_point(x + 120, y, Black, 20)
    """Draw the colors"""
    arcade.draw_point(x + 20, y + 300, DarkGreen, 20)
    arcade.draw_point(x + 20, y + 320, DarkGreen, 20)
    arcade.draw_point(x + 20, y + 280, HalfDarkGreen, 20)
    arcade.draw_point(x + 20, y + 340, HalfDarkGreen, 20)
    arcade.draw_point(x + 40, y + 340, HalfDarkGreen, 20)
    arcade.draw_point(x + 40, y + 320, HalfDarkGreen, 20)
    arcade.draw_point(x + 40, y + 300, HalfDarkGreen, 20)
    arcade.draw_point(x + 40, y + 280, HalfDarkGreen, 20)
    arcade.draw_point(x + 40, y + 260, DarkGreen, 20)
    arcade.draw_point(x + 60, y + 340, HalfLightGreen, 20)
    arcade.draw_point(x + 60, y + 320, HalfLightGreen, 20)
    arcade.draw_point(x + 60, y + 360, HalfLightGreen, 20)
    arcade.draw_point(x + 80, y + 360, HalfLightGreen, 20)
    arcade.draw_point(x + 100, y + 360, HalfLightGreen, 20)
    arcade.draw_point(x + 80, y + 320, HalfLightGreen, 20)
    arcade.draw_point(x + 80, y + 340, HalfLightGreen, 20)
    arcade.draw_point(x + 100, y + 340, HalfLightGreen, 20)
    arcade.draw_point(x + 100, y + 320, HalfLightGreen, 20)
    arcade.draw_point(x + 100, y + 300, HalfLightGreen, 20)
    arcade.draw_point(x + 80, y + 300, HalfDarkGreen, 20)
    arcade.draw_point(x + 60, y + 300, HalfDarkGreen, 20)
    arcade.draw_point(x + 60, y + 280, HalfDarkGreen, 20)
    arcade.draw_point(x + 60, y + 260, HalfDarkGreen, 20)
    arcade.draw_point(x + 60, y + 240, DarkGreen, 20)
    arcade.draw_point(x + 60, y + 220, DarkGreen, 20)
    arcade.draw_point(x + 60, y + 200, DarkGreen, 20)
    arcade.draw_point(x + 60, y + 380, HalfDarkGreen, 20)
    arcade.draw_point(x + 60, y + 400, HalfDarkGreen, 20)
    arcade.draw_point(x + 60, y + 420, HalfLightGreen, 20)
    arcade.draw_point(x + 80, y + 420, HalfLightGreen, 20)
    arcade.draw_point(x + 100, y + 420, HalfLightGreen, 20)
    arcade.draw_point(x + 120, y + 400, HalfLightGreen, 20)
    arcade.draw_point(x + 120, y + 420, HalfLightGreen, 20)
    arcade.draw_point(x + 120, y + 440, HalfLightGreen, 20)
    arcade.draw_point(x + 140, y + 440, HalfLightGreen, 20)
    arcade.draw_point(x + 140, y + 420, HalfLightGreen, 20)
    arcade.draw_point(x + 160, y + 420, HalfLightGreen, 20)
    arcade.draw_point(x + 180, y + 420, LightGreen, 20)
    arcade.draw_point(x + 180, y + 440, LightGreen, 20)
    arcade.draw_point(x + 160, y + 440, LightGreen, 20)
    arcade.draw_point(x + 100, y + 400, HalfDarkGreen, 20)
    arcade.draw_point(x + 80, y + 400, HalfDarkGreen, 20)
    arcade.draw_point(x + 140, y + 400, HalfDarkGreen, 20)
    arcade.draw_point(x + 100, y + 380, HalfDarkGreen, 20)
    arcade.draw_point(x + 80, y + 380, HalfDarkGreen, 20)
    arcade.draw_point(x + 120, y + 380, HalfDarkGreen, 20)
    arcade.draw_point(x + 140, y + 380, HalfDarkGreen, 20)
    arcade.draw_point(x + 160, y + 380, HalfDarkGreen, 20)
    arcade.draw_point(x + 160, y + 400, HalfDarkGreen, 20)
    arcade.draw_point(x + 160, y + 360, HalfDarkGreen, 20)
    arcade.draw_point(x + 140, y + 360, LightGreen, 20)
    arcade.draw_point(x + 140, y + 340, LightGreen, 20)
    arcade.draw_point(x + 120, y + 360, LightGreen, 20)
    arcade.draw_point(x + 120, y + 340, HalfLightGreen, 20)
    arcade.draw_point(x + 160, y + 340, HalfLightGreen, 20)
    arcade.draw_point(x + 160, y + 320, HalfLightGreen, 20)
    arcade.draw_point(x + 140, y + 320, HalfLightGreen, 20)
    arcade.draw_point(x + 120, y + 320, HalfLightGreen, 20)
    arcade.draw_point(x + 120, y + 300, HalfLightGreen, 20)
    arcade.draw_point(x + 120, y + 280, HalfDarkGreen, 20)
    arcade.draw_point(x + 100, y + 280, HalfDarkGreen, 20)
    arcade.draw_point(x + 80, y + 280, HalfDarkGreen, 20)
    arcade.draw_point(x + 80, y + 260, HalfDarkGreen, 20)
    arcade.draw_point(x + 80, y + 240, HalfDarkGreen, 20)
    arcade.draw_point(x + 80, y + 220, DarkGreen, 20)
    arcade.draw_point(x + 80, y + 200, DarkGreen, 20)
    arcade.draw_point(x + 100, y + 180, DarkGreen, 20)
    arcade.draw_point(x + 100, y + 200, DarkGreen, 20)
    arcade.draw_point(x + 100, y + 180, DarkGreen, 20)
    arcade.draw_point(x + 100, y + 220, HalfDarkGreen, 20)
    arcade.draw_point(x + 120, y + 220, DarkGreen, 20)
    arcade.draw_point(x + 120, y + 200, DarkGreen, 20)
    arcade.draw_point(x + 120, y + 180, DarkGreen, 20)
    arcade.draw_point(x + 140, y + 180, DarkGreen, 20)
    arcade.draw_point(x + 140, y + 160, DarkGreen, 20)
    arcade.draw_point(x + 140, y + 200, DarkGreen, 20)
    arcade.draw_point(x + 140, y + 220, DarkGreen, 20)
    arcade.draw_point(x + 160, y + 200, DarkGreen, 20)
    arcade.draw_point(x + 160, y + 180, DarkGreen, 20)
    arcade.draw_point(x + 160, y + 220, HalfDarkGreen, 20)
    arcade.draw_point(x + 180, y + 180, DarkGreen, 20)
    arcade.draw_point(x + 180, y + 200, DarkGreen, 20)
    arcade.draw_point(x + 180, y + 220, DarkGreen, 20)
    arcade.draw_point(x + 180, y + 240, DarkGreen, 20)
    arcade.draw_point(x + 160, y + 240, DarkGreen, 20)
    arcade.draw_point(x + 200, y + 200, DarkGreen, 20)
    arcade.draw_point(x + 200, y + 220, DarkGreen, 20)
    arcade.draw_point(x + 200, y + 180, DarkGreen, 20)
    arcade.draw_point(x + 200, y + 160, DarkGreen, 20)
    arcade.draw_point(x + 220, y + 160, DarkGreen, 20)
    arcade.draw_point(x + 220, y + 180, DarkGreen, 20)
    arcade.draw_point(x + 220, y + 200, DarkGreen, 20)
    arcade.draw_point(x + 220, y + 220, DarkGreen, 20)
    arcade.draw_point(x + 240, y + 220, DarkGreen, 20)
    arcade.draw_point(x + 240, y + 200, DarkGreen, 20)
    arcade.draw_point(x + 240, y + 180, DarkGreen, 20)
    arcade.draw_point(x + 260, y + 180, DarkGreen, 20)
    arcade.draw_point(x + 260, y + 200, DarkGreen, 20)
    arcade.draw_point(x + 280, y + 200, DarkGreen, 20)
    arcade.draw_point(x + 280, y + 180, DarkGreen, 20)
    arcade.draw_point(x + 280, y + 220, DarkGreen, 20)
    arcade.draw_point(x + 300, y + 220, DarkGreen, 20)
    arcade.draw_point(x + 300, y + 200, DarkGreen, 20)
    arcade.draw_point(x + 320, y + 200, DarkGreen, 20)
    arcade.draw_point(x + 320, y + 220, DarkGreen, 20)
    arcade.draw_point(x + 340, y + 240, DarkGreen, 20)
    arcade.draw_point(x + 320, y + 240, HalfDarkGreen, 20)
    arcade.draw_point(x + 300, y + 240, HalfDarkGreen, 20)
    arcade.draw_point(x + 280, y + 240, HalfDarkGreen, 20)
    arcade.draw_point(x + 260, y + 240, HalfDarkGreen, 20)
    arcade.draw_point(x + 260, y + 220, HalfDarkGreen, 20)
    arcade.draw_point(x + 240, y + 240, HalfDarkGreen, 20)
    arcade.draw_point(x + 220, y + 240, HalfDarkGreen, 20)
    arcade.draw_point(x + 200, y + 240, HalfDarkGreen, 20)
    arcade.draw_point(x + 140, y + 240, HalfDarkGreen, 20)
    arcade.draw_point(x + 120, y + 240, HalfDarkGreen, 20)
    arcade.draw_point(x + 100, y + 240, HalfDarkGreen, 20)
    arcade.draw_point(x + 100, y + 260, HalfDarkGreen, 20)
    arcade.draw_point(x + 120, y + 260, HalfDarkGreen, 20)
    arcade.draw_point(x + 140, y + 260, HalfDarkGreen, 20)
    arcade.draw_point(x + 160, y + 260, HalfDarkGreen, 20)
    arcade.draw_point(x + 180, y + 260, HalfDarkGreen, 20)
    arcade.draw_point(x + 200, y + 260, HalfDarkGreen, 20)
    arcade.draw_point(x + 220, y + 260, HalfDarkGreen, 20)
    arcade.draw_point(x + 240, y + 260, HalfDarkGreen, 20)
    arcade.draw_point(x + 260, y + 260, HalfDarkGreen, 20)
    arcade.draw_point(x + 280, y + 260, HalfDarkGreen, 20)
    arcade.draw_point(x + 300, y + 260, HalfDarkGreen, 20)
    arcade.draw_point(x + 320, y + 260, HalfDarkGreen, 20)
    arcade.draw_point(x + 340, y + 260, HalfDarkGreen, 20)
    arcade.draw_point(x + 340, y + 280, HalfLightGreen, 20)
    arcade.draw_point(x + 340, y + 300, HalfLightGreen, 20)
    arcade.draw_point(x + 320, y + 280, HalfDarkGreen, 20)
    arcade.draw_point(x + 300, y + 280, HalfDarkGreen, 20)
    arcade.draw_point(x + 320, y + 300, HalfDarkGreen, 20)
    arcade.draw_point(x + 300, y + 300, HalfDarkGreen, 20)
    arcade.draw_point(x + 280, y + 300, HalfLightGreen, 20)
    arcade.draw_point(x + 280, y + 280, HalfDarkGreen, 20)
    arcade.draw_point(x + 260, y + 280, HalfDarkGreen, 20)
    arcade.draw_point(x + 240, y + 280, HalfDarkGreen, 20)
    arcade.draw_point(x + 220, y + 280, HalfDarkGreen, 20)
    arcade.draw_point(x + 200, y + 280, HalfDarkGreen, 20)
    arcade.draw_point(x + 180, y + 280, HalfDarkGreen, 20)
    arcade.draw_point(x + 160, y + 280, HalfDarkGreen, 20)
    arcade.draw_point(x + 140, y + 280, HalfDarkGreen, 20)
    arcade.draw_point(x + 140, y + 300, HalfDarkGreen, 20)
    arcade.draw_point(x + 160, y + 300, HalfDarkGreen, 20)
    arcade.draw_point(x + 180, y + 300, HalfDarkGreen, 20)
    arcade.draw_point(x + 200, y + 300, HalfDarkGreen, 20)
    arcade.draw_point(x + 220, y + 300, HalfDarkGreen, 20)
    arcade.draw_point(x + 240, y + 300, HalfLightGreen, 20)
    arcade.draw_point(x + 260, y + 300, HalfLightGreen, 20)
    arcade.draw_point(x + 260, y + 320, HalfLightGreen, 20)
    arcade.draw_point(x + 280, y + 320, LightGreen, 20)
    arcade.draw_point(x + 300, y + 320, LightGreen, 20)
    arcade.draw_point(x + 240, y + 320, HalfLightGreen, 20)
    arcade.draw_point(x + 220, y + 320, HalfLightGreen, 20)
    arcade.draw_point(x + 200, y + 320, HalfDarkGreen, 20)
    arcade.draw_point(x + 180, y + 320, HalfDarkGreen, 20)
    arcade.draw_point(x + 180, y + 340, HalfDarkGreen, 20)
    arcade.draw_point(x + 180, y + 360, HalfDarkGreen, 20)
    arcade.draw_point(x + 180, y + 380, HalfDarkGreen, 20)
    arcade.draw_point(x + 180, y + 400, HalfDarkGreen, 20)
    arcade.draw_point(x + 200, y + 400, HalfDarkGreen, 20)
    arcade.draw_point(x + 200, y + 380, HalfLightGreen, 20)
    arcade.draw_point(x + 200, y + 360, HalfDarkGreen, 20)
    arcade.draw_point(x + 200, y + 340, HalfDarkGreen, 20)
    arcade.draw_point(x + 220, y + 340, HalfDarkGreen, 20)
    arcade.draw_point(x + 220, y + 360, HalfDarkGreen, 20)
    arcade.draw_point(x + 220, y + 380, HalfDarkGreen, 20)
    arcade.draw_point(x + 220, y + 400, HalfDarkGreen, 20)
    arcade.draw_point(x + 240, y + 340, HalfLightGreen, 20)
    arcade.draw_point(x + 260, y + 340, LightGreen, 20)
    arcade.draw_point(x + 280, y + 340, LightGreen, 20)
    arcade.draw_point(x + 300, y + 340, HalfDarkGreen, 20)
    arcade.draw_point(x + 320, y + 340, HalfDarkGreen, 20)
    arcade.draw_point(x + 320, y + 320, HalfDarkGreen, 20)
    arcade.draw_point(x + 320, y + 360, HalfDarkGreen, 20)
    arcade.draw_point(x + 300, y + 360, HalfDarkGreen, 20)
    arcade.draw_point(x + 280, y + 360, HalfDarkGreen, 20)
    arcade.draw_point(x + 260, y + 360, HalfDarkGreen, 20)
    arcade.draw_point(x + 240, y + 360, HalfDarkGreen, 20)
    arcade.draw_point(x + 240, y + 380, HalfDarkGreen, 20)
    arcade.draw_point(x + 260, y + 380, HalfDarkGreen, 20)
    arcade.draw_point(x + 280, y + 380, HalfLightGreen, 20)
    arcade.draw_point(x + 300, y + 380, HalfLightGreen, 20)
    arcade.draw_point(x + 320, y + 380, HalfLightGreen, 20)
    arcade.draw_point(x + 260, y + 400, HalfLightGreen, 20)
    arcade.draw_point(x + 240, y + 400, HalfLightGreen, 20)
    arcade.draw_point(x + 240, y + 420, HalfLightGreen, 20)
    arcade.draw_point(x + 260, y + 420, LightGreen, 20)
    arcade.draw_point(x + 280, y + 420, LightGreen, 20)
    arcade.draw_point(x + 300, y + 420, LightGreen, 20)
    arcade.draw_point(x + 300, y + 400, LightGreen, 20)
    arcade.draw_point(x + 280, y + 400, LightGreen, 20)
    """Bark"""
    arcade.draw_point(x + 180, y + 40, LightBrown, 20)
    arcade.draw_point(x + 140, y + 40, DarkBrown, 20)
    arcade.draw_point(x + 160, y + 40, DarkBrown, 20)
    arcade.draw_point(x + 160, y + 60, DarkBrown, 20)
    arcade.draw_point(x + 160, y + 80, DarkBrown, 20)
    arcade.draw_point(x + 180, y + 60, DarkBrown, 20)
    arcade.draw_point(x + 220, y + 80, DarkBrown, 20)
    arcade.draw_point(x + 200, y + 80, LightBrown, 20)
    arcade.draw_point(x + 180, y + 80, LightBrown, 20)
    arcade.draw_point(x + 200, y + 60, LightBrown, 20)
    arcade.draw_point(x + 220, y + 60, LightBrown, 20)
    arcade.draw_point(x + 220, y + 40, LightBrown, 20)
    arcade.draw_point(x + 200, y + 40, LightBrown, 20)
    arcade.draw_point(x + 160, y + 100, LightBrown, 20)
    arcade.draw_point(x + 180, y + 100, LightBrown, 20)
    arcade.draw_point(x + 200, y + 100, LightBrown, 20)
    arcade.draw_point(x + 180, y + 120, LightBrown, 20)
    arcade.draw_point(x + 200, y + 120, LightBrown, 20)
    arcade.draw_point(x + 160, y + 120, DarkBrown, 20)
    arcade.draw_point(x + 160, y + 140, DarkBrown, 20)
    arcade.draw_point(x + 180, y + 140, DarkBrown, 20)
    arcade.draw_point(x + 200, y + 140, DarkBrown, 20)
    arcade.draw_point(x + 120, y + 20, DarkBrown, 20)
    arcade.draw_point(x + 180, y + 20, LightBrown, 20)
    arcade.draw_point(x + 240, y + 20, LightBrown, 20)
    arcade.draw_point(x + 260, y + 20, LightBrown, 20)

class Tree:
    def __init__(self):
        self.x = 20
        self.y = 20
        self.changeX = 0
        self.changeY = 0

    def update(self):
        # Move the ball
        self.x += self.changeX
        self.y += self.changeY

class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self):
        """ Initializer """

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")
        arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)

        #Hide the mouse
        self.set_mouse_visible(False)

        # Get a list of all the game controllers that are plugged in
        joysticks = arcade.get_joysticks()

        # If we have a game controller plugged in, grab it and
        # make an instance variable out of it.
        if joysticks:
            self.joystick = joysticks[0]
            self.joystick.open()
        else:
            print("There are no joysticks.")
            self.joystick = None

        #THREE TREES
        self.tree1 = Tree()
        self.tree2 = Tree()
        self.tree3 = Tree()

    def on_draw(self):
        arcade.start_render()
        TREE(self.tree1.x, self.tree1.y, arcade.color.BLACK, arcade.color.CASTLETON_GREEN, arcade.color.AO, arcade.color.FOREST_GREEN, arcade.color.DARK_PASTEL_GREEN, arcade.color.BROWN_NOSE, arcade.color.COCONUT)
        TREE(self.tree2.x, self.tree2.y, arcade.color.BLACK, arcade.color.PURPLE, arcade.color.DARK_VIOLET, arcade.color.VIVID_VIOLET, arcade.color.BRIGHT_LILAC, arcade.color.BROWN_NOSE, arcade.color.COCONUT)
        TREE(self.tree3.x, self.tree3.y, arcade.color.AMETHYST, arcade.color.BLUEBONNET, arcade.color.BRANDEIS_BLUE, arcade.color.COLUMBIA_BLUE, arcade.color.BRIGHT_TURQUOISE, arcade.color.DARK_ORCHID, arcade.color.DEEP_MAGENTA)

    def on_mouse_motion(self, x, y, dx, dy):
        """ Called to update our objects.
        Happens approximately 60 times per second."""
        self.tree1.x = x
        self.tree1.y = y


    def update(self, delta_time):
        self.tree2.update()

        # Update the position according to the game controller
        if self.joystick:
            # Set a "dead zone" to prevent drive from a centered joystick
            if abs(self.joystick.x) < DEAD_ZONE:
                self.tree3.changeX = 0
            else:
                self.tree3.changeX = self.joystick.x * MOVEMENT_SPEED

            # Set a "dead zone" to prevent drive from a centered joystick
            if abs(self.joystick.y) < DEAD_ZONE:
                self.tree3.changeY = 0
            else:
                self.tree3.changeY = -self.joystick.y * MOVEMENT_SPEED

        self.tree3.update()
    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
            self.tree2.changeX = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.tree2.changeX = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.tree2.changeY = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.tree2.changeY = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.tree2.changeX = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.tree2.changeY = 0

def main():
    window = MyGame()
    arcade.run()


main()