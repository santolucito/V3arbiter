#!/usr/bin/env python3
import http.server
import ssl
import socketserver
import os

PORT = 8443
CERT_FILE = "cert.pem"
KEY_FILE = "key.pem"

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add CORS headers for mobile compatibility
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

def main():
    # Check if certificate files exist
    if not os.path.exists(CERT_FILE) or not os.path.exists(KEY_FILE):
        print(f"Error: Certificate files {CERT_FILE} and {KEY_FILE} not found!")
        print("Please run the OpenSSL command to generate them first.")
        return

    # Create HTTPS server
    with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
        # Create SSL context
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        context.load_cert_chain(CERT_FILE, KEY_FILE)

        # Wrap the socket with SSL
        httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

        print(f"HTTPS Server running on https://localhost:{PORT}")
        print(f"For mobile access, use your computer's IP address:")
        print(f"Find your IP with: hostname -I")
        print(f"Then visit: https://YOUR_IP:{PORT}/pizza-delivery-game.html")
        print("\nNote: You'll need to accept the self-signed certificate warning.")

        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")

if __name__ == "__main__":
    main()