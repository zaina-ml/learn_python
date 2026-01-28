from player import Player
from environment import Environment

p = Player(1, 2, " ⎔ ")

env = Environment(6, 7, " ▢ ", p)
env.initialize()

while True:
    
    p.move(input(), env.size_x, env.size_y)
    env.clear()
    env.render_player()
    print(p.x, p.y)
    env.render()