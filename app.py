from flask import Flask, render_template, request, jsonify
from utils.person import Person
from chat import next_step

app = Flask(__name__)


@app.get("/")
def index_get():
    return render_template("base.html")


@app.post("/predict")
def predict():
    person = Person(None, None, None)
    text = request.get_json().get("message")
    response = next_step(text, person)
    response = "Hi"
    message = {"answer": response}
    return jsonify(message)

if __name__ == "__main__":
    app.run(debug=True)