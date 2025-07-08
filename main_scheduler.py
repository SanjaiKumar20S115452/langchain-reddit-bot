import schedule
import time
import json
import os
from reddit_bot import post_to_reddit

POSTED_LOG = "posted_log.json"
def load_posted2():
    try:
        if os.path.exists(POSTED_LOG):
            with open(POSTED_LOG, "r") as f:
                data = json.load(f)
                return set(data if data is not None else [])
        else:
            return set()
    except Exception as e:
        print("Error loading posted_log.json:", e)
        return set()
    
def save_posted2(posted_set):
    try:
        with open(POSTED_LOG, "w") as f:
            json.dump(list(posted_set), f)
    except Exception as e:
        print("Error saving posted_log.json")

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
        description = meme.get("definition", "")
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

schedule.every().day.at("20:00").do(post_meme)
# schedule.every(1).minute.do(post_meme)

def start_bot():
    print("LangChain Reddit Bot is running........")
    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    start_bot()


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