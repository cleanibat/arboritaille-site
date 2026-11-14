#!/usr/bin/env python3
"""Serveur de prévisualisation local : reproduit les URL propres de .htaccess (/contact -> contact.html, 404 -> 404.html).
Usage : python3 tools/serve.py [port]"""
import http.server, os, sys, urllib.parse
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8766

class H(http.server.SimpleHTTPRequestHandler):
    def translate_path(self, path):
        p = urllib.parse.urlparse(path).path
        if p.endswith('/') and p != '/': p = p[:-1]
        fs = super().translate_path(p)
        if p == '/': return fs
        if not os.path.exists(fs) and os.path.isfile(fs + '.html'): return fs + '.html'
        return fs
    def send_head(self):
        fs = self.translate_path(self.path)
        if not os.path.exists(fs) and not self.path.startswith(('/img/', '/fonts/')):
            self.send_response(404); self.send_header('Content-Type', 'text/html; charset=utf-8'); self.end_headers()
            return open('404.html', 'rb') if os.path.exists('404.html') else None
        return super().send_head()
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store'); super().end_headers()
    def log_message(self, *a): pass

http.server.ThreadingHTTPServer.allow_reuse_address = True
print(f'http://localhost:{PORT}/')
http.server.ThreadingHTTPServer(('127.0.0.1', PORT), H).serve_forever()
