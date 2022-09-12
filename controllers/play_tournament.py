from modules.tournament import *
from controllers.manager_controller import Manager
from views.play_view import *

class Play:

    def __init__(self,tournament:Tournament) -> None:
        Manager.clear_screen()
        self.tournament=tournament
        self.pairs=[]
        main_title=MainPlay.title().format(self.tournament.name)
        self.start_tournament()

    def first_player_pairing(self):
        players=self.tournament.players
        ordered_players=sorted(players, key=lambda player: player.rank,reverse=False)
        for _index in range(len(ordered_players[:4])):
            self.pairs.append((ordered_players[_index],ordered_players[_index+4]))
        
    def start_tournament(self):
        self.tournament.tournament_start()
        if self.tournament.current_turn==1:
            self.first_player_pairing()
        else:
            self.sort_player()
        #INIT turn
            #init match
        
        

    def sort_player(self):
        pass

        

