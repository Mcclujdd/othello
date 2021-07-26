import tkinter as tkr

master = tkr.Tk()
master.geometry("800x800")
frame = tkr.Frame(master)
frame.pack()

canvas = tkr.Canvas(master, width=720, height=720)
canvas.pack(expand=tkr.YES, fill=tkr.BOTH)



# def init_tile():
#     tile = tkr.Button(frame, bg='black')
#     tile.pack()


class tile:
    def __init__(self, coordinate, is_black):
        self.coordinate = coordinate
        self.is_black = is_black

def test_button():
    print('testing')

class Board_Square:
    pass

board_matrix = [[0,1,2,3,4,5,6,7],
            [8,9,10,11,12,13,14,15],
            [16,17,18,19,20,21,22,23],
            [24,25,26,27,28,29,30,31],
            [32,33,34,35,36,37,38,39],
            [40,41,42,43,44,45,46,47],
            [48,49,50,51,52,53,54,55],
            [56,57,58,59,60,61,62,63]]


board_matrix2 = ['0','1','2','3','4','5','6','7',
            '8','9','10','11','12','13','14','15',
            '16','17','18','19','20','21','22','23',
            '24','25','26','27','28','29','30','31',
            '32','33','34','35','36','37','38','39',
            '40','41','42','43','44','45','46','47',
            '48','49','50','51','52','53','54','55',
            '56','57','58','59','60','61','62','63']

board_height = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
board_width = ('1', '2', '3', '4', '5', '6', '7', '8')




board_matrix_assignments = {}  # a1 - h8 assigned to 0-63
index = 0
for letter in board_height:
    for number in board_width:

        board_matrix_assignments[letter+number] = f'{board_matrix2[int(index)]}'
        index +=1



x1 = 10
x2 = 20
y1 = 10
y2 = 20

for row in board_matrix:
    x1 = 10
    x2 = 20
    for col in row:
        canvas.create_rectangle(x1, y1, x2, y2)
        # init_tile()
        x1 += 10
        x2 += 10
    y1 += 10
    y2 += 10

# rect1 = canvas.create_rectangle(10, 10, 20, 20, width=1)
# rect2 = canvas.create_rectangle(10, 20, 20, 30, width=1)
# canvas.move(rect1, 10, 10)

tkr.mainloop()