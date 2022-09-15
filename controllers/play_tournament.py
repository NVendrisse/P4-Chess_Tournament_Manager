from controllers.menu_controller import *
from modules.tournament import *
from controllers.manager_controller import Manager
from views.play_view import *

class Play:

    def __init__(self,tournament:Tournament) -> None:
        #Manager.clear_screen()
        menu_display=MainPlay.play_menu()
        self.tournament=tournament
        self.players=self.tournament.players
        self.pairs=[]
        main_title=MainPlay.main_title().format(self.tournament.name)
    
    def select(self,selection:int):
        if selection=="1":
            self.start_tournament()
        else:
            return_back = MainMenu()
            main_menu_selector = return_back.select(
                input("Enter your choice : "))


    def first_player_pairing(self):
        self.pairs.clear()
        players_list=Manager.unserialize_player_dict(self.players)
        ordered_players=sorted(players_list, key=lambda player: player.rank,reverse=False)
        for _index in range(len(ordered_players[:len(ordered_players)//2])):
            self.pairs.append((ordered_players[_index],ordered_players[_index+len(ordered_players)//2]))
        
    def start_tournament(self):
        self.tournament.tournament_start()
        if self.tournament.current_turn==1:
            self.first_player_pairing()
        else:
            self.sort_player()
        _round=Turn(self.tournament,[],self.tournament.current_turn)
        while _round.ct <= int(self.tournament.round_amount):
            self.play_turn(_round)
            self.sort_player()
            self.tournament.current_turn=_round.ct
        self.tournament.tournament_stop()
        
        

    def sort_player(self):
        self.pairs.clear()
        players=self.tournament.players
        players_list=Manager.unserialize_player_dict(self.players)
        ordered_players=sorted(players_list, key=lambda player: player.score,reverse=False)
        for _index in range(len(ordered_players[:len(ordered_players)//2])):
            self.pairs.append((ordered_players[_index],ordered_players[_index+len(ordered_players)//2]))

    def play_turn(self, round:Turn):
        
        round_display=cprint(MainPlay.round_display().format(self.tournament.current_turn))
        for match_number in range(len(self.pairs)):
            this_match=Match(self.pairs[match_number])
            match_play=this_match.define_score()
            round.m.append(this_match.export_score())
        round.ct+=1



