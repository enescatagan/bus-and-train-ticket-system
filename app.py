from flask import Flask, render_template, request
import requests
from bus import Bus
from train import Train

#https://api.npoint.io/6bf62bd3840119596101
#https://api.npoint.io/d3cbff124991fc033373
bus_json = requests.get("https://api.npoint.io/a9e39f24ebf06a9a3cae").json()
bus_tickets = []
for bus_ticket in bus_json:
    bus_tick_obj = Bus(bus_ticket["id"], bus_ticket["company"], bus_ticket["departure"], bus_ticket["destination"], bus_ticket["date"], bus_ticket["time"], bus_ticket["fee"], bus_ticket["seats"])
    bus_tickets.append(bus_tick_obj)

#tren data without compartments and seats https://api.npoint.io/6d3c5a8f8064dfbd6be3
#https://api.npoint.io/065aef5e4f5e883be8b4
#https://api.npoint.io/84164e811a25f16851e6
#https://api.npoint.io/84164e811a25f16851e6
tren_json = requests.get("https://api.npoint.io/d3cbff124991fc033373").json()
train_tickets = []
for train_ticket in tren_json:
    train_tick_obj = Train(train_ticket["id"], train_ticket["company"], train_ticket["departure"], train_ticket["destination"], train_ticket["date"], train_ticket["time"], train_ticket["fee"], train_ticket["compartments"], train_ticket["seats"])
    train_tickets.append(train_tick_obj)

app = Flask(__name__)
turkiye_illeri = [
    "Adana",
    "Adıyaman",
    "Afyonkarahisar",
    "Ağrı",
    "Amasya",
    "Ankara",
    "Antalya",
    "Artvin",
    "Aydın",
    "Balıkesir",
    "Bilecik",
    "Bingöl",
    "Bitlis",
    "Bolu",
    "Burdur",
    "Bursa",
    "Canakkale",
    "Cankırı",
    "Corum",
    "Denizli",
    "Diyarbakır",
    "Edirne",
    "Elazığ",
    "Erzincan",
    "Erzurum",
    "Eskişehir",
    "Gaziantep",
    "Giresun",
    "Gümüşhane",
    "Hakkâri",
    "Hatay",
    "Isparta",
    "Mersin",
    "Istanbul",
    "Izmir",
    "Kars",
    "Kastamonu",
    "Kayseri",
    "Kırklareli",
    "Kırşehir",
    "Kocaeli",
    "Konya",
    "Kütahya",
    "Malatya",
    "Manisa",
    "Kahramanmaraş",
    "Mardin",
    "Muğla",
    "Muş",
    "Nevşehir",
    "Niğde",
    "Ordu",
    "Rize",
    "Sakarya",
    "Samsun",
    "Siirt",
    "Sinop",
    "Sivas",
    "Tekirdağ",
    "Tokat",
    "Trabzon",
    "Tunceli",
    "Şanlıurfa",
    "Uşak",
    "Van",
    "Yozgat",
    "Zonguldak",
    "Aksaray",
    "Bayburt",
    "Karaman",
    "Kırıkkale",
    "Batman",
    "Sırnak",
    "Bartın",
    "Ardahan",
    "Iğdır",
    "Yalova",
    "Karabük",
    "Kilis",
    "Osmaniye",
    "Düzce"
]

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/otobus')
def otobus():
    return render_template("otobus.html", iller=turkiye_illeri)

@app.route('/bus_search', methods=["POST"])
def bus_search():
    location = request.form.get('location')
    journey = request.form.get('journey')
    selected_date = request.form.get('select-date')
    search = {'location': location, 'journey': journey, 'selected_date': selected_date}
    search['selected_date'] = str(search['selected_date'])
    return render_template("bus_search.html", bus_tickets=bus_tickets, search=search)



@app.route('/otobus_biletleri')
def otobus_biletleri():
    return render_template("otobus_biletleri.html", bus_tickets=bus_tickets)

@app.route('/tren')
def tren():
    return render_template("tren.html",iller=turkiye_illeri)

@app.route('/tren_biletleri')
def tren_biletleri():
    return render_template("tren_biletleri.html", train_tickets=train_tickets)

@app.route('/bus_seats/<int:index>')
def show_bus_seat_grid(index):
    requested_ticket = None
    for bus_ticket in bus_tickets:
        if bus_ticket.id == index:
            requested_ticket = bus_ticket
    return render_template("bus_seats.html", ticket=requested_ticket)

@app.route('/tren_seats/<int:index>')
def show_tren_seat_grid(index):
    requested_ticket = None
    for tren_ticket in train_tickets:
        if tren_ticket.id == index:
            requested_ticket = tren_ticket
    return render_template("tren_seats.html", ticket=requested_ticket)


if __name__ == "__main__":
    app.run(debug=True)
