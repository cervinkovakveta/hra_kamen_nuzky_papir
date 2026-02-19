# importuje modul flask (Flask, render_template, request)
from flask import Flask, render_template, request

# importuje vestavěný modul random
import random               # modul na náhodný výběr

# vytvoří instanci třídy flask - aplikace (server)
app = Flask(__name__)

# definuje funkci pro obsluhu stránky pro hru
@app.route("/hra", methods=["GET", "POST"])      # dekorátor
def hra():
    tahy = ["kámen", "nůžky", "papír"]
    tah_pocitace = random.choice(tahy)           # náhodný výběr počítače - kámen, nužky, papír

    tah_uzivatele = None
    vysledek = None
    # po odeslání formuláře uloží zakliknutou odpověď
    if request.method == "POST":
        tah_uzivatele = request.form.get("tah")
        vysledek = vyhodnoceni_hry(tah_uzivatele,tah_pocitace)
    return render_template("kamen_nuzky_papir_1.html", vysledek=vysledek, tah_uzivatele=tah_uzivatele, tah_pocitace=tah_pocitace)
# definuje funkci pro vyhotovení hry
def vyhodnoceni_hry(tah_uzivatele, tah_pocitace):
    vitezne_tahy = [("kámen", "nůžky"), ("nůžky", "papír"), ("papír", "kámen")]
    if tah_uzivatele == tah_pocitace:
        return "remiza"
    elif (tah_uzivatele, tah_pocitace) in vitezne_tahy:
        return "výhra"
    else:
        return "prohra"

# zkrontroluje přímé spuštění programu
if __name__ == "__main__":
    # spustí server
    app.run(debug=True, port=5000)