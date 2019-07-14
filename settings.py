import os

APPLICATION_SECRET = (
    os.getenv('APPLICATION_SECRET')
    or 'Your_app_secret_here'
)

TG_BOT_TOKEN = (
    os.getenv('TG_BOT_TOKEN')
    or 'Your bot token'
)

APP_DOMAIN = (
    os.getenv('APP_DOMAIN')
    or 'Your heroku app address'
)
