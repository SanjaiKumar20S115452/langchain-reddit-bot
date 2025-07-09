import firebase_admin
from firebase_admin import credentials, db

# Step 1: Load credentials and initialize the app
cred = credentials.Certificate("wordcornreddit.json")  # Make sure this file is in the same folder
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://wordcornredditbot-default-rtdb.firebaseio.com/'
})

# Step 2: Write some test data
ref = db.reference("test_connection")
ref.set({
    "status": "connected",
    "message": "This is a test from local Python script!"
})

# Step 3: Read the same data back
snapshot = ref.get()
print("✅ Firebase test successful! Data read from Firebase:")
print(snapshot)
