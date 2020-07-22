from flask import flask


app = Flask(__name__)


@app.route('/')
def index():
    print("f u")


if __name__ == "__main__":
    app.run(debug=True)
