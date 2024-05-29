import os

API_ID = API_ID = 22789024

API_HASH = os.environ.get("API_HASH", "05dd73c56053828044cb71216cdfd0cc")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6855450527:AAE_ij9agZiig5QdZQl2bs3ddPtSEoUSOKs")

PASS_DB = int(os.environ.get("PASS_DB",))

OWNER = int(os.environ.get("OWNER", 6791986779))

LOG = -1002070057679

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5987970971").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


