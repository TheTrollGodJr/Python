from ursina import *

application.developement_mode = False

#def update():
    #firstEntity.rotation_y += 5

app = Ursina()
window.fullscreen = True

firstEntity = Entity(model = 'model',
                    texture='brick',
                    color = color.rgb(200, 10, 10),
                    position = (0,0,0),
                    rotation = (20, 40, 2))
text_entity = Text('hello', world_scale=2)

EditorCamera()

app.run()