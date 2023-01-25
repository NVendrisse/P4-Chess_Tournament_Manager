

class Player:
    def __init__(self, firstname: str, lastname: str, birthdate: str, genre: str, rank: int):
        self.firstname = firstname
        self.lastname = lastname
        self.birthdate = birthdate
        self.genre = genre
        self.rank = rank
        self.score = 0

    def serialize(self):
        return {"firstname": self.firstname, "lastname": self.lastname, "birthdate": self.birthdate,
                "genre": self.genre, "rank": self.rank, "score": self.score}
