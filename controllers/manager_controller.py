from modules.players import Player
from modules.tournament import Tournament


class Manager:
    def __init__(self) -> None:
        pass

    def serialize_player_list(self, players):
        serialized_list = []
        for player in players:
            serialized_list.append(player.serialized())
        return serialized_list

    def view_all_players(self):
        pass

    def create_new_tournament(self):
        new_tournament = Tournament()
        pass

    def view_tournament(self):
        pass

    def play_tournament(self, tournament: Tournament):
        pass
