from peewee import CharField
from app import db 


class Todo(db.Model):
    task = CharField()

# class Todo(db.Entity):
#     id = PrimaryKey(int, auto=True)
#     title = Required(str)
#     done = Optional(bool)
#     date_created = Optional(datetime)
#     date_scheduled = Optional(datetime)
    # notes = Set('Note')
    # tags = Set('Tag')
    # todos = Set('Todo', reverse='todos')


# class Note(db.Entity):
#     id = PrimaryKey(int, auto=True)
#     text = Required(str)
#     todos = Set(Todo)
#     tags = Set('Tag')


# class Tag(db.Entity):
#     id = PrimaryKey(int, auto=True)
#     name = Required(str)
#     todos = Set(Todo)
#     notes = Set(Note)

