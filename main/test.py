import firebase_admin
from firebase_admin import credentials, db
import utils

# Set up the Firebase Admin SDK with your service account
ref = utils.initialize()

# Get a reference to the database root
def listener(event):
    return  # new data at /reference/event.path. None if deleted

db.reference('/').listen(listener)
