import firebase_admin
from firebase_admin import credentials, db
import json

#Initialize creds and database link
def initialize():
    with open("creds_path.json", "r") as f :
        cred = json.load(f)
        cred = cred["creds_path"]
    cred = credentials.Certificate(cred)
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://enji-9fe2b-default-rtdb.firebaseio.com/'
    })
    ref = db.reference("/chat")