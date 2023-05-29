from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/otobus')
def otobus():
    return render_template("otobus.html")

@app.route('/otobus_biletleri')
def otobus_biletleri():
    return render_template("otobus_biletleri.html")


@app.route('/tren')
def tren():
    return render_template("tren.html")

@app.route('/tren_biletleri')
def tren_biletleri():
    return render_template("tren_biletleri.html")


if __name__ == "__main__":
    app.run(debug=True)
