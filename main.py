import time
import pyglet

mus = pyglet.resource.media("dead.mp3")

x = 1007

mus.play()

while x >= 0 :
    x = x-7
    print(x," - 7") 
    time.sleep(0.0468)

pyglet.app.run()
