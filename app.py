from flask import Flask, render_template
from bus import Bus
from train import Train

bus_tickets = []
for bus_ticket in bus_tickets:
    bus_tick_obj = Bus(bus_ticket["id"], bus_ticket["company"], bus_ticket["departure"], bus_ticket["destination"], bus_ticket["date"], bus_ticket["time"], bus_ticket["fee"])

train_tickets = []
for train_ticket in train_tickets:
    bus_tick_obj = Train(train_ticket["id"], train_ticket["company"], train_ticket["departure"], train_ticket["destination"], train_ticket["date"], train_ticket["time"], train_ticket["fee"])

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/otobus')
def otobus():
    return render_template("otobus.html")

@app.route('/otobus_biletleri')
def otobus_biletleri():
    return render_template("otobus_biletleri.html", bus_tickets=bus_tickets)


@app.route('/tren')
def tren():
    return render_template("tren.html")

@app.route('/tren_biletleri')
def tren_biletleri():
    return render_template("tren_biletleri.html", train_tickets=train_tickets)


if __name__ == "__main__":
    app.run(debug=True)
