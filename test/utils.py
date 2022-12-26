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
    with open("creds.json", "r") as f :
        cred = json.load(f)
        cred = cred["path"]
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
    time = get_current_time()
    ref.child(room).child(time).set(data)

def set_data(user, msg, room="2"):
    data = {
        "user": user,
        "message": msg,
    }
    return data, room

def get_user():
    try:
        with open("user.json", "r") as f:
            data = json.load(f)
            return data["user"]
    except:
        pass
