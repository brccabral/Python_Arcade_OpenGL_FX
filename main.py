import arcade
from arcade.experimental import Shadertoy


# Derive an application window from Arcade's parent Window class
class MyGame(arcade.Window):
    def __init__(self):
        # Call the parent constructor
        super().__init__(width=1920, height=1080)

        # Load a file and create a shader from it
        file_name = "circle_1.glsl"
        with open(file_name) as file:
            shader_source = file.read()
        self.shadertoy = Shadertoy(size=self.get_size(), main_source=shader_source)

    def on_draw(self):
        # Set uniform data to send to the GLSL shader
        self.shadertoy.program["pos"] = self.mouse["x"], self.mouse["y"]
        self.shadertoy.program["color"] = arcade.get_three_float_color(
            arcade.color.NEON_GREEN
        )
        # Run the GLSL code
        self.shadertoy.render()


if __name__ == "__main__":
    MyGame()
    arcade.run()
