#!/usr/bin/env python3

import random 
class game:
    matrix = [  [ '-' , '-' , '-' ] ,
                [ '-' , '-' , '-' ] ,
                [ '-' , '-' , '-' ]  
             ]
    moves_played = 0
    game_status = "unset"
    player_char_set = [ ["str", 'X' , 0 ] , ["str", 'O' , 1] ]
    current_player_id = 0
    symbol_won = '-'        
    def __init__ (self , name0 , name1 ):
        self.player_char_set[0][0] = name0
        self.player_char_set[1][0] = name1
        self.current_player_id = random.choice([0, 1])
        print ("Player choosen for start is : " + str(self.player_char_set[self.current_player_id][0]) + " your symbol is : " + str(self.player_char_set[self.current_player_id][1]) )
        self.show_matrix()
        self.game_status = "initialized"
        self.game_run()
    
    def show_matrix(self):
        print("      __ GAME __")
        print ("      0    1    2")
        print ("  0 " + str(self.matrix[0]))
        print ("  1 " + str(self.matrix[1]))
        print ("  2 " + str(self.matrix[2]))

    def next_id(self):
        return (not (self.current_player_id))

    def set_matrix(self , x , y , player):
        if (self.is_valid_move(x,y)):
            self.matrix[x][y] = self.player_char_set[player][1]
            self.moves_played += 1
            self.show_matrix()
            self.current_player_id = (int)(self.next_id())
            return True
        print ("CANT SET MATRIX")
        return False

    def is_valid_move (self,x,y):
        if (self.matrix[x][y] == '-'):
            return True
        print ("INVALID MOVE")
        return False

    def got_result (self):
        if (self.moves_played < 5):
            self.game_status = "ongoing"
            return False
        # check diagonals
        if (self.matrix[0][0] == self.matrix[1][1] == self.matrix[2][2] != '-'):
            self.game_status = "won"
            self.symbol_won = self.matrix[0][0]
            return True
        if (self.matrix[0][2] == self.matrix[1][1] == self.matrix[2][0] != '-'):
            self.game_status = "won"
            self.symbol_won = self.matrix[0][2]
            return True
        # check horizontal
        for row in (0,1,2) :
            if (self.matrix[row][0] == self.matrix[row][1] == self.matrix[row][2] != '-'):
                self.game_status = "won"
                self.symbol_won = self.matrix[row][0]
                return True
        # check vertical
        for col in (0,1,2):
            if (self.matrix[0][col] == self.matrix[1][col] == self.matrix[2][col] != '-'):
                self.game_status = "won"
                self.symbol_won = self.matrix[0][col]
                return True
        # none true
        if (self.moves_played == 9):
            self.game_status = "draw"
            return True
        return False

    def co_ordinates (self):
        print(self.player_char_set[self.current_player_id][0] + " enter coordinates")
        string = input('>')
        string = string.replace(" " , "")
        x = int(string[0])
        y = int(string[1])
        if ( (x == 0 or x == 1 or x == 2) and (y == 0 or y == 1 or y == 2) ):
            return True , x , y
        print("INPUT OUT OF BOUNDS must belong to (0,1,2)")
        return False , x , y
    
    def get_winner_name(self):
        if (self.symbol_won == self.player_char_set[0][1]):
            return self.player_char_set[0][0]
        return self.player_char_set[1][0]
    
    def game_run(self):
        while (not (self.got_result())):
            is_valid_cordinates , x , y = self.co_ordinates()
            if (is_valid_cordinates):
                self.set_matrix(x,y,self.current_player_id)
                if(self.got_result()):
                    print(self.game_status)
                    if (self.game_status == 'won'):
                        print (self.get_winner_name())
            

gamer = game("rishabh", "dubey")

