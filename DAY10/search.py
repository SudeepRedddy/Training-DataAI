from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import json

HOST = "localhost"
PORT = 8000


ROUTES = {
    ("GET", "/products"): "get_products",
}


class SimpleAPI(BaseHTTPRequestHandler):

    def send_json(self, status=200, data=None):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        if data is not None:
            self.wfile.write(json.dumps(data).encode())

    def read_json(self):
        length = int(self.headers.get("Content-Length", 0))
        if length == 0:
            return {}
        body = self.rfile.read(length)
        return json.loads(body)

    def do_GET(self):
        self.handle_route()

    def do_POST(self):
        self.handle_route()

    def handle_route(self):
        parsed_url = urlparse(self.path)
        route = (self.command, parsed_url.path)
        handler_name = ROUTES.get(route)

        if not handler_name:
            self.send_json(404, {"error": "Route not found"})
            return

        handler = getattr(self, handler_name)
        handler()

    def home(self):
        self.send_json(200, {"message": "API running"})

    
    

    def get_products(self):
        parsed_url = urlparse(self.path)
        params = parse_qs(parsed_url.query)

        name = params.get("name", [None])[0]
        max_price = params.get("max_price", [None])[0]

        products = [
            {"id": 1, "name": "Smartphone", "price": 600},
            {"id": 2, "name": "Feature Phone", "price": 100},
            {"id": 3, "name": "Headphones", "price": 150},
            {"id": 4, "name": "Smart Watch", "price": 250},
        ]

        if name:
            products = [p for p in products if name.lower() in p["name"].lower()]

        if max_price:
            try:
                products = [p for p in products if p["price"] <= int(max_price)]
            except ValueError:
                pass

        self.send_json(200, products)


def run():
    server = HTTPServer((HOST, PORT), SimpleAPI)
    print(f"Server running on http://{HOST}:{PORT}")
    server.serve_forever()


if __name__ == "__main__":
    run()
