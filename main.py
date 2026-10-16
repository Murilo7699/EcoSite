
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/lights/<size>")
def lights(size):
    return render_template("lights.html", size=size)


@app.route("/result/<size>/<int:lights>")
def result(size, lights):
    points = 0

    if size == "pequena":
        points += 5
    elif size == "media":
        points += 3
    elif size == "grande":
        points += 1

    if lights <= 3:
        points += 5
    elif lights <= 6:
        points += 3
    else:
        points += 1

    if points >= 9:
        level = "🌱 Eco Master"
        description = (
            "Parabéns! Você é um verdadeiro Eco Master! "
            "Seu compromisso com a sustentabilidade é inspirador."
        )
    elif points >= 6:
        level = "💡 Econômica"
        description = (
            "Ótimo trabalho! Sua casa possui um bom equilíbrio "
            "entre conforto e economia de energia."
        )
    else:
        level = "⚠️ Alto Consumo"
        description = (
            "Sua casa possui um consumo elevado de energia. "
            "Considere reduzir o número de lâmpadas e otimizar o consumo."
        )

    return render_template(
        "result.html",
        size=size,
        lights=lights,
        points=points,
        level=level,
        description=description
    )


if __name__ == "__main__":
    app.run(debug=True)
