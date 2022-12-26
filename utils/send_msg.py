import firebase_admin
from firebase_admin import credentials, db

#Msg send function
def send_msg(ref, data, room):
    ref.child(room).set(data)
