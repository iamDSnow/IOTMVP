PROXY_URL = "http://your-proxy-server:8080"  # Your HTTP-to-CoAP proxy
NETWORK_CONFIG = {
    "device_type": "ipv4",
    "network_name": "linksnet",
    "default_timeout": 30,
    "retry_attempts": 3,
        "manual_ip": "none"  # Replace with actual IP

}

APN_CONFIG = {
    "apn": "linksnet",  # Replace with your Linksnet APN
    "ip_version": 4,              # Using IPv4
    "auth_type": "none",          # or 'pap', 'chap' if required
    "username": "",               # If required by Linksnet
    "password": ""                # If required by Linksnet
}