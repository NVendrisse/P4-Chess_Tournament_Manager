from modules.players import Player
from modules.tournament import Tournament

class Manager:
    def __init__(self) -> None:
        pass

    def create_new_player(self,firstname,lastname,birthdate,genre,rank):
        new_player=Player(firstname,lastname,birthdate,genre,rank)
        return new_player

    def view_all_players(self):
        pass

    def create_new_tournament(self):
        new_tournament=Tournament()
        pass

    def view_tournament(self):
        pass

    def play_tournament(self,tournament:Tournament):
        pass
