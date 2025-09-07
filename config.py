import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8385471447:AAFDC4_o8tZ2RHXPfZXTeZGkyzEd5kixMCs")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "29435108"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "2d211eb63606dae1bcb413d57391b2de")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "6050965589"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "mongodb+srv://sumitdudhe2002_db_user:sumitdudhe2002_db_user@cluster0.z05z19f.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "cluster0")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
