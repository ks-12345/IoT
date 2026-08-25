from flask import Flask, render_template, jsonify
import threading
import time

app = Flask(__name__)

semaforo = {"cor": "vermelho", "piscar": False}

def ciclo_semaforo():
    while True:
        # Verde aceso
        semaforo["cor"] = "verde"
        semaforo["piscar"] = False
        time.sleep(5)

        # Amarelo aceso
        semaforo["cor"] = "amarelo"
        semaforo["piscar"] = False
        time.sleep(2)

        # Vermelho piscando por 5 segundos (piscar a cada 0.5 seg)
        semaforo["cor"] = "vermelho"
        for _ in range(10):
            semaforo["piscar"] = True
            time.sleep(0.5)
            semaforo["piscar"] = False
            time.sleep(0.5)

threading.Thread(target=ciclo_semaforo, daemon=True).start()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/status")
def status():
    return jsonify(semaforo)

if __name__ == "__main__":
    app.run(debug=True)
