

class Tournament:
    def __init__(self, name: str, location: str, start_date: str, end_date: str, time_control: str, description: str, turn = [], round_amount=4, players=[]):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.turn = turn
        self.time_control = time_control
        self.description = description
        self.round_amount = round_amount
        self.players = players
