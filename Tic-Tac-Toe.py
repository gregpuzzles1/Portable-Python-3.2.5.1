class Board:

    def __init__(self):
        """__init_ method"""
        self.x = "-"
        self.y = "|"
        self.z = " "
        self.board = [1, 2, 3, 4, 5, 6, 7, 8, 9]    # the list for the board items (0-8)

    def Draw(self):
        """Draws the board without square numbers then draws the board with square numbers"""
        print ('The Board looks like this: \n')     # draw the board without any square numbers
        print (self.z, self.y, self.z, self.y, self.z)
        print (self.x * 9)
        print (self.z, self.y, self.z, self.y, self.z)
        print (self.x * 9)
        print (self.z, self.y, self.z, self.y, self.z)
        print ('\n')
        print ('The Board with the square numbers looks like this: \n')     # draw the borad with the square numbers
        print (self.board[0], self.y, self.board[1], self.y, self.board[2])
        print (self.x * 9)
        print (self.board[3], self.y, self.board[4], self.y, self.board[5])
        print (self.x * 9)
        print (self.board[6], self.y, self.board[7], self.y, self.board[8])
        print ('\n')

class Mark(Board):
    
    def draw(self, square_number, mark):
        """Draws the borad with current values"""
        self.square_number = square_number - 1      # subtract 1 from the square number - list board starts at position 0 - (0-8)
        self.mark = mark                            # mark is either "X" or "O"
        self.board[self.square_number] = self.mark  # set the position in list board to either "X" or "O"
        for i in range(9):      # loop thru the values in list board
            try:
                self.board[i] += 1  # checks if the value in list board is an integer,
                self.board[i] = " " # if it is, set it equal to a space (" ")
            except TypeError:       # if the value is an "X" or an "O", just pass
                pass
        print ('\n')
        print (self.board[0], self.y, self.board[1], self.y, self.board[2]) # print the first row of the board, with current values
        print (self.x * 9)
        print (self.board[3], self.y, self.board[4], self.y, self.board[5]) # print the second row of the board, with current values
        print (self.x * 9)
        print (self.board[6], self.y, self.board[7], self.y, self.board[8]) # print the third row of the board, with the current values
        print ('\n')

    def select_square(self):
        """Starts the game with square selection"""
        self.switch = True      # initializes the switch for the while loop to True
        self.turn = ["X", "O"]  # turn is either an "X" or an "O"
        self.counter = 0        # set counter for a possible Tie game - (no winner)
        while self.switch == True:  # starts the while loop
            for move in range(2):   # alternate between "X" and "O"
                self.move = move
                self.get_input(self.turn, self.move)    # calls the get_input function
                if self.switch == False:        # checks to see if the while loop switch has been set to False
                    break                       # if it has, break out of the while loop - end game
                else:
                    self.counter += 1       # increment the counter by 1    
                if self.counter == 9:       # if 9 moves have been made with no winner
                    print ("The game is a Tie - no winner.\n")   # prints message - the game is a tie
                    self.switch = False     # set while loop switch to False
                    break                   # break out of the while loop
                else:
                    continue                # if counter in not equal to 9, continue alternating between "X" and "O"

    def get_input(self, turn, move):
        """Gets input from user"""
        self.turn = turn
        self.move = move
        try:
            sn = int(input(self.turn[self.move] + " Enter a square number (1-9) for your move: "))  # get input from user
            if self.check_input(sn) == True:                    # check the input for errors
                self.draw(sn, self.turn[move])                  # if no errors, draw the grid
                if self.check_win(self.turn, move) == True:     # Check if move is a win
                    self.print_win(self.turn, move)             # if win, print win message
                else:
                    pass
            else:
                pass
        except ValueError:
            print ("\nError: Please enter a number between 1-9\n")  # print message if a letter is entered
            self.get_input(self.turn, self.move)                    # try to get input again

    def check_input(self, square_number):
        """Checks the input for errors"""
        self.square_number = square_number
        if((self.square_number >= 1) and (self.square_number <= 9)):    # make sure number is between 1-9
            if ((self.board[self.square_number - 1]) == "X") \
                or ((self.board[self.square_number - 1]) == "O"):       # make sure the square is not already taken
                print ("\nError: That space is already taken, please choose an open space.\n")  # print message if space taken
                self.get_input(self.turn, self.move)                # try to get input again
            else:       
                return True     # if the number is between 1-9 and the space is not taken - return True
        else:
            print ("\nError: That is not a valid square number, please enter a value between 1-9\n")    # print message if number is out or range
            self.get_input(self.turn, self.move)                    # try to get input again

    def check_win(self, turn, move):
        """Checks the eight possibilites for a win"""
        if (self.board[0] == self.turn[move] and self.board[1] == self.turn[move] and self.board[2] == self.turn[move]):
            return True
        elif (self.board[3] == self.turn[move] and self.board[4] == self.turn[move] and self.board[5] == self.turn[move]):
            return True
        elif (self.board[6] == self.turn[move] and self.board[7] == self.turn[move] and self.board[8] == self.turn[move]):
            return True
        elif (self.board[0] == self.turn[move] and self.board[3] == self.turn[move] and self.board[6] == self.turn[move]):
            return True
        elif (self.board[1] == self.turn[move] and self.board[4] == self.turn[move] and self.board[7] == self.turn[move]):
            return True
        elif (self.board[2] == self.turn[move] and self.board[5] == self.turn[move] and self.board[8] == self.turn[move]):
            return True
        elif (self.board[0] == self.turn[move] and self.board[4] == self.turn[move] and self.board[8] == self.turn[move]):
            return True
        elif (self.board[2] == self.turn[move] and self.board[4] == self.turn[move] and self.board[6] == self.turn[move]):
            return True
        else:
            return False

    def print_win(self, turn, move):
        """Prints the winning message"""
        print (str(turn[move]) + " Wins ! \n")  # prints the winning message
        self.switch = False                     # sets the looping switch in select_square function to False
        return self.switch                      # returns the value of the switch (False)
    
d1 = Mark()     # Create object d1 of the Mark class - (mark class inherits from the Board class)
d1.Draw()       # call the Draw function in the Board class
d1.select_square()  # start the game by calling the select_square function in the Mark class
