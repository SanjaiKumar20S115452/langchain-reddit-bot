import praw
import os
import requests
from dotenv import load_dotenv
import time

load_dotenv()

reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    username=os.getenv("REDDIT_USERNAME"),
    password=os.getenv("REDDIT_PASSWORD"),
    user_agent=os.getenv("REDDIT_USER_AGENT")
)

def post_to_reddit(title, image_url, description, subreddit_name="wordcorn"):
    subreddit = reddit.subreddit(subreddit_name)

    # Download the image
    image_data = requests.get(image_url).content
    temp_filename = "temp_image.jpg"
    with open(temp_filename, "wb") as f:
        f.write(image_data)

    # Upload the image with the title
    submission = subreddit.submit_image(title=title, image_path=temp_filename)

    time.sleep(5)

    # Edit the post to add the description (visible only when clicked)
    submission.edit(description)

    # Cleanup
    os.remove(temp_filename)
<<<<<<< HEAD
    print(f"✅ Posted to r/{subreddit_name}: {title}")
=======
    print(f"✅ Posted to r/{subreddit_name}: {title}")
