from environment import Environment

class Player:
    def __init__(self, y, x, char_symbol):
        self.char_symbol = char_symbol

        self.y = y
        self.x =  x

        self.prev_y = y
        self.prev_x = x

        self.points = 0
        
    def move(self, input, len_x, len_y):
        self.prev_y = self.y
        self.prev_x = self.x

        if input == "w":
            self.y -= 1
        elif input == "s":
            self.y += 1
        elif input == "d":
            self.x += 1
        elif input == "a":
            self.x -= 1

        self.check_valid_move(len_x, len_y)

    def check_valid_move(self, len_x, len_y):
        if self.x <= 0 or self.y <= 0 or self.x > len_x or self.y > len_y:
            self.x = self.prev_x
            self.y = self.prev_y

    
    

    


