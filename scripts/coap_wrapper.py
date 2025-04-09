#!/usr/bin/env python3
import asyncio 
import sys   
from aiocoap import Context, Message, error  

# This function sends a CoAP request asynchronously
async def send_coap_request(method, uri, payload_hex=None):
    try:
        # Create a CoAP client context (like opening a connection)
        context = await Context.create_client_context()

        # If a payload is provided in hex format, convert it to bytes
        payload = bytes.fromhex(payload_hex) if payload_hex else None

        # Create a CoAP message with the given method, URI, and optional payload
        request = Message(code=method, uri=uri, payload=payload)

        # Send the request and wait for the response
        response = await context.request(request).response

        # Return the payload of the response in hex format (if it exists)
        return response.payload.hex() if response.payload else None

    # If the URI is not in a proper format, show an error message
    except error.MalformedUrlError:
        print(f"ERROR: Invalid URI - must be like: coap://[IP]/path")
        sys.exit(1)

    # Catch all other errors and print the error type and message
    except Exception as e:
        print(f"CoAP error: {type(e).__name__}: {e}")
        sys.exit(1)

# This block runs only if the script is executed directly (not imported)
if __name__ == "__main__":
    # Check if the required arguments are provided
    if len(sys.argv) < 3:
        # Show correct usage instructions
        print("Usage: ./coap_wrapper.py <METHOD> <URI> [PAYLOAD_HEX]")
        print("Example: ./coap_wrapper.py POST coap://[IP]/path 48656c6c6f")
