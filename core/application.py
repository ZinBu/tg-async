import asyncio

from aiohttp import web

from core.methods import reload_web_hook, send_message
from settings import APPLICATION_SECRET

routes = web.RouteTableDef()


@routes.post(f'/{APPLICATION_SECRET}')
async def handler(request):
    # Extend by your logic from here
    data = await request.json()
    return await send_message(
        chat_id=data['message']['chat']['id'],
        text=data['message']['text']
    )

app = web.Application()
app.add_routes(routes)


if __name__ == '__main__':
    asyncio.run(reload_web_hook())
    web.run_app(app)
