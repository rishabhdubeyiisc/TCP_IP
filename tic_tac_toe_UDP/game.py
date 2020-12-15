#!/usr/bin/env python3
import socket 
import os
import random 
import sys
import server_class
import debugger_class

verbose_control_GLOBAL = True
use_debugger_GLOBAl = True
class game:
    matrix = [  [ '-' , '-' , '-' ] ,
                [ '-' , '-' , '-' ] ,
                [ '-' , '-' , '-' ]  
             ]
    moves_played = 0
    game_status = "unset"
    #TODO create a IP set here take set from server class
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
    #debugger
    debugger = debugger_class.debugger_class(use_debugger=True , verbose_control = True , create_dir= False , filename="game.log")
    #commStages
    comm_stage_1_str = "" 
    comm_stage_2_str = ""       
    def __init__ (self , name0 = "Rishabh" , name1 = "Dubey"):
        self.debugger = debugger_class.debugger_class(use_debugger=use_debugger_GLOBAl , 
                                                        verbose_control = verbose_control_GLOBAL , 
                                                        create_dir= False , 
                                                        filename="game.log")        
        self.player_char_set[self.player0][self.name_field] = name0
        self.player_char_set[self.player1][self.name_field] = name1
        self.current_player_id = random.choice([0, 1])
        self.player_info_str = ("\nPlayer choosen for start is : " + str(self.player_char_set[self.current_player_id][self.name_field]) + " your symbol is : " + str(self.player_char_set[self.current_player_id][self.symbol_field]) + "\n")
        self.show_matrix()
        self.game_status = "initialized"
        self.debugger.log("game.init","self.player_info_str " + self.player_info_str)
    
    def show_matrix(self):
        self.display_str =  ("\n      __ GAME __")
        self.display_str += ("\n      " + self.player_char_set[self.player0][self.name_field] + " : " +  self.player_char_set[self.player0][self.symbol_field] )
        self.display_str += ("\n      " + self.player_char_set[self.player1][self.name_field] + " : " +  self.player_char_set[self.player1][self.symbol_field] )
        self.display_str += ("\n      0    1    2")
        self.display_str += ("\n  0 " + str(self.matrix[0]))
        self.display_str += ("\n  1 " + str(self.matrix[1]))
        self.display_str += ("\n  2 " + str(self.matrix[2]))
        self.display_str += ("\n")
        self.debugger.log("game.show_matrix" , self.display_str)
        
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
        self.comm_stage_base (self.player_ERROR_str)
        self.debugger.log("game.set_matrix", " ERR : " + self.player_ERROR_str )
        return False

    def is_valid_move (self,x,y):
        if (self.matrix[x][y] == '-'):
            return True
        self.player_ERROR_str = (" \nINVALID MOVE ")
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
        status , x , y = self.comm_stage_base() # done 0 1 2 check
        return status , x , y
    
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
    
    def comm_11(self):
        self.player_info_str = (self.player_char_set[self.current_player_id][self.name_field] + " enter coordinates")
        self.out_str_player = self.display_str + self.player_info_str
        #send
        self.debugger.log("game.comm_11", " SENDING : " + self.out_str_player )
        network_module.send_ack ( self.out_str_player)
        self.debugger.log("game.comm_11", " SENT : " + self.player_info_str )
        #recv
        self.debugger.log("game.comm_11", " ON RECV " )
        self.comm_stage_1_str = network_module.recv_data()
        self.debugger.log("game.comm_11", " RECVEING : " + self.comm_stage_1_str )

    def comm_stage_base(self , err_string = ""):
        self.player_info_str = (self.player_char_set[self.current_player_id][self.name_field] + " enter coordinates")
        self.out_str_player = self.display_str + self.player_info_str + err_string
        #send
        self.debugger.log("game.comm_stage_base", " SENDING : " + self.out_str_player )
        network_module.send_ack ( self.out_str_player)
        self.debugger.log("game.comm_stage_base", " SENT : " + self.player_info_str )
        #recv
        self.debugger.log("game.comm_stage_base", " ON RECV " )
        self.comm_stage_1_str = network_module.recv_data()
        self.debugger.log("game.comm_stage_base", " RECVEING : " + self.comm_stage_1_str )
        is_input_valid , x , y = self.check_input(self.comm_stage_1_str) # checks for 0 , 1 , 2
        if (not is_input_valid):
            x , y = self.comm_stage_012_err()
        return True , x , y

    def comm_stage_012_err(self , err_string = "ERR : INPUT 'length < 2' OR invalid charcters must belong to (0,1,2)"):
        #chechk what error occured
        self.player_info_str = (self.player_char_set[self.current_player_id][self.name_field] + " enter coordinates")
        self.out_str_player = self.display_str + err_string + "\n" + self.player_info_str
        is_input_valid = False
        x = 3 
        y = 3
        while (not is_input_valid):
            #send
            self.debugger.log("game.comm_stage_012_err", " SENDING : " + self.out_str_player )
            network_module.send_ack ( self.out_str_player)
            self.debugger.log("game.comm_stage_012_err", " SENT : " + self.player_info_str )
            #recv
            self.debugger.log("game.comm_stage_012_err", " ON RECV " )
            self.comm_stage_2_str = network_module.recv_data()
            self.debugger.log("game.comm_stage_012_err", " RECVEING : " + self.comm_stage_2_str )
            is_input_valid , x , y = self.check_input(self.comm_stage_2_str) # checks for 0 , 1 , 2
        return x , y

    def game_process(self):
        self.debugger.log("game.game_process","START")
        is_valid_cordinates , x , y = self.co_ordinates_check()
        if (is_valid_cordinates):
            self.set_matrix(x,y,self.current_player_id)

if __name__ == "__main__":
    debugger = debugger_class.debugger_class( use_debugger=use_debugger_GLOBAl, 
                                              verbose_control = verbose_control_GLOBAL ,
                                              filename = "main.log")
    debugger.log(debugger.function_name(),"Initialized debugger")
    
    network_module = server_class.game_server(use_debugger=True,
                                              verbose_control=True )
    debugger.log("main","Initialized network_module")
    
    game_module = game( name0 = "Rishabh", 
                        name1 = "Surabhi")
    debugger.log("main","Initialized game_module")
    
    engine_state = "INIT"
    
    while( not (game_module.got_result())):
        if (engine_state == "INIT"):
            debugger.log("While_INIT","START")
            # recv data
            incoming_string = network_module.recv_data() # first break here
            debugger.log("While_INIT", "incoming_string : " + incoming_string)
            # send data
            game_module.out_str_player = game_module.player_info_str + game_module.player_ERROR_str + game_module.display_str
            debugger.log("While_INIT", "SENDING " + game_module.out_str_player )
            debugger.log("While_INIT", "SENDING game_module.out_str_player" )
            network_module.send_ack (game_module.out_str_player)
            debugger.log("While_INIT", "SENT ")
            #recv 2
            incoming_string = network_module.recv_data() # first break here
            debugger.log("While_INIT", "incoming_string : " + incoming_string)
            # change state
            engine_state = "GAME_PROCESS"
            debugger.log("While_INIT","END")

        if (engine_state == "GAME_PROCESS"):
            debugger.log("While_GAME_PROCESS","start")
            #Game process
            game_module.game_process()
            if (game_module.got_result()):
                winner = game_module.get_winner_name()
                #send winner name
                network_module.send_ack( game_module.display_str + "\n The_winner_is : " + winner )
                #recieve
                incoming_str = network_module.recv_data()
            debugger.log("While_GAME_PROCESS","start")
    print("Game done")


