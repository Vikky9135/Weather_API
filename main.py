from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("Home.html")


@app.route("/api/v1/<station>/<date>")
def about(station, date):
    temperature = 23
    return {"station": station,
            "date": date,
            "Temperature": temperature }


if __name__ == "__main__":
    app.run(debug=True)