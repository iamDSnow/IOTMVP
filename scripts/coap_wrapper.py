#!/usr/bin/env python3

import asyncio
import sys
from aiocoap import Context, Message, error
from aiocoap.numbers.codes import Code

# This function sends a CoAP request asynchronously
async def send_coap_request(method, uri, payload_hex=None):
    try:
        # Create a CoAP client context (like opening a connection)
        context = await Context.create_client_context()

        # Convert payload from hex string to bytes if provided, otherwise send empty bytes
        payload = bytes.fromhex(payload_hex) if payload_hex else b""

        # Map string method to CoAP code enum
        method_codes = {'GET': Code.GET, 'POST': Code.POST}
        if method not in method_codes:
            raise ValueError("Unsupported method. Use GET or POST.")

        # Create and send the CoAP request
        request = Message(code=method_codes[method], uri=uri, payload=payload)
        response = await context.request(request).response

        # Return the response payload in hex (or a string, if preferred)
        return response.payload.hex() if response.payload else None

    # Handle improperly formatted URIs
    except error.MalformedUrlError:
        print(f"ERROR: Invalid URI - must be like: coap://[IP]/path")
        raise Exception("Check the URI")

    # Handle any other unexpected errors
    except Exception as e:
        print(f"CoAP error: {type(e).__name__}: {e}")
        raise Exception("Error in the CoAP request")

# Entry point for command-line usage
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: ./coap_wrapper.py <METHOD> <URI> [PAYLOAD_HEX]")
        print("Example: ./coap_wrapper.py POST coap://192.168.1.100/nanolink 48656c6c6f")
        sys.exit(1)

    try:
        # Run the async function and print the response
        response = asyncio.run(send_coap_request(
            sys.argv[1].upper(),
            sys.argv[2],
            sys.argv[3] if len(sys.argv) > 3 else None
        ))
        print(f"Response: {response}" if response else "Empty response")

    except Exception as final_error:
        print(f"Request failed: {final_error}")
        sys.exit(1)
