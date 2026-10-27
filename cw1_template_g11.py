import csv
from copy import deepcopy

groupNumber = 0
groupName = {'Person 1 name' : 'Person 1 Username',\
             'Person 2 name' : 'Person 2 Username',\
             'Person 3 name' : 'Person 3 Username',\
             'Person 4 name' : 'Person 4 Username',\
             'Person 5 name' : 'Person 5 Username'}


###############################################################################
# Task 1

###############################################################################


###############################################################################
# Task 2

###############################################################################


###############################################################################
# Task 3

###############################################################################


###############################################################################
# Task 4

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

###############################################################################


###############################################################################
# Task 11

###############################################################################


###############################################################################
# Task 11

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
