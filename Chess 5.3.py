from tkinter import *
import time, math
w=Tk()
w.title('Chess')
menubar=Menu(w)
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
    pieces_lst=[pawn_b,pawn_w,king_b,king_w,queen_b,queen_w,bishop_b,knight_b,rook_b,bishop_w,knight_w,rook_w]
def piece_pos():
    global board
    board=[]
    file=open('saves/data.txt','r')
    for ln in range(8):
        line=file.readline()
        print(line)
        data=line.split('\n')
        print(data)
        board.append(data)
    print(board)
    file.close

    #board=[[9,8,7,3,5,7,8,9],
     #      [1,1,1,1,1,1,1,1],
      #     [0,0,0,0,0,0,0,0],
       #    [0,0,0,0,0,0,0,0],       #Board layout
        #   [0,0,0,0,0,0,0,0],
         #  [0,0,0,0,0,0,0,0],
          # [2,2,2,2,2,2,2,2],
           #[12,11,10,4,6,10,11,12]]
          
def draw():
    g.delete('pieces')
    global x, y, num, tile, i
    g.create_image(0,0,image=chess_board,anchor=NW) #Displays chess board
    for i in range(12):
        for row in range(8):
            for column in range(8):
                if board[column][row]==i+1:
                    g.create_image((row*100)+50,(column*100)+50,image=pieces_lst[i], tags='pieces')
def mousepos(event):
    global mx, my, sq1
    g.delete("txt", "mSelected")
    g.create_text(805,10,font=('Prototype', 20), text=('Mouse clicked at:\n' + str(event.x) + ', ' + str(event.y)),anchor=NW,tags = "txt")
    mx=int(math.ceil(event.x / 100.0)) * 100 -100           #finds the top left corner of a square
    my=int(math.ceil(event.y / 100.0)) * 100 -100
    if mx<800:
        g.create_rectangle( mx, my, mx+100, my+100, outline="green3", width=4, tags="mSelected")
        g.bind("<Button-3>", out)
    #print(mx, my)
def out(event):
    m2x=int(math.ceil(event.x / 100.0)) * 100 -100           #finds the top left corner of a square
    m2y=int(math.ceil(event.y / 100.0)) * 100 -100
    if m2x==mx and m2y==my:
        g.delete("mSelected", "txt")
        g.create_text(805,10,font=('Prototype', 20), text=('Mouse clicked at:'),anchor=NW,tags="txt")

def add_menu():
    file=Menu(menubar, tearoff=False)
    edit=Menu(menubar, tearoff=False)
    game=Menu(menubar, tearoff=False)
    file.add_command(label="New", command=None)
    file.add_command(label="Open", command=None)
    file.add_command(label="Save", command=None)
    edit.add_command(label="Undo", command=None)
    edit.add_command(label="Redo", command=None)
    game.add_command(label="Restart", command=None)
    game.add_command(label="Quit", command=None)
    game.add_command(label="", command=None)

    menubar.add_cascade(label="File", menu=file)
    menubar.add_cascade(label="Edit", menu=edit)
    menubar.add_cascade(label="Game", menu=game)
    menubar.add_command(label="Preferences")


g.bind("<Button-1>", mousepos)
g.create_text(805,10,font=('Prototype', 20), text=('Mouse clicked at:'),anchor=NW,tags="txt")
g.pack()
add_menu()
import_images()
piece_pos()
draw()
w.config(menu=menubar)
w.mainloop()
