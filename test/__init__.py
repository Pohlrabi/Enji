import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials, db

# Initialize the Firebase app with a service account, granting admin privileges
cred = credentials.Certificate('C:/Users/fiero/Downloads/enji-9fe2b-firebase-adminsdk-npe4q-94d5acf441.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://enji-9fe2b-default-rtdb.firebaseio.com/'
})

# As an admin, the app has access to read and write all data, regradless of Security Rules
ref = db.reference('/chat')

print(firestore.SERVER_TIMESTAMP)
# Add a new message to the database
ref.push({
    'sender': 'Alice',
    'timestamp': firestore.Timestamp.now(),
    'message': 'Hello, World!'
})
