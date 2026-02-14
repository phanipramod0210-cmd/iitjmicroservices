from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/orders":
            body = json.dumps({
                "orders": ["order-101", "order-102"]
            }).encode()

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()

            self.wfile.write(body)
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not Found")

server = HTTPServer(("0.0.0.0", 8002), Handler)
print("Order Service running on port 8002")
server.serve_forever()
