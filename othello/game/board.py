import tkinter as tkr

master = tkr.Tk()
master.geometry("800x800")
frame = tkr.Frame(master)
frame.pack()

canvas = tkr.Canvas(master, width=800, height=800)
canvas.pack(expand=tkr.YES, fill=tkr.BOTH)


class Tile:
    is_empty = True

    def __init__(self, coordinate, is_black, tkr_coordinates):
        self.coordinate = coordinate
        self.color = 'grey'
        self.tkr_coordinates = tkr_coordinates
        # self.tkr_coordinates = [40, 40, 130, 130] #pixel coordinates for x1, y1, x2, y2


board_matrix = [0,1,2,3,4,5,6,7,
            8,9,10,11,12,13,14,15,
            16,17,18,19,20,21,22,23,
            24,25,26,27,28,29,30,31,
            32,33,34,35,36,37,38,39,
            40,41,42,43,44,45,46,47,
            48,49,50,51,52,53,54,55,
            56,57,58,59,60,61,62,63]

def create_tkr_coordinates(coordinates): # coordinates must be [x1, y1, x2, y2] format

    y1 = coordinates[1]
    y2 = coordinates[3]
    tkr_values = []

    for row in range(8):
        x1 = coordinates[0]
        x2 = coordinates[2]
        for col in range(8):
            tkr_values.append([x1, y1, x2, y2])
            x1 += 90
            x2 += 90
        y1 += 90
        y2 += 90
    return tkr_values



def generateBoardValues():


    board_height = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
    board_width = ('1', '2', '3', '4', '5', '6', '7', '8')

    board_matrix_assignments = {}  # a1 - h8 to be assigned to tile objects
    index = 0
    tkr_values = create_tkr_coordinates([40, 40, 130, 130])

    for letter in board_height:
        for number in board_width:

            board_matrix_assignments[board_matrix[index]] = Tile(f'{letter+number}', False, tkr_values[index])
            index +=1

    return board_matrix_assignments

def modifyColor(tile, color):
    canvas.itemconfig(tile, fill=color)


def onClick(event):
    tile = canvas.find_closest(event.x, event.y)

    current_color = canvas.itemcget(tile, 'fill')

    if current_color == 'grey' or 'blue':
        modify_color(tile, 'red')


def drawBoard(board):

    for tile in board:
        x1 = board.get(tile).tkr_coordinates[0]
        y1 = board.get(tile).tkr_coordinates[1]
        x2 = board.get(tile).tkr_coordinates[2]
        y2 = board.get(tile).tkr_coordinates[3]

        canvas.create_rectangle(x1, y1, x2, y2, fill=board.get(tile).color)


    tkr.mainloop()


