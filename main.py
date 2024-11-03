from flask import Flask,render_template


app = Flask(__name__)


@app.get("/")
def index():
    return render_template("index.html")


@app.get("/menu/")
def menu():
    pizzas = [
        {"name": "пеперонi", "ingridients":"ковбаса пеперонi,сир пеперонi", "price": 10},
        {"name": "класична", "ingridients": "помидори,cир,соус", "price":120 },
        {"name": "моцарела", "ingridients": "пеперони,cир бальзам,соус", "price":100 }
   ] 
    return render_template("menu.html",pizzas=pizzas)

if __name__ == "__main__":
    app.run(debug=True, port=80)









