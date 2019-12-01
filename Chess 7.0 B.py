import tkinter as tk
from tkinter import *
import time, math, ast, socket, threading, time
w=Tk()
w.title('Chess')
menubar=Menu(w)
g=Canvas(width=1050,height=800,bg="khaki")


s = socket.socket()        
host = 'danwalsh450.duckdns.org' 
port = 6702
s.connect((host, port))

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
    global board
    s.send((str(board)).encode())
    g.delete('pieces', 'board')
    global x,y,num,tile,i
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
    #print(current)
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

def new():
    global board
    piece_pos()
    g.delete("txt", "mSelected")
##    g.create_text(805,10,font=('Prototype', 20), text=('Mouse clicked at:'),anchor=NW,tags="txt")
    piece_pos()
    draw()
    print('New game')
def open_():
    global Sname, master
    master=Tk()
    Label(master, text="Document name:").grid(row=0)
    Sname = Entry(master)
    Sname.grid(row=0, column=1)
    Button(master, text='Open', command=open_from).grid(row=0, column=2, sticky=W, pady=4)
def open_from():
    global board
    searchfile = open("saves/save.txt", "r")
    savename=Sname.get()
    for line in searchfile:
        if savename in line:
            #print(line)
            toboard=line.replace(savename,"")
            toboard=toboard.replace(" ","")
            toboard=toboard.replace("\n","")
            toboard
            #print(toboard)
            board=ast.literal_eval(toboard)     #Converts str into lst using ast module
            #print(board)
            draw()
            master.destroy()
def restart():
    piece_pos()
    draw()
    g.delete("txt")
##    g.create_text(805,10,font=('Prototype', 20), text=('Mouse clicked at:'),anchor=NW,tags="txt")
    print('Restarted Game')
def save():
    None
def save_as():
    global name, master, board
    master=Tk()
    Label(master, text="Save name").grid(row=0)
    name = Entry(master)
    name.grid(row=0, column=1)
    Button(master, text='Save', command=save_to).grid(row=0, column=2, sticky=W, pady=4)
def save_to():
    global board
    with open("saves/save.txt", "a") as output:
        #print(name.get() + 'Has Saved their game')
        output.write(name.get()+' ')
        output.write(str(board))            #Appends the player name and board to a list
        output.write('\n')
        master.destroy()

def add_menu():
    file=Menu(menubar, tearoff=False)
    edit=Menu(menubar, tearoff=False)
    game=Menu(menubar, tearoff=False)
    file.add_command(label="New", command=new)
    file.add_command(label="Open", command=open_)
    file.add_command(label="Save", command=save)
    file.add_command(label="Save As...", command=save_as)
##    edit.add_command(label="Undo", command=None)
##    edit.add_command(label="Redo", command=None)
    game.add_command(label="Restart", command=restart)
    game.add_command(label="Quit", command=None)

    menubar.add_cascade(label="File", menu=file)
##    menubar.add_cascade(label="Edit", menu=edit)
    menubar.add_cascade(label="Game", menu=game)

def commline():
    global board, loop
    while loop:
        s.send(("ping").encode())
        time.sleep(0.5)
        toboard=repr(s.recv(1024).decode())
        print(toboard)
        if "[" in toboard:
            board=None
            toboard=toboard.replace(" ","")
            toboard=toboard.replace("ping","")
            toboard=toboard.replace("\n","")
    ##        print(toboard)
            board=ast.literal_eval(ast.literal_eval(toboard))
##        print(type(board))
##        print(board)



g.bind("<Button-1>", mousepos)
##g.create_text(805,10,font=('Prototype', 20), text=('Mouse clicked at:'),anchor=NW,tags="txt")
g.focus_set()
g.pack()
add_menu()
import_images()
piece_pos()
draw()
w.config(menu=menubar)
if s.recv(1024).decode() == "Connected":
    print('Server: Connected')
    loop = True
    dataloop = threading.Timer(0,commline)
    dataloop.start()
w.mainloop()
print('Disconnecting')
dataloop.cancel()
loop=False
s.send(("Disconnect").encode())













