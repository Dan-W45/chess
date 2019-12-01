import tkinter as tk
from tkinter import *
import time, math, ast
w=Tk()
w.title('Chess')
menubar=Menu(w)
g=Canvas(width=1050,height=800,bg="khaki")
def import_images():
    global chess_board, pieces_lst
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
    pieces_lst=[pawn_b,pawn_w,king_b,king_w,queen_b,queen_w,bishop_b,knight_b,rook_b,bishop_w,knight_w,rook_w]
def piece_pos():
    global board
    board=[['9','8','7','3','5','7','8','9'],
           ['1','1','1','1','1','1','1','1'],
           ['0','0','0','0','0','0','0','0'],
           ['0','0','0','0','0','0','0','0'],       #Board layout
           ['0','0','0','0','0','0','0','0'],
           ['0','0','0','0','0','0','0','0'],
           ['2','2','2','2','2','2','2','2'],
           ['12','11','10','4','6','10','11','12']]
def draw():
    g.delete('pieces', 'board')
    global x, y, num, tile, i
    g.create_image(0,0,image=chess_board,anchor=NW, tags='board') #Displays chess board
    for i in range(12):
        for row in range(8):
            for column in range(8):
                if board[column][row]==str(i+1):
                    g.create_image((row*100)+50,(column*100)+50,image=pieces_lst[i], tags='pieces')

def mousepos(event):
    global mx, my, sq1, current
    g.delete("txt", "mSelected")
    mx=int(math.ceil(event.x / 100.0)) * 100 -100           #finds the top left corner of a square
    my=int(math.ceil(event.y / 100.0)) * 100 -100
    current=board[int(my/100)][int(mx/100)]
    board[int(my/100)][int(mx/100)]=0
    print(current)
    if mx<800:
        g.create_rectangle( mx, my, mx+100, my+100, outline="green3", width=4, tags="mSelected")
        g.bind("<Button-3>", remove)
        g.bind("<Button-1>", mousepos2)
def mousepos2(event):
    g.delete("mSelected")
    mx=int(math.ceil(event.x / 100.0)) * 100 -100           #finds the top left corner of a square
    my=int(math.ceil(event.y / 100.0)) * 100 -100
    board[int(my/100)][int(mx/100)]=current
    draw()
    g.bind("<Button-1>", mousepos)
def remove(event):
    m2x=int(math.ceil(event.x / 100.0)) * 100 -100           #finds the top left corner of a square
    m2y=int(math.ceil(event.y / 100.0)) * 100 -100
    if m2x==mx and m2y==my:
        g.delete("mSelected", "txt")
        g.bind("<Button-1>", mousepos)

g.bind("<Button-1>", mousepos)
g.focus_set()
g.pack()
import_images()
piece_pos()
draw()
w.mainloop()
