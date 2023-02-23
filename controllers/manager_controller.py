from modules.players import Player
from modules.tournament import Tournament
import os


class Manager:
    # Classe controleur : gestion des structure de données et du clear screen
    def serialize_player_list(players: list):
        # Fonction de sérialisation d'une liste d'objets Player
        # Retourne une liste de dictionnaires contenant les infos des joueurs
        serialized_list = []
        for player in players:
            serialized_list.append(player.serialize())
        return serialized_list

    def unserialize_player_dict(player_dict_list: list):
        # Fonction de désérialisation des joueurs
        # Retourne une liste d'objets Player
        unserialized_list = []
        for player_dict in player_dict_list:
            f, l, b, g, r, s = player_dict.values()
            unserialized_player = Player(f, l, b, g, r)
            unserialized_player.score = s
            unserialized_list.append(unserialized_player)
        return unserialized_list

    def serialize_tournament(tournament: Tournament):
        # Fonction de sérialisation des tournois
        # retourne une liste contenant le dictionnaire du tournois
        serialized_tournament = []
        return_dict = {"name": tournament.name,
                       "location": tournament.location,
                       "start_date": tournament.start_date,
                       "end_date": tournament.end_date,
                       "turn": tournament.turn,
                       "time_control": tournament.time_control,
                       "description": tournament.description,
                       "round_amount": tournament.round_amount,
                       "players": tournament.players,
                       "results": tournament.results,
                       "start": tournament.start,
                       "stop": tournament.stop}
        serialized_tournament.append(return_dict)
        return serialized_tournament

    def unserialize_tournament(serialised_tournament: list):
        # Fonction de désérialisation de tournois
        # Retourne un objet Tournament
        n, l, sd, ed, t, tc, d, ra, p, r, sta, stp = serialised_tournament[0].values()
        unserialized_tournament = Tournament(n, l, sd, ed, tc, d, t, ra, p, r, sta, stp)
        return unserialized_tournament

    def clear_screen():
        # Fonction de nettoyage de l'écran
        if os.name == "posix":
            os.system("clear")
        else:
            os.system("cls")
