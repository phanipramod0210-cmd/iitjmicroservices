from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.request

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if self.path == "/users":
                url = "http://192.168.56.101:8001/users"

            elif self.path == "/orders":
                url = "http://192.168.56.102:8002/orders"

            else:
                self.send_response(404)
                self.end_headers()
                return

            data = urllib.request.urlopen(url, timeout=5).read()

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()

            self.wfile.write(data)

        except Exception as e:
            msg = f"Gateway Error: {e}".encode()

            self.send_response(502)
            self.send_header("Content-Type", "text/plain")
            self.send_header("Content-Length", str(len(msg)))
            self.end_headers()

            self.wfile.write(msg)

server = HTTPServer(("0.0.0.0", 8000), Handler)
print("API Gateway running on port 8000")
server.serve_forever()
