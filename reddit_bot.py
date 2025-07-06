# import praw
# import os
# import requests
# from dotenv import load_dotenv
# import time

# load_dotenv()
# reddit = praw.Reddit(
#     client_id=os.getenv("REDDIT_CLIENT_ID"),
#     client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
#     username=os.getenv("REDDIT_USERNAME"),
#     password=os.getenv("REDDIT_PASSWORD"),
#     user_agent=os.getenv("REDDIT_USER_AGENT")
# )
# print("The username is: ", reddit.user.me())
# SUBREDDIT_NAME = "wordcorntestingsanjai"
# # def post_to_reddit(title, image_url, subreddit_name="wordcorntestingsanjai"):
# #     image_data = requests.get(image_url).content
# #     temp_filename = "temp_image.jpg"
# #     with open(temp_filename, "wb") as f:
# #         f.write(image_data)
# #     subreddit = reddit.subreddit(subreddit_name)
# #     subreddit.submit_image(title=title, image_path=temp_filename)
# #     print(f"Posted to r/{SUBREDDIT_NAME}: {title}")
# #     os.remove(temp_filename)
# # print("CLIENT_ID:", os.getenv("REDDIT_CLIENT_ID"))
# # print("USERNAME:", os.getenv("REDDIT_USERNAME"))
# # print("PASSWORD:", os.getenv("REDDIT_PASSWORD"))
# # print("SECRET:", os.getenv("REDDIT_CLIENT_SECRET"))

# def post_to_reddit(title, image_url, description ,subreddit_name="wordcorntestingsanjai"):
    
#     subreddit = reddit.subreddit(subreddit_name)
#     image_data = requests.get(image_url).content
#     temp_filename = "temp_image.jpg"
#     with open(temp_filename, "wb") as f:
#         f.write(image_data)
#     submission = subreddit.submit_image(title=title, image_path=temp_filename)
#         # submission = subreddit.submit_image(title=title, image_path=temp_filename)
#     # submission = subreddit.submit(title=title, selftext=description, inline_media=[media])
#     # submission = subreddit.submit(
#     #     title=title,
#     #     selftext=description,
#     #     inline_media=[media]
#     # )
#     # Immediately edit the post to add the description under the image
#     submission.edit(description)
#     # submission.edit(description)
#     os.remove(temp_filename)
#     print(f"Posted to r/{SUBREDDIT_NAME}: {title}")
#     # submission.edit(description)

#     #Embed image and description in the selftext using Reddit Markdown
#     # selfText = f"![]({image_url})\n\n{description}"
#     #Submit as a text post
#     # subreddit.submit(
#     #     title=title,
#     #     selftext=selfText,
#     #     inline_media=[media]
#     # )
#     #upload the image

#     #Post as a text post with image preview + description as body
#     # subreddit.submit(
#     #     title=title,
#     #     selftext=description,
#     #     url=None,
#     #     resubmit=False,
#     #     send_replies=False,
#     #     flair_id=None,
#     #     flair_text=None,
#     #     collection_id=None,
#     #     without_websocket=True,
#     #     inline_media=[media]
#     # )

#     # submission = subreddit.submit_image(title=title, image_path=temp_filename)
#     # print(f"Posted to r/{SUBREDDIT_NAME}: {title}")
#     # time.sleep(5)

#     # os.remove(temp_filename)
# print("CLIENT_ID:", os.getenv("REDDIT_CLIENT_ID"))
# print("USERNAME:", os.getenv("REDDIT_USERNAME"))
# print("PASSWORD:", os.getenv("REDDIT_PASSWORD"))
# print("SECRET:", os.getenv("REDDIT_CLIENT_SECRET"))


# # def post_to_reddit(title, image_path, subreddit_name="test"):

# #     subreddit = reddit.subreddit(subreddit_name)
# #     subreddit.submit_image(title=title, image_path=image_path)
# #     print(f" Posted to r/{subreddit_name}: {title}")

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

def post_to_reddit(title, image_url, description, subreddit_name="wordcorntestingsanjai"):
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
    print(f"✅ Posted to r/{subreddit_name}: {title}")
