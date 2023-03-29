from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    name = request.args.get('name', 'BOB')
    return f"Bonjour, {name}!"

if __name__ == "__main__":
    app.run()