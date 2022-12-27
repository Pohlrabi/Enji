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
    cred = get_info("path")
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

def get_info(type):
    try:
        with open("{}.json".format(type), "r") as f:
            data = json.load(f)
            return data[type]
    except:
        return None
def write_info(type, info):
    try:
        with open("{}.json".format(type), "w") as f:
            data = {"{}".format(type) : info}
            json.dump(data,f)
    except:
        raise Exception

