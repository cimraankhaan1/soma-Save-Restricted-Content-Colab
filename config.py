import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7876974862:AAEF9cAIG6L2SiQCZrtq1yDUqvtrhwVuKzw")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "17461958"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "0f083cb4779252f82b99f5c644274624")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://khaanbarwaani:qL47JyUNrzSRp2Aj@cluster0.qgucx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
