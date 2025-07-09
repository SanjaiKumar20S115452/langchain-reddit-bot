import os
import json
import firebase_admin
from firebase_admin import credentials, db

if not firebase_admin._apps:
    # cred = credentials.Certificate("wordcornreddit.json")
    # firebase_admin.initialize_app(cred, {
    #     'databaseURL': 'https://wordcornredditbot-default-rtdb.firebaseio.com/'
    # })
    firebase_creds = os.getenv("FIREBASE_CREDENTIALS")
    if firebase_creds is None:
        raise Exception("FIREBASE_CREDENTIALS environment variable not set")

    cred_dict = json.loads(firebase_creds)
    cred = credentials.Certificate(cred_dict)

    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://wordcornredditbot-default-rtdb.firebaseio.com'
    })

def load_posted_from_firebase():
    try:
        ref = db.reference("posted_memes")
        data = ref.get()
        return set(data or [])
    except Exception as e:
        print("Error loading from Firebase:", str(e))
        return set()

def save_posted_to_firebase(posted_set):
    try:
        ref = db.reference("posted_memes")
        ref.set(list(posted_set))
    except Exception as e:
        print("Error saving to Firebase:", str(e))