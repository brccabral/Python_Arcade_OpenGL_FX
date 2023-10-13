import arcade
from arcade.experimental import Shadertoy


# Derive an application window from Arcade's parent Window class
class MyGame(arcade.Window):
    def __init__(self):
        # Call the parent constructor
        super().__init__(width=1920, height=1080)

        # Load a file and create a shader from it
        # file_name = "circle_1.glsl"
        file_name = "earth_planet_sky.glsl"
        # file_name = "cyber_fuji_2020.glsl"
        # file_name = "fractal_pyramid.glsl"
        # file_name = "flame.glsl"
        # file_name = "star_nest.glsl"
        with open(file_name) as file:
            shader_source = file.read()
        self.shadertoy = Shadertoy(size=self.get_size(), main_source=shader_source)

        # Keep track of total run-time
        self.time = 0.0
        self.channel0 = self.shadertoy.ctx.framebuffer(
            color_attachments=[self.shadertoy.ctx.texture(self.get_size(), components=4)]
        )
        self.shadertoy.channel_0 = self.channel0.color_attachments[0]
        # self.shadertoy.iChannel0 = self.channel0.color_attachments[0]
        self.sprite = arcade.Sprite("clouds.jpg")

    def on_draw(self):
        self.channel0.use()
        self.sprite.draw()
        self.use()
        self.clear()
        mouse_pos = self.mouse["x"], self.mouse["y"]

        # Set uniform data to send to the GLSL shader
        #  circle_1.glsl inputs
        # self.shadertoy.program["pos"] = mouse_pos
        # self.shadertoy.program["color"] = arcade.get_three_float_color(
        #     arcade.color.NEON_GREEN
        # )
        # Run the GLSL code
        self.shadertoy.render(time=self.time, mouse_position=mouse_pos)
        # self.sprite.draw()

    def on_update(self, dt):
        # Keep track of elapsed time
        self.time += dt


if __name__ == "__main__":
    MyGame()
    arcade.run()
