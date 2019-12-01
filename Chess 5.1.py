from tkinter import *
import time
w=Tk()
w.title('Chess')
g=Canvas(width=1050,height=800)
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
    pieces_lst=[None,pawn_b,pawn_w,king_b,king_w,queen_b,queen_w,bishop_b,knight_b,rook_b,bishop_w,knight_w,rook_w]
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
    g.delete('pieces')
    global x, y, num, tile, i
    g.create_image(0,0,image=chess_board,anchor=NW) #Displays chess board
    for i in range(13):
        for row in range(8):
            for column in range(8):
                if board[column][row]==i:
                    g.create_image((row*100)+50,(column*100)+50,image=pieces_lst[i], tags='pieces')
def callback(event):
    global mx, my, sq1
    g.delete("txt")
    mx=event.x
    my=event.y
    g.create_text(805,10,font=('Prototype', 20), text=('Mouse clicked at:\n' + str(mx) + ', ' + str(my)),anchor=NW,tags = "txt")
    print ("Mouse clicked at", mx, my)
g.bind("<Button-1>", callback)

g.create_text(805,10,font=('Prototype', 20), text=('Mouse clicked at:'),anchor=NW,tags="txt")
g.pack()
import_images()
piece_pos()
draw()
mainloop()
