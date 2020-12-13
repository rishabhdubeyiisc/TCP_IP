#!/usr/bin/env python3
import socket 
import os
import random 
import sys
import server_class
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
    #output strings
    display_str = ""
    player_info_str = ""
    player_ERROR_str = ""
    out_str_player=""
    out_str_spectator=""
    #private variables
    player0 = 0        
    player1 = 1
    name_field = 0        
    symbol_field = 1        
    id_field = 2        
    def __init__ (self , name0 , name1 ):
        self.player_char_set[self.player0][self.name_field] = name0
        self.player_char_set[self.player1][self.name_field] = name1
        self.current_player_id = random.choice([0, 1])
        self.player_info_str = ("\nPlayer choosen for start is : " + str(self.player_char_set[self.current_player_id][self.name_field]) + " your symbol is : " + str(self.player_char_set[self.current_player_id][self.symbol_field]) + "\n")
        #priint(self.player_info_str)
        self.show_matrix()
        self.game_status = "initialized"
        #self.game_run()
    
    def show_matrix(self):
        self.display_str =  ("\n      __ GAME __")
        self.display_str += ("\n      " + self.player_char_set[self.player0][self.name_field] + " : " +  self.player_char_set[self.player0][self.symbol_field] )
        self.display_str += ("\n      " + self.player_char_set[self.player1][self.name_field] + " : " +  self.player_char_set[self.player1][self.symbol_field] )
        self.display_str += ("\n      0    1    2")
        self.display_str += ("\n  0 " + str(self.matrix[0]))
        self.display_str += ("\n  1 " + str(self.matrix[1]))
        self.display_str += ("\n  2 " + str(self.matrix[2]))
        self.display_str += ("\n")
        #priint(self.display_str)
        
    def next_id(self):
        return (not (self.current_player_id))

    def set_matrix(self , x , y , player):
        if (self.is_valid_move(x,y)):
            self.matrix[x][y] = self.player_char_set[player][self.symbol_field]
            self.moves_played += 1
            self.show_matrix()
            self.current_player_id = (int)(self.next_id())
            return True
        self.player_ERROR_str += ("CANT SET MATRIX")
        #priint(self.player_ERROR_str)
        return False

    def is_valid_move (self,x,y):
        if (self.matrix[x][y] == '-'):
            return True
        self.player_ERROR_str = ("INVALID MOVE ")
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

    def co_ordinates_check (self):
        status , x , y = take_input(self)
        if not status :
            self.player_ERROR_str = ("ERR : INPUT 'length < 2' OR invalid charcters must belong to (0,1,2)")
            #priint(self.player_ERROR_str)
            return False , x , y
        if ( (x == 0 or x == 1 or x == 2) and (y == 0 or y == 1 or y == 2) ):
            return True , x , y
        self.player_ERROR_str = ("\nERR : INPUT 'OUT OF BOUNDS' must belong to (0,1,2)")
        #priint(self.player_ERROR_str)
        return False , x , y
    
    def get_winner_name(self):
        if (self.symbol_won == self.player_char_set[self.player0][self.symbol_field]):
            return self.player_char_set[self.player0][self.name_field]
        return self.player_char_set[self.player1][self.name_field]
    
    def check_input (self , string ):
        string = string.replace(" " , "")
        if (len(string) < 2):
            return False , 3 , 3
        if ( (string[0] != '0' and string[0] != '1' and string[0] != '2' ) or ( string[1] != '0' and string[1] != '1' and string[1] != '2' ) ):
            return False , 3 , 3
        return True , int(string[0]) , int(string[1]) 

#these two below functions has to be changed
#TODO
def take_input(game):
    game.player_info_str = (game.player_char_set[game.current_player_id][game.name_field] + " enter coordinates")
    #TODO
    network_module.send_ack ( game.player_info_str)
    string = network_module.recv_data()
    if (string == "q!"):
        #TODO
        #write exit stratedy we can flase the condition of while and exit by that
        network_module.send_ack ( "Player : " + game.player_char_set[game.current_player_id][game.name_field] + " is quiting" )
        exit(0)

    is_input_valid , x , y = game.check_input(string)
    if (not is_input_valid):
        return False , 3 , 3
    return True , x , y

def game_process(game):
    is_valid_cordinates , x , y = game.co_ordinates_check()
    if (is_valid_cordinates):
        game.set_matrix(x,y,game.current_player_id)
    game.out_str_player = game.player_ERROR_str + game.display_str
    #TODO 
    network_module.send_ack( game.out_str_player)

def game_end(game):
    if (game.game_status == 'won'):
        game.display_str += ("   WINNER : "+ game.get_winner_name() + "\n")
    if (game.game_status == 'draw'):
        game.display_str += ("          DRAW   \n")
    game.out_str_player = game.display_str
    #TODO
    network_module.send_ack( game.out_str_player)      

if __name__ == "__main__":
    
    network_module = server_class.game_server()
    game_module = game("Rishabh", "Surabhi")
    game_module.out_str_player = game_module.player_info_str + game_module.player_ERROR_str + game_module.display_str
    print ("game :  " + game_module.out_str_player)
    #TODO
    incoming_string = network_module.recv_data()
    network_module.send_ack (game_module.out_str_player)
    incoming_string = network_module.recv_data()

    while( not (game_module.got_result())):
        game_process (game_module)       
        incoming_string = network_module.recv_data()
        print(incoming_string)
        network_module.send_ack(game_module.out_str_player)    

    #game_process( game_module )

