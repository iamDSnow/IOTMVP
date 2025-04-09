import asyncio
from aiohttp import web
from coap_wrapper import send_coap_request

async def handle(request):
    # Extract HTTP query parameters
    method = request.query.get('method', 'GET').upper()
    uri = request.query.get('uri', '')
    payload = request.query.get('payload', None)

    if not uri:
        return web.Response(status=400, text="Missing URI parameter")

    # Call the coap_wrapper function
    try:
        coap_response = await send_coap_request(method, uri, payload)
        return web.Response(text=f"CoAP response: {coap_response}" if coap_response else "Empty response")
    except Exception as e:
        return web.Response(status=500, text=f"Error: {str(e)}")

async def init_app():
    app = web.Application()
    app.router.add_get('/coap', handle)  # This route triggers the CoAP logic
    return app

if __name__ == '__main__':
    app = init_app()
    web.run_app(app, host='0.0.0.0', port=8080)  # Running the server
