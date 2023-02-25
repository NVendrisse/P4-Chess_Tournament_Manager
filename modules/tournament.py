import time
from views.play_view import MainPlay


class Tournament:
    # Classe représentant un objet tournois
    def __init__(self, name: str, location: str, start_date: str, end_date: str, time_control: str,
                 description: str, turn=[], round_amount=4, players=[], results=[], start="", stop="", _ct=1):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.turn = turn
        self.time_control = time_control
        self.description = description
        self.round_amount = round_amount
        self.players = players
        self.results = results
        self.current_turn = _ct
        self.start = start
        self.stop = stop

    def store_results(self, updated_results: list = []):
        self.results = updated_results

    def tournament_start(self):
        self.start = time.asctime()

    def tournament_stop(self):
        self.stop = time.asctime()


class Match:
    # Classe représentant un objet match
    def __init__(self, players: tuple) -> None:
        self.player_one = players[0]
        self.player_two = players[1]

    def define_score(self):
        # Fonction de définition du score d'un match
        print(MainPlay.scoring_display().format(
            self.player_one.lastname, self.player_two.lastname))

        winner = input("Résultats : ")
        if winner == "1":
            self.player_one.score += 1
        elif winner == "2":
            self.player_two.score += 1
        elif winner == "3":
            self.player_one.score += 0.5
            self.player_two.score += 0.5
        else:
            exit()
        return self.player_one.score, self.player_two.score

    def export_score(self):
        # Fonction d'export du score d'un match
        score = (["{} {}".format(self.player_one.serialize()["firstname"], self.player_one.serialize()["lastname"]),
                 "{} {}".format(self.player_two.serialize()["firstname"], self.player_two.serialize()["lastname"])],
                 [self.player_one.score, self.player_two.score])
        return score


class Turn:
    # Classe représentant un objet tour
    def __init__(self, tournament: Tournament, match: list, current_turn: int) -> None:
        self.t = tournament
        self.m = match
        self.ct = current_turn
        self.name = "Round {}".format(self.ct)

    def turn_start(self):
        self.start = time.asctime()

    def turn_stop(self):
        self.t.current_turn += 1
        self.stop = time.asctime()

    def serialized(self):
        return (self.name, self.m, self.ct)
