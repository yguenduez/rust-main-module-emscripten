#!/usr/bin/env python3
"""
Simple HTTP server for serving WebAssembly files with correct MIME types.
This server adds the proper MIME type for .wasm files and other common web files.
"""

import http.server
import socketserver
import sys
import os

PORT = 8000

class WasmHandler(http.server.SimpleHTTPRequestHandler):
    """HTTP request handler with WASM MIME type support."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def end_headers(self):
        # Add CORS headers to allow cross-origin requests if needed
        self.send_header('Cross-Origin-Opener-Policy', 'same-origin')
        self.send_header('Cross-Origin-Embedder-Policy', 'require-corp')
        super().end_headers()

    def guess_type(self, path):
        """Override guess_type to add WASM and other web-related MIME types."""
        mimetype = super().guess_type(path)

        # Add custom MIME types
        if path.endswith('.wasm'):
            return 'application/wasm'
        elif path.endswith('.js'):
            return 'application/javascript'
        elif path.endswith('.mjs'):
            return 'application/javascript'
        elif path.endswith('.json'):
            return 'application/json'
        elif path.endswith('.wat'):
            return 'text/plain'

        return mimetype

def main():
    """Start the HTTP server."""
    # Allow specifying port as command-line argument
    port = PORT
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            print(f"Invalid port number: {sys.argv[1]}")
            print(f"Usage: {sys.argv[0]} [port]")
            sys.exit(1)

    # Allow specifying directory as second argument
    directory = os.getcwd()
    if len(sys.argv) > 2:
        directory = sys.argv[2]
        if not os.path.isdir(directory):
            print(f"Directory not found: {directory}")
            sys.exit(1)
        os.chdir(directory)

    print(f"Starting HTTP server...")
    print(f"Serving directory: {os.getcwd()}")
    print(f"Server running at: http://localhost:{port}/")
    print(f"Press Ctrl+C to stop the server")

    with socketserver.TCPServer(("", port), WasmHandler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\nShutting down server...")
            httpd.shutdown()
            print("Server stopped.")

if __name__ == "__main__":
    main()
