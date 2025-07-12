import schedule
import time
import json
import os
from reddit_bot import post_to_reddit
from firebase_admin import db
from firebase_utils import initialize_firebase

# POSTED_LOG = "posted_log.json"

#Initializing firebase first
initialize_firebase()

def load_posted2():
    try:
        ref = db.reference("posted_memes")
        data = ref.get()
        return set(data or [])
    except Exception as e:
        print("Error loading posted_log.json:", e)
        return set()
    
def save_posted2(posted_set):
    try:
        ref = db.reference("posted_memes")
        ref.set(list(posted_set))
    except Exception as e:
        print("Error saving to Firebase:", str(e))

def post_meme():
    posted = load_posted2()
    try:
        with open("redditwords.json", "r") as f:
            memes = json.load(f)
    except Exception as e:
        print("Error loading memes JSON:", e)
        return 

    for meme in memes:
        image_url = meme.get("memeurl", "")
        if not image_url or image_url in posted:
            continue

        caption = meme.get("word", "")
        definition = meme.get("definition", "")
        description = f"{definition}\n\n🔗 Learn more words at [www.wordcorn.co](https://www.wordcorn.co)"
        # title = caption.strip()
        # print(f"Posting meme: {title}")
        try:
            post_to_reddit(caption, image_url, description)
            posted.add(image_url)
            save_posted2(posted)
            print(f"Posted: {caption}")
        except Exception as e:
            print("Error posting to Reddit:", e)
        break

schedule.every().day.at("01:15").do(post_meme)
# schedule.every(1).minute.do(post_meme)

def start_bot():
    print("LangChain Reddit Bot is running........")
    post_meme()
    

    # def load_posted():
#     try:
#         if os.path.exists(POSTED_LOG):
#             with open(POSTED_LOG, "r") as f:
#                 data = json.load(f)
#             return set(data if data is not None else [])
#     except Exception as e:
#         print("Error loading posted_log.json:", e)
#     return set()


# def save_posted(posted_set):
#     with open(POSTED_LOG, "w") as f:
#         json.dump(list(posted_set), f)

# def post_meme():
#     posted = load_posted()
#     with open("memes.json", "r") as f:
#         memes = json.load(f)
#     for meme in memes:
#         image = meme["image"]
#         if image in posted:
#             continue
#         caption = generate_caption(image)
#         post_to_reddit(caption, image)
#         posted.add(image)
#         save_posted(posted)
#         break