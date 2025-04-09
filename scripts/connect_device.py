#!/usr/bin/env python3
from mtb04_connector import MTB04Connector
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config.settings import PROXY_URL, NETWORK_CONFIG, APN_CONFIG

def main():
    print("Initializing MTB04 Connector for Linksnet IPv4...")
    connector = MTB04Connector(
        proxy_url=PROXY_URL,
        network_config=NETWORK_CONFIG,
        apn_config=APN_CONFIG
    )
    
    # Try to discover device (in real implementation, might scan network)
    print("\nAttempting to discover device...")
    device_ip = connector.discover_device()
    
    if device_ip:
        print(f"Discovered device at {device_ip}")
        
        # Configure APN for Linksnet
        print("\nConfiguring APN...")
        apn_result = connector.configure_apn()
        print(apn_result)
        
        # Get device status
        print("\nGetting device status...")
        status = connector.get_device_status()
        print(status)
    else:
        print("Could not discover device automatically. Please:")
        print("1. Check device is powered on (blue LED)")
        print("2. Verify it's connected to Linksnet network")
        print("3. Manually specify IP address in settings.py if known")

if __name__ == "__main__":
    main()