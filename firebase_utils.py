import firebase_admin
from firebase_admin import credentials, db

if not firebase_admin._apps:
    cred = credentials.Certificate("wordcornreddit.json")
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://wordcornredditbot-default-rtdb.firebaseio.com/'
    })

def load_posted_from_firebase():
    ref = db.reference("posted_memes")
    data = ref.get()
    return set(data or [])

def save_posted_to_firebase(posted_set):
    ref = db.reference("posted_memes")
    ref.set(list(posted_set))