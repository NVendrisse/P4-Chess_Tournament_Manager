from tinydb import TinyDB as tdb
from modules.tournament import Match, Tournament, Turn


class Save:

    def export_(data: dict, table_name: str, db_name="db"):
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


class TurnSave:

    def save(tournament: Tournament, _turn: Turn):
        tournament.turn.append(_turn)


class MatchSave:

    def save(turn: Turn, _match: Match):
        turn.m.append(_match)
