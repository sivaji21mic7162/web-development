from flask import Flask
from flask.sansio.scaffold import default_exceptions

app = Flask(__name__)

@app.route("/")
def hello_world():
  return "Hello, Nani!"

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)

