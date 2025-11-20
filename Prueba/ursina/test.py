from ursina import Ursina, Entity, color

app = Ursina()
Entity(model='cube', color=color.red)
app.run()
