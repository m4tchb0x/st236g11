import csv
from copy import deepcopy

groupNumber = 11
groupName = {'Vihar Reddy' : '5715484',\
             'Maciej Wdowin' : '5682215',\
             'Emilyne Mohd Ruzaimi' : '5725919',\
             'Oliver Stevens' : '5685258'}


###############################################################################
## Task 1

def newEmptyGame(p1, p2, ShowSubs=[]):
    '''
    Input:  p1       [str]  name of Player 1
            p2       [str]  name of Player 2
            ShowSubs [list] which players' submarines are printed after each
                            move: [], [1], [2] or [1, 2]. Default is [].

    Output: [dict] a new game dictionary with the keys 'Player 1', 'Player 2',
            'Who', 'ShowSubs', 'Player 1 Board' and 'Player 2 Board'.
            Both boards are 5x5x5 lists filled with 0 (no submarines, hits or
            misses) and Player 1 moves first.

    Exceptions: [none]
    '''
    # board[k][j][i]: k is the level, j is the row and i is the column
    board1 = [[[0 for i in range(5)] for j in range(5)] for k in range(5)]
    board2 = deepcopy(board1)   # a separate copy so the boards share nothing

    return {'Player 1' : p1,
            'Player 2' : p2,
            'Who' : 1,
            'ShowSubs' : list(ShowSubs),
            'Player 1 Board' : board1,
            'Player 2 Board' : board2}

###############################################################################


###############################################################################
# Task 2

class OutOfBoundsError(Exception):
    '''Raised when a cube, or part of a submarine, is not on the board.'''
    pass


class InvalidInputFormat(Exception):
    '''Raised when an input is not of the form the function expects.'''
    pass


def posToIndex(place):
    '''
    Input:  place [str] a cube reference made of one letter in {a,b,c,d,e}
                        (row), one letter in {A,B,C,D,E} (column) and one digit
                        in {1,2,3,4,5} (level), in any order,
                        e.g. 'Aa1', 'aA1' and '1Aa' all mean the same cube.

    Output: [list] [i, j, k] of integers in 0-4 such that the state of the
            cube is board[k][j][i]. i comes from the capital letter,
            j from the lower case letter and k from the digit (minus 1).

    Exceptions: InvalidInputFormat if place is not a string, is not exactly
                                   three characters long, or does not contain
                                   exactly one lower case letter, one capital
                                   letter and one digit.
                OutOfBoundsError   if place has the right format but the cube
                                   is not on the board, e.g. 'Fa1' or 'Aa6'.
    '''
    if not isinstance(place, str) or len(place) != 3:
        raise InvalidInputFormat('place must be a string of three characters.')

    # split the three characters into lower case letters, capitals and digits
    lower = [c for c in place if 'a' <= c <= 'z']
    upper = [c for c in place if 'A' <= c <= 'Z']
    digit = [c for c in place if '0' <= c <= '9']
    if len(lower) != 1 or len(upper) != 1 or len(digit) != 1:
        raise InvalidInputFormat('place needs one letter in a-e, one in A-E '
                                 'and one digit.')

    i = 'ABCDE'.find(upper[0])    # -1 if the letter is not in A-E
    j = 'abcde'.find(lower[0])    # -1 if the letter is not in a-e
    k = int(digit[0]) - 1
    if i == -1 or j == -1 or k < 0 or k > 4:
        raise OutOfBoundsError('That cube is not on the board.')
    return [i, j, k]

###############################################################################


###############################################################################
# Task 3

class SubmarineOverlapError(Exception):
    '''Raised when a submarine would be placed on top of another submarine.'''
    pass


def placeSubs(board, name, pos):
    '''
    Input:  board [list] a 5x5x5 board, indexed board[k][j][i]
            name  [str]  the submarine to place: 'S1', 'S2', 'S3', 'S4' or 'S5'
            pos   [dict] {'anchor' : place, 'direction' : d, 'length' : L}
                         anchor is the cube at one end of the submarine, in
                         the form 'Xxn' (any order, see posToIndex).
                         d is one of 'up', 'down', 'left', 'right', 'forwards'
                         or 'backwards' and is the direction the submarine
                         extends from the anchor ('forwards' moves towards
                         row e, 'backwards' towards row a).
                         L is the number of cubes the submarine occupies.

    Output: [none] board is changed in place: every cube of the submarine is
            set to name. If an exception is raised the board is not changed.

    Exceptions: InvalidInputFormat    if name is not one of 'S1'-'S5', pos is
                                      not a dictionary with the keys above,
                                      the direction is not one of the six
                                      allowed, the length is not a positive
                                      integer, or the anchor is not in the
                                      correct form.
                OutOfBoundsError      if the anchor is not on the board or any
                                      part of the submarine would be off it.
                SubmarineOverlapError if any cube of the submarine is already
                                      occupied.
    '''
    # how [i, j, k] changes for one step in each direction
    directions = {'up' : (0, 0, 1),
                  'down' : (0, 0, -1),
                  'left' : (-1, 0, 0),
                  'right' : (1, 0, 0),
                  'forwards' : (0, 1, 0),
                  'backwards' : (0, -1, 0)}

    if name not in ('S1', 'S2', 'S3', 'S4', 'S5'):
        raise InvalidInputFormat("name must be one of 'S1' to 'S5'.")
    if not isinstance(pos, dict) or \
       any(key not in pos for key in ('anchor', 'direction', 'length')):
        raise InvalidInputFormat("pos must be a dictionary with the keys "
                                 "'anchor', 'direction' and 'length'.")
    if not isinstance(pos['direction'], str) or \
       pos['direction'] not in directions:
        raise InvalidInputFormat('Not a valid direction.')
    if type(pos['length']) is not int or pos['length'] < 1:
        raise InvalidInputFormat('length must be a positive integer.')

    # a bad anchor raises InvalidInputFormat or OutOfBoundsError in posToIndex
    i, j, k = posToIndex(pos['anchor'])
    di, dj, dk = directions[pos['direction']]

    # find every cube first so nothing is written unless the whole sub fits
    cubes = [[i + n*di, j + n*dj, k + n*dk] for n in range(pos['length'])]
    for cube in cubes:
        if min(cube) < 0 or max(cube) > 4:
            raise OutOfBoundsError('The submarine does not fit on the board.')
    for a, b, c in cubes:
        if board[c][b][a] != 0:
            raise SubmarineOverlapError('The submarine overlaps another cube.')

    for a, b, c in cubes:
        board[c][b][a] = name

###############################################################################



###############################################################################
# Task 4

def printBoard(board, showSubs=False, showSubNum=False);
  '''
  Input:  board [list] a 5x5 game board with index [k][j][i].
          showSubs [bool] whether submarines are shown on the board. 
          showSubNum [bool] whether submarine numbers are displayed. 
          Both optional arguments default to False.
          
  Output:  [str] the formatted board showing all 5 layers side by side
           If showSubs is False - unhit submarines are hidden.
           If showSubNum is False - submarine numbers are not displayed.
           Empty cubes are represented by blank spaces.
           
  Expectations: [none] for a valid game board.
  '''
  lines = []
  titles = []
  columns = []
  borders = []

  # Create the headings and rows for each layer
  for k in range(5):
    titles.append(f'{"Layer" + str(k + 1):^17}')
    columns.append('  |A |B |C |D |E ')
    borders.append('--+--+--+--+--+--')

  lines.append(' | '.join(titles))
  lines.append(' | '.join(columns))
  lines.append(' | '.join(borders))

  # Build each row across all five layers
  for j in range(5):
    rows = []
    
    for k in range(5):
      row = 'abcde'[j] + ' |'
      
      for i in range(5):
        cell = board[k][j][i]
        
        if cell == 0:
          display = ''
        elif cell[0] == 'S' and not showSubs:
          display = ''
        elif not showSubNum:
          display = cell[0]
        else:
          display = cell
          
        row += f'{display:<2}|'
        
      rows.append(row[:-1])
      
    lines.append(' | '.join(rows))
    
  return '\n'.join(lines)
      
###############################################################################


###############################################################################
# Task 5

###############################################################################


###############################################################################
# Task 6

###############################################################################


###############################################################################
# Task 7

###############################################################################


###############################################################################
# Task 8

###############################################################################


###############################################################################
# Task 9

###############################################################################


###############################################################################
# Task 10
def isWinner(game):
    '''
    Parameters:
        game: Dictionary which contains keys called 'Player 1 Board' and 'Player 2 Board'.
            Each of the values for those keys is a 5x5x5 3D array.
            At least one of those arrays contains one of the following 'critical strings': 'S1', 'S2', 'S3', 'S4', 'S5'.
    Returns:
        An integer. Either 0 or 1 or 2 depending on the contents of the arrays.
        0 is returned iff both arrays contain any of the critical strings as one of their elements.
        This indicates that neither player has won the game yet.
        1 is returned iff the array with key 'Player 2 Board' doesn't contain any of the critical strings.
        This indicates that player 1 has won the game.
        2 is returned iff only the array with key 'Player 2 Board' contains any of the critical strings.
        This indicates that player 2 has won the game.
      Exceptions:
        None
    '''
    # Set of the strings which indicate that there are still unsunk subs on a player's board
    unsunk = {'S1', 'S2', 'S3', 'S4', 'S5'} 
    # Boolean flags to indicate whether or not a specific player has won yet
    # We can assume that both players have won simultaneously to begin with because at least one of the arrays contains a critical string
    player1win = True
    player2win = True
    # Searches every valid index in the 3D arrays
    for i in range(5):
        for j in range(5):
            for k in range(5):
                # If an element in a board contains any unsunk parts of a sub, then their opponent can't have won yet
                if (game['Player 1 Board'][i][j][k] in unsunk):
                    player2win = False
                if (game['Player 2 Board'][i][j][k] in unsunk):
                    player1win = False
    # Checks the flags and returns the corresponding integer
    if player1win:
        return 1
    elif player2win:
        return 2
    else:
        return 0
###############################################################################


###############################################################################
# Task 11

###############################################################################


###############################################################################
# Task 12

###############################################################################

###############################################################################
# Testing Function
def testFunctionCalls():
    '''
    Input:  [none]
    
    Output: [none]
    
    You can use this function to test if your function names are correct.
    To call the function: "testFunctionCalls()"
    '''
    c = input('The following function will test whether your code can be \
successfully called, i.e. you have used the correct name. \
This function does not test whether the outputs of the functions \
are of the correct type, so passing this function does not \
guarentee that your code will successfully run and you should \
still perform your own checks. \n\nIf you accept these limitations \
type "y" to proceed: ')
    if c == 'y':
        print('You have chosen to proceed.\n\n')
        try:
            newEmptyGame.__doc__
            print('Task 1: Call to "newEmptyGame" successful.\n')
        except:
            print('Task 1: Call to "newEmptyGame" UNSUCCESSFUL.\n')
        
        try:
            posToIndex.__doc__
            print('Task 2: Call to "posToIndex" successful.\n')
        except:
            print('Task 2: Call to "posToIndex" UNSUCCESSFUL.\n')
            
        try:
             OutOfBoundsError()
             print('Task 2: "OutOfBoundsError" found.\n')
        except:
             print('Task 2: "OutOfBoundsError" NOT FOUND.\n')  
            
        try:
             InvalidInputFormat()
             print('Task 2: "InvalidInputFormat" found.\n')
        except:
             print('Task 2: "InvalidInputFormat" NOT FOUND.\n')
            
        try:
            placeSubs.__doc__
            print('Task 3: Call to "placeSubs" successful.')
        except:
            print('Task 3: Call to "placeSubs" UNSUCCESSFUL.')
         
        try:
            SubmarineOverlapError()
            print('Task 3: "SubmarineOverlapError" found.\n')
        except:
            print('Task 3: "SubmarineOverlapError" NOT FOUND.\n')
         
        try:
            printBoard.__doc__
            print('Task 4: Call to "printBoard" successful.')
        except:
            print('Task 4: Call to "printBoard" UNSUCCESSFUL.')
        
        try:
            IndexOutOfRange()
            print('Task 5: "IndexOutOfRange" found.\n')
        except:
            print('Task 5: "IndexOutOfRange" NOT FOUND.\n')
        
        try:
            indexToPos.__doc__
            print('Task 5: Call to "indexToPos" successful.\n')
        except:
            print('Task 5: Call to "indexToPos" UNSUCCESSFUL.\n')
            
        try:
            saveGame.__doc__
            print('Task 6: Call to "saveGame" successful.\n')
        except:
            print('Task 6: Call to "saveGame" UNSUCCESSFUL.\n')
            
        try:
            loadGame.__doc__
            print('Task 7: Call to "loadGame" successful.\n')
        except:
            print('Task 7: Call to "loadGame" UNSUCCESSFUL.\n')
            
        try:
            findValidMoves.__doc__
            print('Task 8: Call to "findValidMoves" successful.')
        except:
            print('Task 8: Call to "findValidMoves" UNSUCCESSFUL.')
        
        try:
            MoveNotMade()
            print('Task 9: "MoveNotMade" found.\n')
        except:
            print('Task 9: "MoveNotMade" NOT FOUND.\n')
        
        try:
            makeMove.__doc__
            print('Task 9: Call to "makeMove" successful.\n')
        except:
            print('Task 9: Call to "makeMove" UNSUCCESSFUL.\n')
            
        try:
            isWinner.__doc__
            print('Task 10: Call to "isWinner" successful.')
        except:
            print('Task 10: Call to "isWinner" UNSUCCESSFUL.')
            
        try:
            suggestMove.__doc__
            print('Task 11: "suggestMove" found.\n')
        except:
            print('Task 11: "suggestMove" NOT FOUND.\n')
            
        try:
            playGame.__doc__
            print('Task 12: Call to "playGame" successful.\n')
        except:
            print('Task 12: Call to "playGame" UNSUCCESSFUL.\n')
    else:
         print('You have chosen not to proceed.')   
###############################################################################
