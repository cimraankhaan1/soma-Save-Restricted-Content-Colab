import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7778777103:AAHSSxjAIPyE13XhFkGDfHhjwN4kOGJpPY0")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "19169648"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "6e4a72fc13ac3486344ea662b002eaed")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://khaanbarwaani:qL47JyUNrzSRp2Aj@cluster0.qgucx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
