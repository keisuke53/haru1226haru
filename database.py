from peewee import *

db = SqliteDatabase('people.db')

class Person(Model):
    name = CharField()
    emotion = CharField()
    age = IntegerField()
    
    class Meta:
        database = db # This model uses the "people.db" database.

db.create_tables({Person})

Person.create(name="はるひと",emotion="眠い", age=12)
Person.create(name="たかひと",emotion="眠い",age=16)
Person.create(name="母さん",emotion="普通",age=25)
