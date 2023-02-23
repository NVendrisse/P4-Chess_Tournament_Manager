from tinydb import TinyDB as tdb
from modules.tournament import Match, Tournament, Turn
from controllers.manager_controller import Manager
from os import listdir


class Save:
    # Classe de gestion de la sauvegarde dans les fichiers json

    def export_(data: list, table_name: str, db_name="db"):
        # Fonction d'export des données
        db = tdb("{}.json".format(db_name))
        table = db.table(table_name)
        table.truncate()
        table.insert_multiple(data)

    def import_(table_name: str, db_name="db"):
        # Fonction d'importation des données
        db = tdb("{}.json".format(db_name))
        table = db.table(table_name)
        return table.all()

    def select_tournament():
        # Fonction de sélection d'un tournois dans la liste de sauvegarde
        # Retourne tous les tournois non terminés
        tournament_list = listdir("./save/tournament")
        tournament_available = []
        for i in tournament_list:
            t_ = Save.import_("tournament", "./save/tournament/{}".format(i[:len(i) - 5]))
            t_u = Manager.unserialize_tournament(t_)
            if t_u.stop == "":
                tournament_available.append(i)
        return tournament_available
    
    def select_tournament_visu():
        # Fonction de sélection d'un tournois dans la liste de sauvegarde
        # Retourne tous les tournois pour visualisation
        tournament_list = listdir("./save/tournament")
        return tournament_list

class TurnSave:
    # Classe de sauvegarde d'un tour dans un tournois
    def save(tournament: Tournament, _turn: Turn):
        tournament.turn.append(_turn.serialized())


class MatchSave:
    # Classe de sauvegarde d'un match dans un tour
    def save(turn: Turn, _match: Match):
        turn.m.append(_match)
