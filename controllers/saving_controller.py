from tinydb import TinyDB as tdb

class Save:

    def export_(data:dict, table_name:str):
        db=tdb("db.json")
        table=db.table(table_name)
        table.truncate()
        table.insert_multiple(data)

    def import_(table_name):
        db=tdb("db.json")
        table=db.table(table_name)
        return table.all()

    def update_(table_name):
        pass