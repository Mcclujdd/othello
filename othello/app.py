from othello.game.board import generateBoardValues

board = generateBoardValues()

#for i in board:



#print(board.get(1).tkr_coordinates) # should be True now

value_increase = 10
for tile in board:
    if board.get(tile).coordinate == 'a1':
        continue
    else:
        board.get(tile).tkr_coordinates[0] = board.get(tile).tkr_coordinates[0] + 10 * tile
        board.get(tile).tkr_coordinates[1] = board.get(tile).tkr_coordinates[1] + 10 * tile
        board.get(tile).tkr_coordinates[2] = board.get(tile).tkr_coordinates[2] + 10 * tile
        board.get(tile).tkr_coordinates[3] = board.get(tile).tkr_coordinates[3] + 10 * tile

print(board.get(0).tkr_coordinates)
print(board.get(1).tkr_coordinates)
print(board.get(2).tkr_coordinates)
print(board.get(3).tkr_coordinates)

from othello.game.board import drawBoard

drawBoard()