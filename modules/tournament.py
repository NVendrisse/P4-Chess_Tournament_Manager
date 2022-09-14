from modules.players import Player
import time


class Tournament:
    def __init__(self, name: str, location: str, start_date: str, end_date: str, time_control: str, description: str, turn=[], round_amount=4, players=[], results=[]):
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
        self.current_turn = 1

    def store_results(self, updated_results: list = []):
        self.results = updated_results

    def tournament_start(self):
        self.start = time.asctime()

    def tournament_stop(self):
        self.stop = time.asctime()


class Match:

    def __init__(self, players:tuple) -> None:
        self.player_one = players[0]
        self.player_two = players[1]
        self.score_player_one = 0
        self.score_player_two = 0

    def define_score(self):
        self.score_player_one = input(
            "Score {} : ".format(self.player_one.lastname))
        self.score_player_two = input(
            "Score {} : ".format(self.player_two.lastname))
        self.player_one.score+=self.score_player_one
        self.player_two.score+=self.score_player_two
        return (self.score_player_one, self.score_player_two)

    def export_score(self):
        score = ([self.player_one, self.player_two], [
                 self.score_player_one, self.score_player_two])
        return score


class Turn:

    def __init__(self, tournament: Tournament, match: list, current_turn: int) -> None:
        self.t = tournament
        self.m = match
        self.ct = current_turn
        self.name = "Round {}".format(self.ct)

    def turn_start(self):
        self.start = time.asctime()

    def turn_stop(self):
        self.t.current_turn+=1
        self.stop = time.asctime()
