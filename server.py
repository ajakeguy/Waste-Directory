#!/usr/bin/env python3
"""
Simple HTTP server for Vermont Waste Hauler Directory
Run: python3 server.py
Then open: http://localhost:8000
"""

import http.server
import socketserver
import os
import json

PORT = 8000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
    
    def end_headers(self):
        # Add CORS headers for local development
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"🗑️  Vermont Waste Hauler Directory")
        print(f"=" * 50)
        print(f"Server running at: http://localhost:{PORT}")
        print(f"=" * 50)
        print(f"\nFeatures:")
        print(f"  • Search by company, town, or address")
        print(f"  • Filter by state and waste type")
        print(f"  • Interactive map with hauler locations")
        print(f"  • {json.load(open(os.path.join(DIRECTORY, 'vermont_haulers.json')))} haulers in database")
        print(f"\nPress Ctrl+C to stop")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\nServer stopped.")
