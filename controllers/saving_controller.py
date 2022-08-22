from tinydb import TinyDB as tdb

class Save:

    def export_(data:dict, filename:str):
        db=tdb("db.json")
        table=db.table(filename)
        table.truncate()
        table.insert_multiple(data)

    def import_(filename):
        db=tdb("db.json")
        table=db.table(filename)
        return table.all()
