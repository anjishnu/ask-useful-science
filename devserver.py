from flask import Flask, request
from lambda_function import lambda_handler

server = Flask(__name__)

@server.route('/')
def main():
    return lambda_handler(request.to_json())

if __name__ == "__main__":
    server.run()
