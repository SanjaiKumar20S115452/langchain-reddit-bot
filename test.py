import os
import praw
from dotenv import load_dotenv
import requests
load_dotenv()
username="That_Adhesiveness_54"
password="123456@Seven"
client_id="6yV3pVhhNohEn5lbzWSY4g"
client_secret="DYFJU3eFea39GBCJj7gmHEDvyh5PUA"
user_agent="script by u/That_Adhesiveness_54"
reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    username=username,
    password=password,
    user_agent=user_agent
)
print(reddit.user.me())
response = requests.get("https://res.cloudinary.com/dtbbxzcyq/image/upload/v1742430905/wordcorn/wordImages/memes/aberrant-branded_n0qetl.jpg")
print("Status:", response.status_code)
print("Content-Type:", response.headers.get("Content-Type"))


# print("Client ID:", os.getenv("REDDIT_CLIENT_ID"))
# print("Client Secret:", os.getenv("REDDIT_CLIENT_SECRET"))
# print("Username:", os.getenv("REDDIT_USERNAME"))
# print("Password:", os.getenv("REDDIT_PASSWORD"))
# print("User Agent:", os.getenv("REDDIT_USER_AGENT"))
# print("USERNAME", os.getenv("REDDIT_USERNAME"))