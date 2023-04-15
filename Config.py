import os


class Config():
    # Bu dəyərləri my.telegram.org saytından əldə edin
    #>>> https://my.telegram.org
    API_ID = int(os.environ.get("API_ID",""))
    API_HASH = os.environ.get("API_HASH","")
    BOT_TOKEN = os.environ.get("BOT_TOKEN","5337183930:")
    BOT_USERNAME = os.environ.get("BOT_USERNAME","dejavy")
    BOT_NAME = os.environ.get("BOT_NAME","goldtag")
    BOT_ID = int(os.environ.get("BOT_ID","-"))
    SUDO_USERS = os.environ.get("SUDO_USERS","").split()
    SUPPORT_CHAT = os.environ.get("SUPPORT_CHAT","ioj")
    OWNER_ID = int(os.environ.get("OWNER_ID","5154387018"))
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME","uijio;kl,")
