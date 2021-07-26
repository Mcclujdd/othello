
class Piece:
    def __init__(self, coordinates, is_black):
       self.coordinates = coordinates
       self.is_black = is_black

class Player:
    def __init__(self, is_black):
        self.is_black = is_black

playerB = Player(True)
playerW = Player(False)


def place_piece(coordinates, player):
    piece_color = player.is_black
    piece = Piece(coordinates, piece_color)
    
    return str(piece.is_black) + ':' + str(piece.coordinates) + ' '

array = ['a1', 'a6']
past_moves = ''
for coordinate in array:
    past_moves = past_moves + place_piece(coordinate, playerB)

print(past_moves)


