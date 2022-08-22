from modules.players import Player
from modules.tournament import Tournament


class Manager:
    '''def __init__(self) -> None:
        pass'''

    def serialize_player_list(players:list):
        serialized_list = []
        for player in players:
            serialized_list.append(player.serialize())
        return serialized_list
    
    def unserialize_player_dict(player_dict_list:list):
        unserialized_list = []
        for player_dict in player_dict_list:
            pass

    def view_all_players(self):
        pass

    def create_new_tournament(self):
        new_tournament = Tournament()
        pass

    def view_tournament(self):
        pass

    def play_tournament(self, tournament:Tournament):
        pass
