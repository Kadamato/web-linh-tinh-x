#!/usr/bin/env python3
"""
Lightweight HTTP Server for About Sen Clone
Supports full Range requests for HTML5 videos and proper MIME types for 3D GLB/HDR models.
"""
import http.server
import socketserver
import os
import sys

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 3000

class CustomHTTPHandler(http.server.SimpleHTTPRequestHandler):
    extensions_map = {
        **http.server.SimpleHTTPRequestHandler.extensions_map,
        '.glb': 'model/gltf-binary',
        '.gltf': 'model/gltf+json',
        '.hdr': 'image/vnd.radiance',
        '.webp': 'image/webp',
        '.m4v': 'video/mp4',
        '.mov': 'video/quicktime',
        '.mp4': 'video/mp4',
        '.wasm': 'application/wasm',
        '.js': 'text/javascript',
        '.css': 'text/css'
    }

    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), CustomHTTPHandler) as httpd:
        print(f"🚀 About Sen clone running at: http://localhost:{PORT}/")
        print("Press Ctrl+C to stop.")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server.")
