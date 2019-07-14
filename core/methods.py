import aiohttp
from aiohttp import web

from settings import APPLICATION_SECRET, APP_DOMAIN, TG_BOT_TOKEN


API_URL = f'https://api.telegram.org/bot{TG_BOT_TOKEN}/'
HEADERS = {'Content-Type': 'application/json'}


async def send_message(chat_id, text):
    url = API_URL + 'sendMessage'
    data = dict(chat_id=chat_id, text=text)
    response = await _post(url, data)
    if response.status != 200:
        return web.Response(status=500)

    return web.Response(status=200)


async def reload_web_hook():
    await _remove_web_hook()
    await _set_web_hook()


async def _post(url, json):
    async with aiohttp.ClientSession(conn_timeout=5.) as session:
        async with session.post(url, json=json, headers=HEADERS) as response:
            return response


async def _set_web_hook():
    url = API_URL + 'setWebhook'
    data = dict(url=f'{APP_DOMAIN}/{APPLICATION_SECRET}')
    return await _post(url, data)


async def _remove_web_hook():
    url = API_URL + 'deleteWebhook'
    return await _post(url, None)
