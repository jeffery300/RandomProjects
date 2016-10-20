#Jeffery Liu AI Semester 2 Stueben
#Rules of Othello: http://radagast.se/othello/Help/strategy.html
##############################################<START OF PROGRAM>##############################################
def setUpCanvas(root): # These are the REQUIRED magic lines to enter graphics mode.
    root.title("A Tk/Python Graphics Program") # Your screen size may be different from 1270 x 780.
    canvas = Canvas(root, width = 1270, height = 780, bg = 'GREY30')
    canvas.pack(expand = YES, fill = BOTH)
    return canvas
#----------------------------------------------------------------------------------------------------Othello--

def createMatrix(): # = the initial position, with Black = 1, and white = -1.
    M = [ [0, 0, 0, 0, 0, 0, 0, 0,],
          [0, 0, 0, 0, 0, 0, 0, 0,],
          [0, 0, 0, 0, 0, 0, 0, 0,],
          [0, 0, 0,-1, 1, 0, 0, 0,], # The matrix M is GLOBAL.
          [0, 0, 0, 1,-1, 0, 0, 0,],
          [0, 0, 0, 0, 0, 0, 0, 0,],
          [0, 0, 0, 0, 0, 0, 0, 0,],
          [0, 0, 0, 0, 0, 0, 0, 0,],]
    return M
#----------------------------------------------------------------------------------------------------Othello---

def initializePointMatrices():
    global PW, PB
##--The computer's strategy will be based off of this GLOBAL matrix, which will be modified as
#   the board configuration changes. Remember: row (going down) is first:  P[row][col]
    PW = [ [1000,  100,  100,  100,  100,  100,  100, 1000,], # P[0][0], P[0][1], ..., P[0][7]
           [ 100,  -40,  -10,  -10,  -10,  -10,  -40,  100,], # P[1][0], P[1][1], ..., P[1][7]
           [ 100,  -10,    1,    1,    1,    1,  -10,  100,], # P[2][0], P[2][1], ..., P[2][7]
           [ 100,  -10,    1,    1,    1,    1,  -10,  100,], # P[3][0], P[3][1], ..., P[3][7]
           [ 100,  -10,    1,    1,    1,    1,  -10,  100,], # P[4][0], P[4][1], ..., P[4][7]
           [ 100,  -10,    1,    1,    1,    1,  -10,  100,], # P[5][0], P[5][1], ..., P[5][7]
           [ 100,  -40,  -10,  -10,  -10,  -10,  -40,  100,], # P[6][0], P[6][1], ..., P[6][7]
           [1000,  100,  100,  100,  100,  100,  100, 1000,],]# P[7][0], P[7][1], ..., P[7][7]
    from copy import deepcopy
    PB = deepcopy(PW)
    return PW, PB
#---------------------------------------------------------------------------------------------------Othello--

def updateTheFourCorners():
    global PW, PB
#---1B. Modify upper-left corner cell's values if the HUMAN has taken that corner.
    if M[0][0] == 1:
        if M[0][2] in [0,-1]: PW[0][1] = -50 # bad  move for white (computer)
        if M[2][0] in [0,-1]: PW[1][0] = -50 # bad  move for white (computer)
        PW[1][1] = -50                       # bad  move for white (computer)
        PB[1][1] = 100                       # good move for black (human)

#---2B. Modify upper-right corner cell's values if the HUMAN has taken that corner.
    if M[0][7] == 1:
        if M[0][5] in [0,-1]: PW[0][6] = -50 # bad  move for white (computer)
        if M[2][7] in [0,-1]: PW[1][7] = -50 # bad  move for white (computer)
        PW[1][6] = -50                       # bad  move for white (computer)
        PB[1][6] = 100                       # good move for black (human)

#---3B. Modify lower-left corner cell's values if the HUMAN has taken that corner.
    if M[7][0] == 1:
        if M[5][0] in [0,-1]: PW[6][0] = -50 # bad  move for white (computer)
        if M[7][2] in [0,-1]: PW[7][1] = -50 # bad  move for white (computer)
        PW[6][1] = -50                       # bad  move for white (computer)
        PB[6][1] = 100                       # good move for black (human)

#---4B. Modify lower-right corner cell's values if the HUMAN has taken that corner.
    if M[7][7] == 1:
        if M[7][5] in [0,-1]: PW[7][6] = -50 # bad  move for white (computer)
        if M[5][7] in [0,-1]: PW[6][7] = -50 # bad  move for white (computer)
        PW[6][6] = -50                       # bad  move for white (computer)
        PB[6][6] = 100                       # good move for black (human)
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#---1W. Modify upper-left corner cell's values if the COMPUTER has taken that corner.
    if M[0][0] == -1:
        if M[0][2] in [0,1]: PB[0][1] = -50 # bad  move for black (human)
        if M[2][0] in [0,1]: PB[1][0] = -50 # bad  move for black (human)
        PB[1][1] = -50                      # bad  move for black (human)
        PW[1][1] = 100                      # good move for white (computer)

#---2W. Modify upper-right corner cell's values if the COMPUTER has taken that corner.
    if M[0][7] == -1:
        if M[0][5] in [0,1]: PB[0][6] = -50 # bad  move for black (human)
        if M[2][7] in [0,1]: PB[1][7] = -50 # bad  move for black (human)
        PB[1][6] = -50                      # bad  move for black (human)
        PW[1][6] = 100                      # good move for white (computer)

#---3W. Modify lower-left corner cell's values if the COMPUTER has taken that corner.
    if M[7][0] == -1:
        if M[5][0] in [0,1]: PB[6][0] = -50 # bad  move for black (human)
        if M[7][2] in [0,1]: PB[7][1] = -50 # bad  move for black (human)
        PB[6][1] = -50                      # bad  move for black (human)
        PW[6][1] = 100                      # good move for white (computer)

#---4W. Modify lower-right corner cell's values if the COMPUTER has taken that corner.
    if M[7][7] == -1:
        if M[7][5] in [0,1]: PB[7][6] = -50 # bad  move for black (human)
        if M[5][7] in [0,1]: PB[6][7] = -50 # bad  move for black (human)
        PB[6][6] = -50                      # bad  move for black (human))
        PW[6][6] = 100                      # good move for white (computer)
#----------------------------------------------------------------------------------------------------Othello--

def updateTheMiddleRowsAndColumns():
    global PW, B
    for n in range (2, 6):
        if M[0][n] == -1:
            PW[1][n] =  20 # TOP    row
            PB[1][n] = -10 # TOP    row
        if M[7][n] == -1:
            PW[6][n] =  20 # BOTTOM row
            PB[6][n] = -10 # BOTTOM row
        if M[n][0] == -1:
            PW[n][1] =  20 # LEFT  column
            PB[n][1] = -10 # LEFT  column
        if M[n][7] == -1:
            PW[n][6] =  20 # RIGHT column
            PB[n][6] = -10 # RIGHT column
        if M[0][n] == 1:
            PW[1][n] = -10 # TOP    row
            PB[1][n] =  20 # TOP    row
        if M[7][n] == 1:
            PW[6][n] = -10 # BOTTOM row
            PB[6][n] =  20 # BOTTOM row
        if M[n][0] == 1:
            PW[n][1] = -10 # LEFT  column
            PB[n][1] =  20 # LEFT  column
        if M[n][7] == 1:
            PW[n][6] = -10 # RIGHT column
            PB[n][6] =  20 # RIGHT column
#----------------------------------------------------------------------------------------------------Othello--

def updateThePointMatrices():
    updateTheFourCorners()
    updateTheMiddleRowsAndColumns()
#----------------------------------------------------------------------------------------------------Othello--






def copyMatrixToScreen():
    canvas.create_text(30,30, text="x", fill = 'BLACK', font = ('Helvetica',1))
    for r in range (8):
       for c in range (8):
        if M[r][c] ==  1:
           sx = c*70 + 85
           sy = r*70 + 105
           canvas.create_oval(sx-25,sy-25, sx+25, sy+25, fill = 'BLACK')
        if M[r][c] == -1:
           sx = c*70 + 85
           sy = r*70 + 105
           canvas.create_oval(sx-25,sy-25, sx+25, sy+25, fill = 'WHITE')
    canvas.update()
#----------------------------------------------------------------------------------------------------Othello--

def showComputersMovesInRedOnScreen (r, c, pieces):
#---If white just moved, then make that stone red
    sy = r*70 + 105
    sx = c*70 + 85
    canvas.create_oval(sx-15,sy-15, sx+15, sy+15, fill = 'RED')

#------Turn any black stones pink if they are about to be about to be turned over.
    for r,c in pieces:
           sy = r*70 + 105
           sx = c*70 + 85
           canvas.create_oval(sx-15,sy-15, sx+15, sy+15, fill = 'PINK')
    canvas.update()
    sleep(PAUSE_TIME)
#----------------------------------------------------------------------------------------------------Othello--

def copyOldBoardToScreenInMiniaturizedForm(rr, cc):
 #--erase previous miniature board
    canvas.create_rectangle(650, 400, 821, 567, width = 5, fill    = 'GRAY30')
    ch = chr(9679)
    for r in range (8):
       for c in range (8):
        sx = c*20 + 665
        sy = r*20 + 412
        if M[r][c] ==  1:
           canvas.create_text(sx, sy, text = ch, fill = 'BLACK', font = ('Helvetica', 20, 'bold') )
        if M[r][c] == -1:
           canvas.create_text(sx, sy, text = ch, fill = 'WHITE', font = ('Helvetica', 20, 'bold') )

    canvas.create_text(cc*20 + 665, rr*20 + 413, text = 'B', fill = 'BLACK', \
                             font = ('Helvetica', 9, 'bold') )
    canvas.update()      # make all previous changes to the canvas
#----------------------------------------------------------------------------------------------------Othello--

def score(): # returns the number of black and white disks.
    whiteTotal = 0; blackTotal = 0
    for r in range(8):
      for c in range (8):
        if M[r][c] ==  1: blackTotal += 1
        if M[r][c] == -1: whiteTotal += 1
    return (blackTotal, whiteTotal)
#----------------------------------------------------------------------------------------------------Othello--

def printMatrices(): # <-- This function prints the matrices M , PW, and PB to the console for debugging.
    print('\n Matrix M')
    print ('     0  1  2  3  4  5  6  7')
    print ('  +--------------------------+')







    for r in range(8):
      print (r, '|', end = '')
      for c in range (8):
         if M[r][c] == 1: ch = '#'
         if M[r][c] ==-1: ch = 'O'
         if M[r][c] == 0: ch = '-'
         if M[r][c] not in {-1,0,1}: ch = '?'
         print ("%3s"%ch, end = '')
      print ("  |")
    print ('  +--------------------------+')
    print ('  |human    = # = BLACK  =  1|')
    print ('  |computer = O = WHITE  = -1|')
    print ('  +--------------------------+')
    print ('M[3][0] =', M[3][0])
#   ------------------------------------------------
    print('\n Matrix PW')
    print ('      0    1    2    3    4    5    6    7')
    print ('  +------------------------------------------+')
    for r in range(8):
      print (r, '|', end = '')
      for c in range (8):
         print ("%5d"%PW[r][c], end = '')
      print ("  |")
    print ('  +------------------------------------------+')
#   ------------------------------------------------
    print('\n Matrix PB')
    print ('      0    1    2    3    4    5    6    7')
    print ('  +------------------------------------------+')
    for r in range(8):
      print (r, '|', end = '')
      for c in range (8):
         print ("%5d"%PB[r][c], end = '')
      print ("  |")
    print ('  +------------------------------------------+')
#----------------------------------------------------------------------------------------------------Othello--

def LocateTurnedPieces(r, c, player): # The pieces turned over are of -player's color. A zero in a
    if M[r][c] != 0: return []        # matrix M cell means an empty cell. This function does NOT
    totalFlipped =   []               # turn any pieces over.
 #--case 1 (move right)
    flipped = []
    if c < 6 and M[r][c+1] == -player:
        for n in range(1, 9):
            if c+n > 7 or M[r][c+n] == 0:
                flipped = []
                break
            if M[r][c+n] == player: break
            flipped += ((r,c+n,),)  # <-- We save the cell locations as tuples.
    totalFlipped += flipped

 #--case 2 (move down)
    flipped = []
    if r < 6 and M[r+1][c] == -player:
        for n in range(1, 9):
            if r+n > 7 or M[r+n][c] == 0:
                flipped = []
                break
            if M[r+n][c] == player: break
            flipped += ((r+n,c,),)
    totalFlipped += flipped








 #--case 3 (move up)
    flipped = []
    if r > 1 and M[r-1][c  ] == -player:
        for n in range(1, 9):
            if r-n < 0 or M[r-n][c] == 0:
                flipped = []
                break
            if M[r-n][c] == player: break
            flipped += ((r-n,c,),)
    totalFlipped += flipped

 #--case 4 (move left)
    flipped = []
    if c > 1 and M[r][c-1] == -player:
        for n in range(1, 9):
            if c-n < 0 or M[r][c-n] == 0:
                flipped = []
                break
            if M[r][c-n] == player: break
            flipped += ((r,c-n,),)
    totalFlipped += flipped

 #--case 5 (move down and right)
    flipped = []
    if r < 6 and c < 6 and M[r+1][c+1] == -player:
        for n in range(1, 9):
            if (r+n) > 7 or (c+n) > 7 or M[r+n][c+n] == 0:
                flipped = []
                break
            if M[r+n][c+n] == player: break
            flipped += ((r+n,c+n,),)
    totalFlipped += flipped

 #--case 6 (move up and left)
    flipped = []
    if r > 0 and c > 0 and M[r-1][c-1] == -player:
        for n in range(1, 9):
            if (r-n) < 0 or (c-n) < 0 or M[r-n][c-n] == 0:
                flipped = []
                break
            if M[r-n][c-n] == player: break
            flipped += ((r-n,c-n,),)
    totalFlipped += flipped

#--case 7 (move up and right)
    flipped = []
    if r > 1 and c < 6 and M[r-1][c+1] == -player:
        for n in range(1, 9):
            if (r-n) < 0 or (c+n) > 7 or M[r-n][c+n] == 0:
                flipped = []
                break
            if M[r-n][c+n] == player: break
            flipped += ((r-n,c+n,),)
    totalFlipped += flipped

 #--case 8 (move down and left)
    flipped = []
    if r < 6 and c > 1 and M[r+1][c-1] == -player:
        for n in range(1, 9):
            if (r+n) > 7 or (c-n) < 0 or M[r+n][c-n] == 0:
                flipped = []
                break
            if M[r+n][c-n] == player: break
            flipped += ((r+n,c-n,),)
    totalFlipped += flipped

    return totalFlipped
#----------------------------------------------------------------------------------------------------Othello--
def setUpInitialBoard():
    ch = chr(9679)
    M  = createMatrix()
 #--print title
    canvas.create_text(330, 50, text = "OTHELLO with AI", \
                       fill = 'WHITE',  font = ('Helvetica', 20, 'bold'))
 #--print directions
    stng = "DIRECTIONS:\n1) Black (human) moves first. Click on any unoccupied cell.\n\
2) If a player cannot move, play passes to the opponent. \n3) Game ends when \
no legal move is possible.\n4) The player with the most colors on the board \
wins.\n5) A legal move MUST cause some pieces to turn color."
    canvas.create_text(810, 100, text = stng,  \
                       fill = 'WHITE',  font = ('Helvetica', 10, 'bold'))
 #--draw outer box, with red border
    canvas.create_rectangle(50, 70, 610, 630, width = 1, fill    = 'DARKGREEN')
    canvas.create_rectangle(47, 67, 612, 632, width = 5, outline = 'RED'  )

 #--Draw 7 horizontal and 7 vertical lines to make the cells
    for n in range (1, 8): # draw horizontal lines
       canvas.create_line(50, 70+70*n, 610, 70+70*n, width = 2, fill = 'BLACK')
    for n in range (1, 8):# draw vertical lines
       canvas.create_line(50+70*n,  70, 50+70*n, 630, width = 2, fill = 'BLACK')

 #--Place gold lines to indicate dangerous area to play (optional).
    canvas.create_rectangle(47+73, 67+73, 612-73, 632-73, width = 1, outline = 'GOLD'  )
    canvas.create_rectangle(47+2*71, 67+2*71, 612-2*71, 632-2*71, width = 1, outline = 'GOLD'  )

 #--Place letters at bottom
    tab = " " * 7
    stng = 'a' + tab + 'b' + tab + 'c' + tab + 'd' + tab + 'e' + \
                 tab + 'f' + tab + 'g' + tab + 'h'
    canvas.create_text(325, 647, text = stng, fill = 'DARKBLUE',  font = ('Helvetica', 20, 'bold'))

 #--Place digits on left side
    for n in range (1,9):
        canvas.create_text(30, 35 + n * 70, text = str(n),
                       fill = 'DARKBLUE',  font = ('Helvetica', 20, 'bold'))
 #--copy matrix to screen.
    copyMatrixToScreen()

 #--Place score on screen
    (BLACK, WHITE) = score()
    stng = 'BLACK = ' + str(BLACK) + '\nWHITE  = ' + str(WHITE)
    canvas.create_text(800, 200, text = stng, fill = 'WHITE',  font = ('Helvetica', 20, 'bold'))
    return M
#----------------------------------------------------------------------------------------------------Othello--

def illegalClick(x, y): # Click is not on board or click is on an already-filled cell.
    player = 1 # player = Black
    if x < 52 or x > 609:
        print("Error 1. Mouse is to left or right of board.")
        return True # = mouse position is off the board

    if y < 62 or y > 632:
        print("Error 2.Mouse is above or below the board.")
        return True # = mouse position is off the board

 #--Calculate matrix position
    c = (x-50)//70
    r = (y-70)//70

    if M[r][c] != 0:
        print("ERROR 3: Cell is occupied at r =", r, " c =", c)
        return True      # = cell is occupied




 #--Not next to cell of opposite color
    flag = 0
    if c < 7 and           M[r  ][c+1] == -player: return False
    if r < 7 and           M[r+1][c  ] == -player: return False
    if r > 0 and           M[r-1][c  ] == -player: return False
    if c > 0 and           M[r  ][c-1] == -player: return False
    if r < 7 and c < 7 and M[r+1][c+1] == -player: return False
    if r > 0 and c > 0 and M[r-1][c-1] == -player: return False
    if r > 0 and c < 7 and M[r-1][c+1] == -player: return False
    if r < 7 and c > 0 and M[r+1][c-1] == -player: return False
    print("ERROR 4: no opposite colored neighbors at r =", r, " c =", c)
    return True # = illegal move
#----------------------------------------------------------------------------------------------------Othello--

def legalMove(player): # Check to see if any pieces will be turned over.
    pieces = []
    for r in range(8):
        for c in range(8):
           pieces += LocateTurnedPieces(r, c, player)
        if pieces != []: break
    if pieces ==[]:
       person = 'WHITE'
       if player == 1: person = 'BLACK'
       stng = 'There is no legal move for ' + person
       canvas.create_rectangle(655,260,957,307, width = 0, fill = 'GRAY30')
       canvas.create_text     (800,280,text = stng, fill = 'RED',  font = ('Helvetica', 10, 'bold'))
       return False
    return True
#----------------------------------------------------------------------------------------------------Othello--

def makeMove(r, c, pieces, player):
    global M
    if player not in [1, -1]: exit('ERROR: BAD PLAYER'+ str(player))
    if pieces == []: return
 #--make the player's legal move in matrix
    M[r][c] = player

    if player == COMPUTER:
        showComputersMovesInRedOnScreen(r, c, pieces)

 #--flip pieces to same color as the player
    for elt in pieces:
        M[elt[0]][elt[1]] = player

#--update the screen
    copyMatrixToScreen()

 #--erase old score and previous move
    canvas.create_rectangle(650, 160, 960, 310, width = 5, fill    = 'GRAY30')

 #--print new score
    (BLACK, WHITE) = score()
    stng = 'BLACK = ' + str(BLACK) + '\nWHITE  = ' + str(WHITE)
    canvas.create_text(800, 200, text = stng, \
                       fill = 'WHITE',  font = ('Helvetica', 20, 'bold'))

 #--print previous move on miniature board
    position = "previous move: "+ str(chr(c + 97))+str(r+1)
    canvas.create_text(800, 250, text = position, \
                       fill = 'WHITE',  font = ('Helvetica', 20, 'bold'))

    if player == COMPUTER:
       canvas.create_text(c*20 + 665, r*20 + 413, text = 'W', fill = 'WHITE', \
                             font = ('Helvetica', 9, 'bold') )
#----------------------------------------------------------------------------------------------------Othello--



def quit():
    canvas.create_text(330, 350, text = "GAME OVER", \
                       fill = 'RED',  font = ('Helvetica', 40, 'bold'))
    stng = 'THERE ARE NO LEGAL MOVES FOR EITHER PLAYER.'
    canvas.create_rectangle(655, 260, 955, 300, width = 0, fill = 'GRAY30')
    canvas.create_text(805, 280, text = stng, fill = 'GOLD',  font = ('Helvetica', 9, 'bold'))
#----------------------------------------------------------------------------------------------------Othello--

def totalPointsGainedFromFlippingPieces(player, r, c, pieces):
    if player == COMPUTER:
       total = PW[r][c]          # total = the points associated with the piece played on the board.
       for (rr,cc) in pieces:
           total += PW[rr][cc]   # Add the values associated with the flipped pieces.
       return total
    if player == HUMAN:
       total = PB[r][c]          # total = the points associated with the piece played on the board.
       for (rr,cc) in pieces:
           total += PB[rr][cc]   # Add the values associated with the flipped pieces.
       return total
    exit('ERROR in totalPointsGainedFromFlippingPieces() player = ' + str(player))
#----------------------------------------------------------------------------------------------------Othello--

def displayAllLegalMovesForHumanPlayer(kolor):
    for r in range(0, 8):
        for c in range(0, 8):
           kkolor = kolor
           if M[r][c] == 0:
              total  = len(LocateTurnedPieces(r, c, HUMAN))
           if M[r][c] == 0 and total != 0:
              sy = r*70 + 109
              sx = c*70 + 85
              if r == 0 or c == 0 or r == 7 or c == 7: kkolor = kolor
              canvas.create_text(sx, sy, text = str(total), fill = kkolor, \
                                 font = ('Helvetica', 15, 'bold') )
#----------------------------------------------------------------------------------------------------Othello--

def printTimeSpentThinking(startTime, player):
    assert player in {COMPUTER, HUMAN}
    if player == COMPUTER:
       msg = 'computer thinks for ' + str(round(clock() - startTime - PAUSE_TIME, 2)) + ' seconds'
    if player == HUMAN:
       msg = 'human thinks for '  + str(round(clock() - startTime, 2)) + ' seconds'
    canvas.create_rectangle(650, 340, 950, 365, width = 0, fill = 'GRAY30')
    canvas.create_text(800, 352, text = msg, fill = 'WHITE',  font = ('Helvetica', 12, 'bold'))
#----------------------------------------------------------------------------------------------------Othello--

def boardScore(player):
   assert player == HUMAN
   computerTotal = 0
   humanTotal    = 0
   for r in range(0, 8):
        for c in range(0, 8):
            if M[r][c] == COMPUTER:
                computerTotal += PW[r][c]
            if M[r][c] == HUMAN:
                humanTotal += PB[r][c]
   return humanTotal - computerTotal
#----------------------------------------------------------------------------------------------------Othello--

def makeTheMoveAndTurnOverThePieces(r, c, piecesTurnedOver, player):
    global M

#---Double check that our move is made to an empty cell.
    assert M[r][c] == 0, ['player =', str(player)]

#---Make the move
    M[r][c] = player

#---Double check that the pieces we are turning over are of the opposite color of our player.
    piecesAreOppositeColorOfPlayer = True
    for (r,c) in piecesTurnedOver:
        if M[r][c] != -player:
           piecesAreOppositeColorOfPlayer = False
    assert piecesAreOppositeColorOfPlayer == True

#---Turn the pieces over.
    for (r,c) in piecesTurnedOver:
        M[r][c] = player
#----------------------------------------------------------------------------------------------------Othello--

def takeBackTheMoveAndTurnBackOverThePieces(r, c, piecesTurnedOver, player):
    global M
#---Double check that we are turning back a piece with the same color as player.
    assert M[r][c] == player, ['player =', str(player), 'M[r][c] =', M[r][c], '(r,c) =', (r,c)]

#---Take the move back.
    M[r][c] = 0

#---Double check that the pieces we are turning over are of the same color of our player.
    piecesAreSameColorAsPlayer = True
    for (r,c) in piecesTurnedOver:
        if M[r][c] != player:
           piecesAreSameColorAsPlayer = False
    assert piecesAreSameColorAsPlayer == True

#---Turn the pieces back over.
    for (r,c) in piecesTurnedOver:
        M[r][c] = -player
#----------------------------------------------------------------------------------------------------Othello--

def click(evt): # A legal move is guaranteed to exist.
    displayAllLegalMovesForHumanPlayer('DARKGREEN')

 #--Erase computer's thinking time as computer starts to think about the next move
    canvas.create_rectangle(650, 340, 950, 365, width = 0, fill = 'GREY30')

 #--If move is off board, or cell full, or no opp. neighbor, then CLICK AGAIN.
    if illegalClick(evt.x, evt.y):
        canvas.create_rectangle(660, 270, 940,300, width = 0, fill = 'GRAY30')
        stng = 'Your last mouse click was an ILLEGAL MOVE.'
        canvas.create_text(800, 280, text = stng, fill = 'RED',  font = ('Helvetica', 9, 'bold'))
        return

 #--Find matrix coordinates (c,r) in terms of mouse coordinates (evt.x, evt.y).
    r = (evt.y-70)//70
    c = (evt.x-50)//70

 #--if none of the computer's pieces will be turned, then CLICK AGAIN.
    pieces     = LocateTurnedPieces(r, c, HUMAN)
    if pieces == []:
       canvas.create_rectangle(660, 270, 940,300, width = 0, fill = 'GRAY30')
       stng = 'Your last mouse click did NOT turn a piece.'
       canvas.create_text(800, 280, text = stng, fill = 'ORANGE',  font = ('Helvetica', 9, 'bold'))
       displayAllLegalMovesForHumanPlayer('YELLOW')
       return

 #--Make human move(s) and computer reply/replies.
    copyOldBoardToScreenInMiniaturizedForm(r, c)
    makeMove(r, c, pieces, HUMAN)
##    printTimeSpentThinking(startTime, HUMAN)
    if legalMove(HUMAN) and not legalMove(COMPUTER): return





 #--Make computer reply/replies (1 = BLACK = human, -1 = computer = WHITE)
    if legalMove(COMPUTER):
        startTime = clock()
        bestRow, bestCol, finalPieces = computersMove(DEPTH, COMPUTER) # <<<<<<<<<<<<<<<<<<<<<<<<<<<<REMOVE X
        makeMove(bestRow, bestCol, finalPieces, COMPUTER)
        printTimeSpentThinking(startTime, COMPUTER)

    while legalMove(COMPUTER) and not legalMove(HUMAN):
        startTime = clock()
        bestRow, bestCol, finalPieces = computersMove(DEPTH, COMPUTER) # <<<<<<<<<<<<<<<<<<<<<<<<<<<<REMOVE X
        makeMove(bestRow, bestCol, finalPieces, COMPUTER)
        printTimeSpentThinking(startTime, COMPUTER)
    displayAllLegalMovesForHumanPlayer('RED')
    startTime = clock()
    if not legalMove(HUMAN) and not legalMove(COMPUTER): quit()

 #-- Note: legal move for human must now necessarily exist.
    return
#----------------------------------------------------------------------------------------------------Othello--

def computersMoveX(depth, player):
    updateThePointMatrices()
#--Make a move that picks up the most points using the point matrix (P).
    bestRow = -1
    bestCol = -1
    maxTotal = -1000
    for r in range(0, 8):
        for c in range(0, 8):
           if M[r][c] == 0:
              pieces = LocateTurnedPieces(r, c, COMPUTER)
              if len(pieces) == 0:
                 continue
              total = totalPointsGainedFromFlippingPieces(COMPUTER, r, c, pieces)
              if maxTotal < total:
                 maxTotal = total
                 bestRow = r
                 bestCol = c
                 finalPieces = pieces
    return(bestRow, bestCol, finalPieces)
#----------------------------------------------------------------------------------------------------Othello--
# Note well: This function begins by creating board positions. It also keeps the (row, col) move associated
#            with each board position. The maxValue and minValue functions do not need to remember the (row,
#            col) moves associated with the positions they create. This function ALWAYS begins with calling
#            the maxValue function, no matter if the ply is even or odd.
def computersMove(depth, player):
    depth = depth-1
    beta = float('inf')
    alpha = float('-inf')
    global M
    setOfMoveValuesAndMoves = []   
    for r in range (8):
      for c in range(8):
        if M[r][c] != 0:
          continue
        setofPieces = LocateTurnedPieces(r,c,player)
        if not setofPieces:
          continue
        makeTheMoveAndTurnOverThePieces(r,c,setofPieces,player)
        setOfMoveValuesAndMoves.append((maxValue(depth-1,-player),r,c))
        takeBackTheMoveAndTurnBackOverThePieces(r,c,setofPieces,player)
    value,bestRow,bestCol = min(setOfMoveValuesAndMoves)
    return bestRow,bestCol, LocateTurnedPieces(bestRow,bestCol,player)
 
#----------------------------------------------------------------------------------------------------Othello--

def maxValue(depth, player): # Return the MAXIMUM value of the boards created by appending black moves.
#---Initialize and check assertions.
    global M
    assert player  == HUMAN
    setOfMoveValuesAndMoves = [] 
    if depth == 0:
      return baseCaseForEvenPlyDepth(depth,player)
    for r in range (8):
      for c in range(8):
        if M[r][c] != 0:
          continue
        setofPieces = LocateTurnedPieces(r,c,player)
        if not setofPieces:
          continue
        makeTheMoveAndTurnOverThePieces(r,c,setofPieces,player)
        setOfMoveValuesAndMoves.append(minValue(depth-1,-player))
        takeBackTheMoveAndTurnBackOverThePieces(r,c,setofPieces,player)
    if setOfMoveValuesAndMoves == []:
        return boardScore(player)
    maxVal = max(setOfMoveValuesAndMoves)
    return maxVal


#----------------------------------------------------------------------------------------------------Othello--
# Return the MINIMUM value of the boards created by appending white moves. Remember, the higher the value,
# the better for black.
def minValue(depth, player):
#---Initialize and check assertions.
    global M
    assert player == COMPUTER # = white
    setOfMoveValuesAndMoves = [] 
    if depth == 0:
      return baseCaseForOddPlyDepth(depth,player)
    for r in range (8):
      for c in range(8):
        if M[r][c] != 0:
          continue
        setofPieces = LocateTurnedPieces(r,c,player)
        if not setofPieces:
          continue
        makeTheMoveAndTurnOverThePieces(r,c,setofPieces,player)
        setOfMoveValuesAndMoves.append(maxValue(depth-1,-player))
        takeBackTheMoveAndTurnBackOverThePieces(r,c,setofPieces,player)
    if setOfMoveValuesAndMoves == []:
        return boardScore(player)
    minVal = min(setOfMoveValuesAndMoves)
    return minVal
      # 3. WRITE THIS FUNCTION
#----------------------------------------------------------------------------------------------------Othello--



# Note that this function is identical to the maxValue function (and is called from the maxValue function),
# except that it does not get its points from its children. Instead, it uses an evaluation function. Why
# return the maximum? The higher the score the better for black.
def baseCaseForEvenPlyDepth(depth, player):
#---Initialize and check assertions.
    global M
    assert depth == 0, [depth]
    updateThePointMatrices()
    maxPlayerValue = float('-inf')     
  # currentPlayerValue = boardScore(player)
    for r in range (8):
      for c in range(8):
        if M[r][c] != 0:
          continue
        setofPieces = LocateTurnedPieces(r,c,player)
        if not setofPieces:
          continue
        makeTheMoveAndTurnOverThePieces(r,c,setofPieces,player)
        if boardScore(player) > maxPlayerValue:
          maxPlayerValue = boardScore(player)
        takeBackTheMoveAndTurnBackOverThePieces(r,c,setofPieces,player)
    return maxPlayerValue

 # 4. WRITE THIS FUNCTION
#----------------------------------------------------------------------------------------------------Othello--

#  This function is identical to the minValue function (and is called from the minValue function), except that
#  it does not get its points from its children. Instead, it uses an evaluation function.
def baseCaseForOddPlyDepth(depth, player):
    global M
    assert depth == 0, [depth]
    updateThePointMatrices()
    minPlayerValue = float('inf')
    currentPlayerValue = boardScore(-player) 
    for r in range (8):
      for c in range(8):
        if M[r][c] != 0:
          continue
        setofPieces = LocateTurnedPieces(r,c,player)
        if not setofPieces:
          continue
        makeTheMoveAndTurnOverThePieces(r,c,setofPieces,player)
        if boardScore(-player) < minPlayerValue:
            minPlayerValue = boardScore(-player)
        takeBackTheMoveAndTurnBackOverThePieces(r,c,setofPieces,player)
    return minPlayerValue
          # 5. WRITE THIS FUNCTION
#====================================<GLOBAL CONSTANTS and GLOBAL IMPORTS>====================================

from tkinter  import *   # <-- Use Tkinter in Python 2.x
from time     import clock, sleep
PAUSE_TIME =  1.5
root       =  Tk()
canvas     =  setUpCanvas(root)
PW, PB     =  initializePointMatrices() # <-- Global.
M          =  createMatrix()            # <-- Global, because no variable can be passed to the click function.
HUMAN      =  1 # = Black
COMPUTER   = -1 # = White
DEPTH      =  3 # if DEPTH = 5, moves can take between 11-15 seconds.
#===================================================<MAIN>====================================================

def main():
    root.bind('<Button-1>', click) # 1 = LEFT  mouse button calls the click function.
    root.bind('<Button-3>', click) # 3 = RIGHT mouse button calls the click function.
    setUpInitialBoard()
    root.mainloop()                # The window waits for the click function to be called.
#----------------------------------------------------------------------------------------------------Othello--
if __name__ == '__main__':  main()
###############################################<END OF PROGRAM>###############################################


