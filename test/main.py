import firebase_admin
from firebase_admin import credentials, db
from utils import initialize

initialize()

ref = db.reference("/chat")
data = {"something":"something"}
ref.set(data)


