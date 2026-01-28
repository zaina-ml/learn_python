from player import Player
from environment import Environment
import time

player = Player(1, 2, "\U000025A1")

env = Environment(10, 10, "   ", player, "\U000025AB")
env.initialize()
env.create_enemy()

while True:
    player.move(input("W, A, S, D to move: "), env.size_x, env.size_y)

    
    env.render_player()
    env.check_player_enemy_collision()
    env.render()

    print("\n\nPoints: " + str(player.points))