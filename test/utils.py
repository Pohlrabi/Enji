import firebase_admin
from firebase_admin import credentials, db
import json
import datetime


def get_current_time():
    now = datetime.datetime.now()
    time = now.strftime("%Y-%m-%d %H:%M:%S")
    return time

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
    return ref

def receive_msg(ref):
    data = ref.get()
    return data

def send_msg(ref, data, room):
    ref.child(room).set(data)

def set_data(user, msg, room):
    time = get_current_time()
    data = {
        "user": user,
        "time": time,
        "message": msg,
    }
    return data, room


