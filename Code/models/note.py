from database.db import Database

class Note:
    def __init__(self, note_id, title, content):
        self.note_id = note_id
        self.title = title
        self.content = content

    def json(self):
        return {
            "note_id" : self.note_id,
            "title" : self.title,
            "content" : self.content
        }

    def save_to_mongo(self):
        Database.insert(
            collection = "notes",
            data = self.json()
        )

    def from_mongo(cls, note_id):
        return Database.find_one(collection = 'notes', query = { 'note_id' : note_id })
