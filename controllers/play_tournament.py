from modules.tournament import *
from controllers.manager_controller import Manager
from views.play_view import *

class Play:

    def __init__(self,tournament:Tournament) -> None:
        Manager.clear_screen()
        self.tournament=tournament
        main_title=MainPlay.title().format(self.tournament.name)

    def first_player_pairing(self):
        players=self.tournament.players
        
    def start_tournament(self):
        pass

    def sort_player(self):
        pass

        

