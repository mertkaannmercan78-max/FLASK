import random
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<h1>Yiğit Emir MERCAN</h1>'
@app.route("/bilgiler")
def bilgi():
    bilgiler = ["2018 yılında yapılan bir araştırmaya göre 18-34 yaş arası kişilerin %50'den fazlası kendilerini akıllı telefonlarına bağımlı olarak görüyor.", "Teknolojik bağımlılık çalışması, modern bilimsel araştırmanın en ilgili alanlarından biridir.", "Sosyal ağların olumlu ve olumsuz yanları vardır ve bu platformları kullanırken her ikisinin de farkında olmalıyız."]
    return '<p>' + random.choice(bilgiler) + '</p>'
app.run(debug=True)
