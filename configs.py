# (c) @Moon_God_Khonsu

import os
                                                                
class Config(object):
        API_ID = int(os.environ.get("API_ID", "26614080"))
        API_HASH = os.environ.get("API_HASH", "7d2c9a5628814e1430b30a1f0dc0165b")
        BOT_TOKEN = os.environ.get("BOT_TOKEN", "7288227872:AAELu6rrPTgkQpsmYbgO9KlWEorISSVKXq8")
        BOT_USERNAME = os.environ.get("BOT_USERNAME", "Free_Hollywood_MoviesRoBot")   
        DB_CHANNEL = int(os.environ.get("DB_CHANNEL", " -1002163667002"))
        BOT_OWNER = int(os.environ.get("BOT_OWNER", "5606990991"))
        DATABASE_URL = os.environ.get("mongodb+srv://mrsudoxspam:mrsudoxspam@cluster0.ufwidpg.mongodb.net/?retryWrites=true&=true&w=majority")
        UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1001902665212")
        LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "-1002185392163")
        BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
        FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
        BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
        BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
        OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
        ABOUT_BOT_TEXT = f"""
This is Permanent Files Store Bot!
Send me any file I will save it in my Database. Also works for channel. Add me to channel as Admin with Edit Permission, I will add Save Uploaded File in Channel & add Sharable Button Link.

🤖 **My Name:** [Files Store Bot](https://t.me/Free_Hollywood_MoviesRoBot)

📝 **Language:** [Python3](https://www.python.org)

📚 **Library:** [Pyrogram](https://docs.pyrogram.org)

📡 **Hosted on:** [Heroku](https://heroku.com)

🧑🏻‍💻 **Developer:** @Moon_God_Khonsu

👥 **Support Group:** [INDIAN HACKER](https://t.me/INDIAN_HACKER_GROUP)

📢 **Updates Channel:** [PBAIL CHANNEL](https://t.me/Pbail_Movie_Channel)
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 **Developer:** @Moon_God_Khonsu

"""
	HOME_TEXT = """
Hi, [{}](tg://user?id={})\n\nThis is Permanent **File Store Bot**.

Send me any file I will give you a permanent Sharable Link. I Support Channel Also! Check **About Bot** Button.
"""
