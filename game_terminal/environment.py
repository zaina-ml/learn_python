import os
import random
import time

class Environment:
    def __init__(self, size_x, size_y, char, player, enemy_symbol):
        self.size_x = size_x
        self.size_y = size_y
        self.char = char
        self.env = []

        self.player = player

        self.enemy_symbol = enemy_symbol
        self.enemy_x = 0
        self.enemy_y = 0

    def initialize(self):
        env = []

        for i in range(self.size_y):
            row = []
            for i in range(self.size_x):
                row.append(self.char)
            env.append(row)

        self.env = env

    def render(self):
        self.clear()

        for i in range(self.size_x):
            print("___", end='')
        print()

        for row in self.env:
            for char in row:
                print(char, end='')
            print()
        print()
        for i in range(self.size_x):
            print("___", end='')

    def render_player(self):
        self.remove(self.player.char_symbol)
        self.env[self.player.y - 1][self.player.x - 1] = self.player.char_symbol

    def create_enemy(self):
        self.enemy_x = random.randint(1, self.size_x)
        self.enemy_y = random.randint(1, self.size_y)

        self.edit(self.enemy_x, self.enemy_y, self.enemy_symbol)
    
    def check_player_enemy_collision(self):
        if self.enemy_x == self.player.x and self.enemy_y == self.player.y:
            self.player.points += 1

            self.remove(self.enemy_symbol)
            self.create_enemy()


    def edit(self, x, y, char):
        x -= 1
        y -= 1

        self.env[y][x] = char
    
    def remove(self, remove_char):
        for row in self.env:
            for char in row:
                if char == remove_char:
                    self.env[self.env.index(row)][row.index(char)] = self.char
    
    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    

