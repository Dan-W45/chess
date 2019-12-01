from tkinter import *
import time
w=Tk()
w.title('Chess')
g=Canvas(width=1050,height=800)
def import_images():
    global chess_board, king_w, king_b, queen_w, queen_b
    global bishop_w, bishop_b, knight_w, knight_b, rook_w
    global rook_b, pawn_w, pawn_b, pieces_lst
    chess_board=PhotoImage(file='textures/board/chess_board.png') #Importing all images
    king_w=PhotoImage(file='textures/pieces/king_w.png')
    king_b=PhotoImage(file='textures/pieces/king_b.png')
    queen_w=PhotoImage(file='textures/pieces/queen_w.png')
    queen_b=PhotoImage(file='textures/pieces/queen_b.png')
    bishop_w=PhotoImage(file='textures/pieces/bishop_w.png')
    bishop_b=PhotoImage(file='textures/pieces/bishop_b.png')
    knight_w=PhotoImage(file='textures/pieces/knight_w.png')
    knight_b=PhotoImage(file='textures/pieces/knight_b.png')
    rook_w=PhotoImage(file='textures/pieces/rook_w.png')
    rook_b=PhotoImage(file='textures/pieces/rook_b.png')
    pawn_w=PhotoImage(file='textures/pieces/pawn_w.png')
    pawn_b=PhotoImage(file='textures/pieces/pawn_b.png')
    pieces_lst=[king_b,queen_b,bishop_b,knight_b,rook_b,pawn_b,
                king_w,queen_w,bishop_w,knight_w,rook_w,pawn_w,
                None]

def piece_pos():
    global board
    board=[[9,8,7,3,5,7,8,9],
           [1,1,1,1,1,1,1,1],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],       #Board layout
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [2,2,2,2,2,2,2,2],
           [12,11,10,4,6,10,11,12]]
def draw():
    global x, y, num, tile, i
    g.create_image(0,0,image=chess_board,anchor=NW) #Displays chess board
    x = y = num=0
    for num in range(8):
        #print('number 1: ' + str(num))
        for num2 in range(8):
            #print('num2 ' + str(num2))
            tile=board[num][num2]
            #print('tile ' + str(tile))
            x=(num2*100)+50
            y=(num*100)+50
            g.create_image(x,y,image=pieces_lst[12])
                


def find():
    pawn_b
        



g.pack()
import_images()
piece_pos()
draw()
mainloop()
