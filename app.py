from flask import Flask
app = Flask(__name__)

@app.route("/", methods=['GET'])
def home():
    return "<h1> Tsering's first app</h1>"

if __name__ == "__main__":
    app.run()

