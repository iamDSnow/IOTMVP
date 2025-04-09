#!/usr/bin/env python3
import asyncio
from aiohttp import web
from aiocoap import Context, Message
from aiocoap.numbers.codes import Code

async def handle(request):
    """Handle HTTP requests and forward to CoAP server"""
    try:
        # Parse query parameters
        method = request.query.get('method', 'GET').upper()
        uri = request.query.get('uri', '')
        payload = request.query.get('payload', None)

        # Validate parameters
        if not uri:
            return web.Response(
                text="Missing URI parameter",
                status=400,
                content_type='text/plain'
            )

        # Convert method to CoAP code
        method_map = {'GET': Code.GET, 'POST': Code.POST}
        if method not in method_map:
            return web.Response(
                text=f"Invalid method {method}. Use GET or POST",
                status=400,
                content_type='text/plain'
            )

        # Create CoAP request
        coap_request = Message(
            code=method_map[method],
            uri=uri,
            payload = bytes.fromhex(payload) if payload else b''
        )

        # Send CoAP request
        context = await Context.create_client_context()
        coap_response = await context.request(coap_request).response

        return web.Response(
            text=f"CoAP response: {coap_response.payload.decode(errors='replace')}",
            content_type='text/plain'
        )

    except Exception as e:
        return web.Response(
            text=f"CoAP request failed: {str(e)}",
            status=500,
            content_type='text/plain'
        )

async def init_app():
    """Initialize the web application"""
    app = web.Application()
    app.router.add_get('/coap', handle)
    return app

if __name__ == '__main__':
    print("Starting HTTP-to-CoAP proxy on http://0.0.0.0:8080")
    web.run_app(init_app(), host='0.0.0.0', port=8080)