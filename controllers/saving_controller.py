from tinydb import TinyDB as tdb
from modules.tournament import Match, Tournament, Turn
from os import listdir


class Save:

    def export_(data: list, table_name: str, db_name="db"):
        db = tdb("{}.json".format(db_name))
        table = db.table(table_name)
        table.truncate()
        table.insert_multiple(data)

    def import_(table_name: str, db_name="db"):
        db = tdb("{}.json".format(db_name))
        table = db.table(table_name)
        return table.all()

    def update_(data: dict, table_name: str, db_name="db"):
        db = tdb("{}.json".format(db_name))
        table = db.table(table_name)
        table.update({"1": data})

    def select_tournament():
        tournament_list = listdir("./save/tournament")
        return tournament_list
        


class TurnSave:

    def save(tournament: Tournament, _turn: Turn):
        tournament.turn.append(_turn)


class MatchSave:

    def save(turn: Turn, _match: Match):
        turn.m.append(_match)
