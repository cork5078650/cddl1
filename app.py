from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Clara's Magical App is Live! ✨"

if __name__ == "__main__":
    app.run(debug=True)

