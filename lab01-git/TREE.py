import arcade

arcade.open_window(1200, 600, "Tree sprite")
arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)

arcade.start_render()

def TREE(x, y):
    # Draw the silhouette
    arcade.draw_point(x, y + 340, arcade.color.BLACK, 20)
    arcade.draw_point(x, y + 320, arcade.color.BLACK, 20)
    arcade.draw_point(x, y + 300, arcade.color.BLACK, 20)
    arcade.draw_point(x, y + 280, arcade.color.BLACK, 20)
    arcade.draw_point(x + 20, y + 360, arcade.color.BLACK, 20)
    arcade.draw_point(x + 40, y + 360, arcade.color.BLACK, 20)
    arcade.draw_point(x + 40, y + 380, arcade.color.BLACK, 20)
    arcade.draw_point(x + 40, y + 400, arcade.color.BLACK, 20)
    arcade.draw_point(x + 40, y + 420, arcade.color.BLACK, 20)
    arcade.draw_point(x + 60, y + 440, arcade.color.BLACK, 20)
    arcade.draw_point(x + 80, y + 440, arcade.color.BLACK, 20)
    arcade.draw_point(x + 100, y + 440, arcade.color.BLACK, 20)
    arcade.draw_point(x + 120, y + 460, arcade.color.BLACK, 20)
    arcade.draw_point(x + 140, y + 460, arcade.color.BLACK, 20)
    arcade.draw_point(x + 160, y + 460, arcade.color.BLACK, 20)
    arcade.draw_point(x + 180, y + 460, arcade.color.BLACK, 20)
    arcade.draw_point(x + 200, y + 440, arcade.color.BLACK, 20)
    arcade.draw_point(x + 200, y + 420, arcade.color.BLACK, 20)
    arcade.draw_point(x + 220, y + 420, arcade.color.BLACK, 20)
    arcade.draw_point(x + 240, y + 440, arcade.color.BLACK, 20)
    arcade.draw_point(x + 260, y + 440, arcade.color.BLACK, 20)
    arcade.draw_point(x + 280, y + 440, arcade.color.BLACK, 20)
    arcade.draw_point(x + 300, y + 440, arcade.color.BLACK, 20)
    arcade.draw_point(x + 320, y + 420, arcade.color.BLACK, 20)
    arcade.draw_point(x + 320, y + 400, arcade.color.BLACK, 20)
    arcade.draw_point(x + 340, y + 380, arcade.color.BLACK, 20)
    arcade.draw_point(x + 340, y + 360, arcade.color.BLACK, 20)
    arcade.draw_point(x + 340, y + 340, arcade.color.BLACK, 20)
    arcade.draw_point(x + 340, y + 320, arcade.color.BLACK, 20)
    arcade.draw_point(x + 360, y + 300, arcade.color.BLACK, 20)
    arcade.draw_point(x + 360, y + 280, arcade.color.BLACK, 20)
    arcade.draw_point(x + 360, y + 260, arcade.color.BLACK, 20)
    arcade.draw_point(x + 360, y + 240, arcade.color.BLACK, 20)
    arcade.draw_point(x + 340, y + 220, arcade.color.BLACK, 20)
    arcade.draw_point(x + 340, y + 200, arcade.color.BLACK, 20)
    arcade.draw_point(x + 320, y + 180, arcade.color.BLACK, 20)
    arcade.draw_point(x + 300, y + 180, arcade.color.BLACK, 20)
    arcade.draw_point(x + 280, y + 160, arcade.color.BLACK, 20)
    arcade.draw_point(x + 260, y + 160, arcade.color.BLACK, 20)
    arcade.draw_point(x + 240, y + 160, arcade.color.BLACK, 20)
    arcade.draw_point(x + 220, y + 140, arcade.color.BLACK, 20)
    arcade.draw_point(x + 220, y + 120, arcade.color.BLACK, 20)
    arcade.draw_point(x + 220, y + 100, arcade.color.BLACK, 20)
    arcade.draw_point(x + 240, y + 80, arcade.color.BLACK, 20)
    arcade.draw_point(x + 240, y + 60, arcade.color.BLACK, 20)
    arcade.draw_point(x + 240, y + 40, arcade.color.BLACK, 20)
    arcade.draw_point(x + 20, y + 260, arcade.color.BLACK, 20)
    arcade.draw_point(x + 40, y + 240, arcade.color.BLACK, 20)
    arcade.draw_point(x + 40, y + 220, arcade.color.BLACK, 20)
    arcade.draw_point(x + 40, y + 200, arcade.color.BLACK, 20)
    arcade.draw_point(x + 60, y + 180, arcade.color.BLACK, 20)
    arcade.draw_point(x + 80, y + 180, arcade.color.BLACK, 20)
    arcade.draw_point(x + 100, y + 160, arcade.color.BLACK, 20)
    arcade.draw_point(x + 120, y + 160, arcade.color.BLACK, 20)
    arcade.draw_point(x + 140, y + 140, arcade.color.BLACK, 20)
    arcade.draw_point(x + 140, y + 120, arcade.color.BLACK, 20)
    arcade.draw_point(x + 140, y + 100, arcade.color.BLACK, 20)
    arcade.draw_point(x + 140, y + 80, arcade.color.BLACK, 20)
    arcade.draw_point(x + 140, y + 60, arcade.color.BLACK, 20)
    arcade.draw_point(x + 120, y + 40, arcade.color.BLACK, 20)
    arcade.draw_point(x + 160, y + 160, arcade.color.BLACK, 20)
    arcade.draw_point(x + 180, y + 160, arcade.color.BLACK, 20)
    arcade.draw_point(x + 200, y + 20, arcade.color.BLACK, 20)
    arcade.draw_point(x + 220, y + 20, arcade.color.BLACK, 20)
    arcade.draw_point(x + 240, y, arcade.color.BLACK, 20)
    arcade.draw_point(x + 260, y, arcade.color.BLACK, 20)
    arcade.draw_point(x + 280, y + 20, arcade.color.BLACK, 20)
    arcade.draw_point(x + 260, y + 40, arcade.color.BLACK, 20)
    arcade.draw_point(x + 280, y, arcade.color.BLACK, 20)
    arcade.draw_point(x + 180, y, arcade.color.BLACK, 20)
    arcade.draw_point(x + 160, y + 20, arcade.color.BLACK, 20)
    arcade.draw_point(x + 140, y + 20, arcade.color.BLACK, 20)
    arcade.draw_point(x + 100, y + 20, arcade.color.BLACK, 20)
    arcade.draw_point(x + 100, y, arcade.color.BLACK, 20)
    arcade.draw_point(x + 120, y, arcade.color.BLACK, 20)

    # Draw the colors
    arcade.draw_point(x + 20, y + 300, arcade.color.CASTLETON_GREEN, 20)
    arcade.draw_point(x + 20, y + 320, arcade.color.CASTLETON_GREEN, 20)
    arcade.draw_point(x + 20, y + 280, arcade.color.AO, 20)
    arcade.draw_point(x + 20, y + 340, arcade.color.AO, 20)
    arcade.draw_point(x + 40, y + 340, arcade.color.AO, 20)
    arcade.draw_point(x + 40, y + 320, arcade.color.AO, 20)
    arcade.draw_point(x + 40, y + 300, arcade.color.AO, 20)
    arcade.draw_point(x + 40, y + 280, arcade.color.AO, 20)
    arcade.draw_point(x + 40, y + 260, arcade.color.CASTLETON_GREEN, 20)
    arcade.draw_point(x + 60, y + 340, arcade.color.FOREST_GREEN, 20)
    arcade.draw_point(x + 60, y + 320, arcade.color.FOREST_GREEN, 20)
    arcade.draw_point(x + 60, y + 360, arcade.color.FOREST_GREEN, 20)
    arcade.draw_point(x + 80, y + 360, arcade.color.FOREST_GREEN, 20)
    arcade.draw_point(x + 100, y + 360, arcade.color.FOREST_GREEN, 20)
    arcade.draw_point(x + 80, y + 320, arcade.color.FOREST_GREEN, 20)
    arcade.draw_point(x + 80, y + 340, arcade.color.FOREST_GREEN, 20)
    arcade.draw_point(x + 100, y + 340, arcade.color.FOREST_GREEN, 20)
    arcade.draw_point(x + 100, y + 320, arcade.color.FOREST_GREEN, 20)
    arcade.draw_point(x + 100, y + 300, arcade.color.FOREST_GREEN, 20)
    arcade.draw_point(x + 80, y + 300, arcade.color.AO, 20)
    arcade.draw_point(x + 60, y + 300, arcade.color.AO, 20)
    arcade.draw_point(x + 60, y + 280, arcade.color.AO, 20)
    arcade.draw_point(x + 60, y + 260, arcade.color.AO, 20)
    arcade.draw_point(x + 60, y + 240, arcade.color.CASTLETON_GREEN, 20)
    arcade.draw_point(x + 60, y + 220, arcade.color.CASTLETON_GREEN, 20)
    arcade.draw_point(x + 60, y + 200, arcade.color.CASTLETON_GREEN, 20)
    arcade.draw_point(x + 60, y + 380, arcade.color.AO, 20)
    arcade.draw_point(x + 60, y + 400, arcade.color.AO, 20)
    arcade.draw_point(x + 60, y + 420, arcade.color.FOREST_GREEN, 20)
    arcade.draw_point(x + 80, y + 420, arcade.color.FOREST_GREEN, 20)
    arcade.draw_point(x + 100, y + 420, arcade.color.FOREST_GREEN, 20)
    arcade.draw_point(x + 120, y + 400, arcade.color.FOREST_GREEN, 20)
    arcade.draw_point(x + 120, y + 420, arcade.color.FOREST_GREEN, 20)
    arcade.draw_point(x + 120, y + 440, arcade.color.FOREST_GREEN, 20)
    arcade.draw_point(x + 140, y + 440, arcade.color.FOREST_GREEN, 20)
    arcade.draw_point(x + 140, y + 420, arcade.color.FOREST_GREEN, 20)
    arcade.draw_point(x + 160, y + 420, arcade.color.FOREST_GREEN, 20)
    arcade.draw_point(x + 180, y + 420, arcade.color.DARK_PASTEL_GREEN, 20)
    arcade.draw_point(x + 180, y + 440, arcade.color.DARK_PASTEL_GREEN, 20)
    arcade.draw_point(x + 160, y + 440, arcade.color.DARK_PASTEL_GREEN, 20)
    arcade.draw_point(x + 100, y + 400, arcade.color.AO, 20)
    arcade.draw_point(x + 80, y + 400, arcade.color.AO, 20)
    arcade.draw_point(x + 140, y + 400, arcade.color.AO, 20)
    arcade.draw_point(x + 100, y + 380, arcade.color.AO, 20)
    arcade.draw_point(x + 80, y + 380, arcade.color.AO, 20)
    arcade.draw_point(x + 120, y + 380, arcade.color.AO, 20)
    arcade.draw_point(x + 140, y + 380, arcade.color.AO, 20)
    arcade.draw_point(x + 160, y + 380, arcade.color.AO, 20)
    arcade.draw_point(x + 160, y + 400, arcade.color.AO, 20)
    arcade.draw_point(x + 160, y + 360, arcade.color.AO, 20)
    arcade.draw_point(x + 140, y + 360, arcade.color.DARK_PASTEL_GREEN, 20)
    arcade.draw_point(x + 140, y + 340, arcade.color.DARK_PASTEL_GREEN, 20)
    arcade.draw_point(x + 120, y + 360, arcade.color.DARK_PASTEL_GREEN, 20)
    arcade.draw_point(x + 120, y + 340, arcade.color.FOREST_GREEN, 20)
    arcade.draw_point(x + 160, y + 340, arcade.color.FOREST_GREEN, 20)
    arcade.draw_point(x + 160, y + 320, arcade.color.FOREST_GREEN, 20)
    arcade.draw_point(x + 140, y + 320, arcade.color.FOREST_GREEN, 20)
    arcade.draw_point(x + 120, y + 320, arcade.color.FOREST_GREEN, 20)
    arcade.draw_point(x + 120, y + 300, arcade.color.FOREST_GREEN, 20)
    arcade.draw_point(x + 120, y + 280, arcade.color.AO, 20)
    arcade.draw_point(x + 100, y + 280, arcade.color.AO, 20)
    arcade.draw_point(x + 80, y + 280, arcade.color.AO, 20)
    arcade.draw_point(x + 80, y + 260, arcade.color.AO, 20)
    arcade.draw_point(x + 80, y + 240, arcade.color.AO, 20)
    arcade.draw_point(x + 80, y + 220, arcade.color.CASTLETON_GREEN, 20)
    arcade.draw_point(x + 80, y + 200, arcade.color.CASTLETON_GREEN, 20)
    arcade.draw_point(x + 100, y + 180, arcade.color.CASTLETON_GREEN, 20)
    arcade.draw_point(x + 100, y + 200, arcade.color.CASTLETON_GREEN, 20)
    arcade.draw_point(x + 100, y + 180, arcade.color.CASTLETON_GREEN, 20)
    arcade.draw_point(x + 100, y + 220, arcade.color.AO, 20)
    arcade.draw_point(x + 120, y + 220, arcade.color.CASTLETON_GREEN, 20)
    arcade.draw_point(x + 120, y + 200, arcade.color.CASTLETON_GREEN, 20)
    arcade.draw_point(x + 120, y + 180, arcade.color.CASTLETON_GREEN, 20)
    arcade.draw_point(x + 140, y + 180, arcade.color.CASTLETON_GREEN, 20)
    arcade.draw_point(x + 140, y + 160, arcade.color.CASTLETON_GREEN, 20)
    arcade.draw_point(x + 140, y + 200, arcade.color.CASTLETON_GREEN, 20)
    arcade.draw_point(x + 140, y + 220, arcade.color.CASTLETON_GREEN, 20)
    arcade.draw_point(x + 160, y + 200, arcade.color.CASTLETON_GREEN, 20)
    arcade.draw_point(x + 160, y + 180, arcade.color.CASTLETON_GREEN, 20)
    arcade.draw_point(x + 160, y + 220, arcade.color.AO, 20)
    arcade.draw_point(x + 180, y + 180, arcade.color.CASTLETON_GREEN, 20)
    arcade.draw_point(x + 180, y + 200, arcade.color.CASTLETON_GREEN, 20)
    arcade.draw_point(x + 180, y + 220, arcade.color.CASTLETON_GREEN, 20)
    arcade.draw_point(x + 180, y + 240, arcade.color.CASTLETON_GREEN, 20)
    arcade.draw_point(x + 160, y + 240, arcade.color.CASTLETON_GREEN, 20)
    arcade.draw_point(x + 200, y + 200, arcade.color.CASTLETON_GREEN, 20)
    arcade.draw_point(x + 200, y + 220, arcade.color.CASTLETON_GREEN, 20)
    arcade.draw_point(x + 200, y + 180, arcade.color.CASTLETON_GREEN, 20)
    arcade.draw_point(x + 200, y + 160, arcade.color.CASTLETON_GREEN, 20)
    arcade.draw_point(x + 220, y + 160, arcade.color.CASTLETON_GREEN, 20)
    arcade.draw_point(x + 220, y + 180, arcade.color.CASTLETON_GREEN, 20)
    arcade.draw_point(x + 220, y + 200, arcade.color.CASTLETON_GREEN, 20)
    arcade.draw_point(x + 220, y + 220, arcade.color.CASTLETON_GREEN, 20)
    arcade.draw_point(x + 240, y + 220, arcade.color.CASTLETON_GREEN, 20)
    arcade.draw_point(x + 240, y + 200, arcade.color.CASTLETON_GREEN, 20)
    arcade.draw_point(x + 240, y + 180, arcade.color.CASTLETON_GREEN, 20)
    arcade.draw_point(x + 260, y + 180, arcade.color.CASTLETON_GREEN, 20)
    arcade.draw_point(x + 260, y + 200, arcade.color.CASTLETON_GREEN, 20)
    arcade.draw_point(x + 280, y + 200, arcade.color.CASTLETON_GREEN, 20)
    arcade.draw_point(x + 280, y + 180, arcade.color.CASTLETON_GREEN, 20)
    arcade.draw_point(x + 280, y + 220, arcade.color.CASTLETON_GREEN, 20)
    arcade.draw_point(x + 300, y + 220, arcade.color.CASTLETON_GREEN, 20)
    arcade.draw_point(x + 300, y + 200, arcade.color.CASTLETON_GREEN, 20)
    arcade.draw_point(x + 320, y + 200, arcade.color.CASTLETON_GREEN, 20)
    arcade.draw_point(x + 320, y + 220, arcade.color.CASTLETON_GREEN, 20)
    arcade.draw_point(x + 340, y + 240, arcade.color.CASTLETON_GREEN, 20)
    arcade.draw_point(x + 320, y + 240, arcade.color.AO, 20)
    arcade.draw_point(x + 300, y + 240, arcade.color.AO, 20)
    arcade.draw_point(x + 280, y + 240, arcade.color.AO, 20)
    arcade.draw_point(x + 260, y + 240, arcade.color.AO, 20)
    arcade.draw_point(x + 260, y + 220, arcade.color.AO, 20)
    arcade.draw_point(x + 240, y + 240, arcade.color.AO, 20)
    arcade.draw_point(x + 220, y + 240, arcade.color.AO, 20)
    arcade.draw_point(x + 200, y + 240, arcade.color.AO, 20)
    arcade.draw_point(x + 140, y + 240, arcade.color.AO, 20)
    arcade.draw_point(x + 120, y + 240, arcade.color.AO, 20)
    arcade.draw_point(x + 100, y + 240, arcade.color.AO, 20)
    arcade.draw_point(x + 100, y + 260, arcade.color.AO, 20)
    arcade.draw_point(x + 120, y + 260, arcade.color.AO, 20)
    arcade.draw_point(x + 140, y + 260, arcade.color.AO, 20)
    arcade.draw_point(x + 160, y + 260, arcade.color.AO, 20)
    arcade.draw_point(x + 180, y + 260, arcade.color.AO, 20)
    arcade.draw_point(x + 200, y + 260, arcade.color.AO, 20)
    arcade.draw_point(x + 220, y + 260, arcade.color.AO, 20)
    arcade.draw_point(x + 240, y + 260, arcade.color.AO, 20)
    arcade.draw_point(x + 260, y + 260, arcade.color.AO, 20)
    arcade.draw_point(x + 280, y + 260, arcade.color.AO, 20)
    arcade.draw_point(x + 300, y + 260, arcade.color.AO, 20)
    arcade.draw_point(x + 320, y + 260, arcade.color.AO, 20)
    arcade.draw_point(x + 340, y + 260, arcade.color.AO, 20)
    arcade.draw_point(x + 340, y + 280, arcade.color.FOREST_GREEN, 20)
    arcade.draw_point(x + 340, y + 300, arcade.color.FOREST_GREEN, 20)
    arcade.draw_point(x + 320, y + 280, arcade.color.AO, 20)
    arcade.draw_point(x + 300, y + 280, arcade.color.AO, 20)
    arcade.draw_point(x + 320, y + 300, arcade.color.AO, 20)
    arcade.draw_point(x + 300, y + 300, arcade.color.AO, 20)
    arcade.draw_point(x + 280, y + 300, arcade.color.FOREST_GREEN, 20)
    arcade.draw_point(x + 280, y + 280, arcade.color.AO, 20)
    arcade.draw_point(x + 260, y + 280, arcade.color.AO, 20)
    arcade.draw_point(x + 240, y + 280, arcade.color.AO, 20)
    arcade.draw_point(x + 220, y + 280, arcade.color.AO, 20)
    arcade.draw_point(x + 200, y + 280, arcade.color.AO, 20)
    arcade.draw_point(x + 180, y + 280, arcade.color.AO, 20)
    arcade.draw_point(x + 160, y + 280, arcade.color.AO, 20)
    arcade.draw_point(x + 140, y + 280, arcade.color.AO, 20)
    arcade.draw_point(x + 140, y + 300, arcade.color.AO, 20)
    arcade.draw_point(x + 160, y + 300, arcade.color.AO, 20)
    arcade.draw_point(x + 180, y + 300, arcade.color.AO, 20)
    arcade.draw_point(x + 200, y + 300, arcade.color.AO, 20)
    arcade.draw_point(x + 220, y + 300, arcade.color.AO, 20)
    arcade.draw_point(x + 240, y + 300, arcade.color.FOREST_GREEN, 20)
    arcade.draw_point(x + 260, y + 300, arcade.color.FOREST_GREEN, 20)
    arcade.draw_point(x + 260, y + 320, arcade.color.FOREST_GREEN, 20)
    arcade.draw_point(x + 280, y + 320, arcade.color.DARK_PASTEL_GREEN, 20)
    arcade.draw_point(x + 300, y + 320, arcade.color.DARK_PASTEL_GREEN, 20)
    arcade.draw_point(x + 240, y + 320, arcade.color.FOREST_GREEN, 20)
    arcade.draw_point(x + 220, y + 320, arcade.color.FOREST_GREEN, 20)
    arcade.draw_point(x + 200, y + 320, arcade.color.AO, 20)
    arcade.draw_point(x + 180, y + 320, arcade.color.AO, 20)
    arcade.draw_point(x + 180, y + 340, arcade.color.AO, 20)
    arcade.draw_point(x + 180, y + 360, arcade.color.AO, 20)
    arcade.draw_point(x + 180, y + 380, arcade.color.AO, 20)
    arcade.draw_point(x + 180, y + 400, arcade.color.AO, 20)
    arcade.draw_point(x + 200, y + 400, arcade.color.AO, 20)
    arcade.draw_point(x + 200, y + 380, arcade.color.FOREST_GREEN, 20)
    arcade.draw_point(x + 200, y + 360, arcade.color.AO, 20)
    arcade.draw_point(x + 200, y + 340, arcade.color.AO, 20)
    arcade.draw_point(x + 220, y + 340, arcade.color.AO, 20)
    arcade.draw_point(x + 220, y + 360, arcade.color.AO, 20)
    arcade.draw_point(x + 220, y + 380, arcade.color.AO, 20)
    arcade.draw_point(x + 220, y + 400, arcade.color.AO, 20)
    arcade.draw_point(x + 240, y + 340, arcade.color.FOREST_GREEN, 20)
    arcade.draw_point(x + 260, y + 340, arcade.color.DARK_PASTEL_GREEN, 20)
    arcade.draw_point(x + 280, y + 340, arcade.color.DARK_PASTEL_GREEN, 20)
    arcade.draw_point(x + 300, y + 340, arcade.color.AO, 20)
    arcade.draw_point(x + 320, y + 340, arcade.color.AO, 20)
    arcade.draw_point(x + 320, y + 320, arcade.color.AO, 20)
    arcade.draw_point(x + 320, y + 360, arcade.color.AO, 20)
    arcade.draw_point(x + 300, y + 360, arcade.color.AO, 20)
    arcade.draw_point(x + 280, y + 360, arcade.color.AO, 20)
    arcade.draw_point(x + 260, y + 360, arcade.color.AO, 20)
    arcade.draw_point(x + 240, y + 360, arcade.color.AO, 20)
    arcade.draw_point(x + 240, y + 380, arcade.color.AO, 20)
    arcade.draw_point(x + 260, y + 380, arcade.color.AO, 20)
    arcade.draw_point(x + 280, y + 380, arcade.color.FOREST_GREEN, 20)
    arcade.draw_point(x + 300, y + 380, arcade.color.FOREST_GREEN, 20)
    arcade.draw_point(x + 320, y + 380, arcade.color.FOREST_GREEN, 20)
    arcade.draw_point(x + 260, y + 400, arcade.color.FOREST_GREEN, 20)
    arcade.draw_point(x + 240, y + 400, arcade.color.FOREST_GREEN, 20)
    arcade.draw_point(x + 240, y + 420, arcade.color.FOREST_GREEN, 20)
    arcade.draw_point(x + 260, y + 420, arcade.color.DARK_PASTEL_GREEN, 20)
    arcade.draw_point(x + 280, y + 420, arcade.color.DARK_PASTEL_GREEN, 20)
    arcade.draw_point(x + 300, y + 420, arcade.color.DARK_PASTEL_GREEN, 20)
    arcade.draw_point(x + 300, y + 400, arcade.color.DARK_PASTEL_GREEN, 20)
    arcade.draw_point(x + 280, y + 400, arcade.color.DARK_PASTEL_GREEN, 20)

    # bark
    arcade.draw_point(x + 180, y + 40, arcade.color.COCONUT, 20)
    arcade.draw_point(x + 140, y + 40, arcade.color.BROWN_NOSE, 20)
    arcade.draw_point(x + 160, y + 40, arcade.color.BROWN_NOSE, 20)
    arcade.draw_point(x + 160, y + 60, arcade.color.BROWN_NOSE, 20)
    arcade.draw_point(x + 160, y + 80, arcade.color.BROWN_NOSE, 20)
    arcade.draw_point(x + 180, y + 60, arcade.color.BROWN_NOSE, 20)
    arcade.draw_point(x + 220, y + 80, arcade.color.BROWN_NOSE, 20)
    arcade.draw_point(x + 200, y + 80, arcade.color.COCONUT, 20)
    arcade.draw_point(x + 180, y + 80, arcade.color.COCONUT, 20)
    arcade.draw_point(x + 200, y + 60, arcade.color.COCONUT, 20)
    arcade.draw_point(x + 220, y + 60, arcade.color.COCONUT, 20)
    arcade.draw_point(x + 220, y + 40, arcade.color.COCONUT, 20)
    arcade.draw_point(x + 200, y + 40, arcade.color.COCONUT, 20)
    arcade.draw_point(x + 160, y + 100, arcade.color.COCONUT, 20)
    arcade.draw_point(x + 180, y + 100, arcade.color.COCONUT, 20)
    arcade.draw_point(x + 200, y + 100, arcade.color.COCONUT, 20)
    arcade.draw_point(x + 180, y + 120, arcade.color.COCONUT, 20)
    arcade.draw_point(x + 200, y + 120, arcade.color.COCONUT, 20)
    arcade.draw_point(x + 160, y + 120, arcade.color.BROWN_NOSE, 20)
    arcade.draw_point(x + 160, y + 140, arcade.color.BROWN_NOSE, 20)
    arcade.draw_point(x + 180, y + 140, arcade.color.BROWN_NOSE, 20)
    arcade.draw_point(x + 200, y + 140, arcade.color.BROWN_NOSE, 20)
    arcade.draw_point(x + 120, y + 20, arcade.color.BROWN_NOSE, 20)
    arcade.draw_point(x + 180, y + 20, arcade.color.COCONUT, 20)
    arcade.draw_point(x + 240, y + 20, arcade.color.COCONUT, 20)
    arcade.draw_point(x + 260, y + 20, arcade.color.COCONUT, 20)

TREE(200, 100)
TREE(0, 100)
TREE(400, 100)
TREE(800, 100)
TREE(600, 100)
# --- Finish drawing ---
arcade.finish_render()
arcade.run()