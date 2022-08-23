from modules.players import Player
from modules.tournament import Tournament


class Manager:
    '''def __init__(self) -> None:
        pass'''

    def serialize_player_list(players: list):
        serialized_list = []
        for player in players:
            serialized_list.append(player.serialize())
        return serialized_list

    def unserialize_player_dict(player_dict_list: list):
        unserialized_list = []
        for player_dict in player_dict_list:
            f, l, g, b, r = player_dict.values()
            unserialized_list.append(Player(f, l, b, g, r,))
        return unserialized_list

    def serialize_tournament(tournament: Tournament):
        return_dict = {"name": tournament.name, "location": tournament.location, "start_date": tournament.start_date, "end_date": tournament.end_date, "turn": tournament.turn,
                       "time_control": tournament.time_control, "description": tournament.description, "round_amount": tournament.round_amount, "players": tournament.players}

        return return_dict
