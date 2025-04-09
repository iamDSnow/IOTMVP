# coap_test_server.py
from aiocoap import *
from aiocoap.resource import Resource, Site
import asyncio

class CoAPResource(Resource):
    async def render_get(self, request):
        return Message(payload=b"</.well-known/core>;ct=40")

    async def render_post(self, request):
        return Message(payload=b"Received: " + request.payload)
    
class Resource(Resource):
    async def render_get(self, request):
        print(f"Received GET from {request.remote.host}")
        return Message(payload=b"Test response")
async def main():
    # Create resource tree
    root = Site()
    protocol = await Context.create_server_context(Resource())
    print("CoAP server running on 0.0.0.0:5683")
    await asyncio.get_running_loop().create_future()

    # Create server context
    context = await Context.create_server_context(root)
    print("CoAP server running on port 5683")
    await asyncio.get_event_loop().create_future()

if __name__ == "__main__":
    asyncio.run(main())



