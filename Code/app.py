from json import dumps
from bson import json_util, ObjectId
from database.db import Database
from models.note import Note
from flask import Flask, request

app = Flask(__name__)

Database.Initialize()

note = Note(1, "My First Note", "Hello MongoDB")
note.save_to_mongo()

@app.route('/')
def MyNote():
    return "Welcome to SimpleNote"

@app.route('/notes/', methods = ['POST'])
def add_note():
    new_note = request.get_json()
    new_note_to_create = Note(new_note['note_id'], new_note['title'], new_note['content'])
    # note = Note(data['note_id'], data['title'], data['content'])
    new_note_to_create.save_to_mongo()
    return { "message" : "success"}

@app.route('/notes/<int:note_id>')
def get_notes(note_id):
    result = note.from_mongo(note_id)
    return json_util.dumps(result)


if __name__ == "__main__":
    app.run(debug=True)