#!/usr/bin/env python3
# Locksan Safety - yerel önizleme sunucusu (temiz URL + önbelleksiz)
import http.server, os, urllib.parse, webbrowser, threading, socket
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'site')
class H(http.server.SimpleHTTPRequestHandler):
    def __init__(s, *a, **k): super().__init__(*a, directory=ROOT, **k)
    def end_headers(s):
        s.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        s.send_header('Pragma', 'no-cache'); s.send_header('Expires', '0')
        super().end_headers()
    def translate_path(s, path):
        p = urllib.parse.unquote(path.split('?')[0].split('#')[0])
        full = os.path.join(ROOT, p.lstrip('/'))
        if p == '/': return os.path.join(ROOT, 'index.html')
        if os.path.isfile(full.rstrip('/') + '.html'): return full.rstrip('/') + '.html'
        return full
    def send_error(s, code, message=None, explain=None):
        if code == 404:
            s.send_response(404); s.send_header('Content-Type', 'text/html; charset=utf-8'); s.end_headers()
            s.wfile.write(open(os.path.join(ROOT, '404.html'), 'rb').read()); return
        super().send_error(code, message, explain)
    def log_message(s, *a): pass
PORT = 8765
while True:
    try:
        srv = http.server.ThreadingHTTPServer(('127.0.0.1', PORT), H); break
    except OSError:
        PORT += 1
url = f'http://localhost:{PORT}/'
threading.Timer(1, lambda: webbrowser.open(url)).start()
print(f'Önizleme açık: {url}\nKlasör: {ROOT}\nKapatmak için Ctrl + C')
srv.serve_forever()
