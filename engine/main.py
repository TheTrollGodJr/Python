from ursina import *
import random

app = Ursina()
EditorCamera()

# Create a Text entity
full_screen_text = Text(
    text='Your ASCII\n Art Here',
    scale=1,  # Adjust the scale to cover the entire screen
    origin=(-5, -5),  # Set the origin to the center of the text
    x=0,  # Set the x position to the center
    y=0,  # Set the y position to the center
)

cube = Entity(model='cube', texture='brick')

app.run()
