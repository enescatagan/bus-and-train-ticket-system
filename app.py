from flask import Flask, render_template
import requests
from bus import Bus
from train import Train

#bus data without seats https://api.npoint.io/3a22c5b61aa1f46639cb
bus_json = requests.get("https://api.npoint.io/6bf62bd3840119596101").json()
bus_tickets = []
for bus_ticket in bus_json:
    bus_tick_obj = Bus(bus_ticket["id"], bus_ticket["company"], bus_ticket["departure"], bus_ticket["destination"], bus_ticket["date"], bus_ticket["time"], bus_ticket["fee"], bus_ticket["seats"])
    bus_tickets.append(bus_tick_obj)

#tren data without compartments and seats https://api.npoint.io/6d3c5a8f8064dfbd6be3
tren_json = requests.get("https://api.npoint.io/6bf62bd3840119596101").json()
train_tickets = []
for train_ticket in tren_json:
    train_tick_obj = Train(train_ticket["id"], train_ticket["company"], train_ticket["departure"], train_ticket["destination"], train_ticket["date"], train_ticket["time"], train_ticket["fee"], train_ticket["compartments"], train_ticket["seats"])
    train_tickets.append(train_tick_obj)

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
