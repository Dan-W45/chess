import contextlib
with contextlib.redirect_stdout(None):
    import pygame, sys, os, ast, time, socket, threading, math
    from pygame.locals import *

os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
font=pygame.font.SysFont("input", 20)


width, height = 1000, 800
g=pygame.display.set_mode([width,height])
clock=pygame.time.Clock()
scale = 100
mouseloc=[800,800]
mx,my=800,800

host = 'danwalsh450.duckdns.org'
#host = '192.168.1.125'
port = 6702
s = socket.socket()
#s.connect((host, port))
#s.send(('joining').encode())
loop = False
pick = True
currnet=0


def import_images():
    global chess_board, pieces_lst
    chess_board=pygame.image.load('textures/board/chess_board.png') #Importing all images
    king_w=pygame.image.load('textures/pieces/king_w.png')
    king_b=pygame.image.load('textures/pieces/king_b.png')
    queen_w=pygame.image.load('textures/pieces/queen_w.png')
    queen_b=pygame.image.load('textures/pieces/queen_b.png')
    bishop_w=pygame.image.load('textures/pieces/bishop_w.png')
    bishop_b=pygame.image.load('textures/pieces/bishop_b.png')
    knight_w=pygame.image.load('textures/pieces/knight_w.png')
    knight_b=pygame.image.load('textures/pieces/knight_b.png')
    rook_w=pygame.image.load('textures/pieces/rook_w.png')
    rook_b=pygame.image.load('textures/pieces/rook_b.png')
    pawn_w=pygame.image.load('textures/pieces/pawn_w.png')
    pawn_b=pygame.image.load('textures/pieces/pawn_b.png')
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


def events():
    global mouseloc, loop, dataloop, mx, my, pick, current
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            if loop == True:
                dataloop.cancel()
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            mouseloc=pygame.mouse.get_pos()
            if mouseloc[0] < 800 and pick == True:
                mx=int(math.ceil(mouseloc[0] / 100.0)) * 100 -100           #finds the top left corner of a square
                my=int(math.ceil(mouseloc[1] / 100.0)) * 100 -100
                current=board[int(my/100)][int(mx/100)]
                pick = False
            elif mouseloc[0] < 800 and pick == False:
                mx2=int(math.ceil(mouseloc[0] / 100.0)) * 100 -100           #finds the top left corner of a square
                my2=int(math.ceil(mouseloc[1] / 100.0)) * 100 -100
                print(current)
                board[int(my/100)][int(mx/100)]=0
                board[int(my2/100)][int(mx2/100)]=str(current)
                pick = True
                #s.send(str(board).encode())


def draw():
    global board, chess_board, pieces_lst, mouseloc, pick
    clock.tick(60)
    g.blit(chess_board, (0,0))
    if pick == False:
        pygame.draw.rect(g,(0,180,0),[mx, my,100,100],4)
    for piece in range(12):
        for row in range(8):
            for column in range(8):
                if board[column][row]==str(piece+1):
                    pass
                    g.blit(pieces_lst[piece], ((row*100)+25,(column*100)+25))
    pygame.draw.rect(g, (240,230,140), [800,0,200,800],0)
    fps = font.render(str(int(clock.get_fps()))+" FPS", True, pygame.Color('Red'))
    g.blit(fps, [800,0])
    pygame.display.flip()

def commline():
    global dataloop, board
    dataloop = threading.Timer(0, commline)
    data=(s.recv(1024).decode())
    print(data)
    if '[' in data:
        board = ast.literal_eval(ast.literal_eval(repr(data)))
    dataloop.start()


import_images()
piece_pos()
#commline()
#loop = True
while True:
    events()
    draw()
    









