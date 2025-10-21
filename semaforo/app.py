from flask import Flask, render_template
import threading
import time
import serial

# ⚠️ Altere para a porta correta (ex: COM3 no Windows ou /dev/ttyUSB0 no Linux)
arduino = serial.Serial('COM4', 9600, timeout=1)

app = Flask(__name__)

semaforo = {"cor": "vermelho"}

def enviar_para_arduino(cor):
    if arduino.is_open:
        arduino.write((cor.upper() + '\n').encode())

def ciclo_semaforo():
    while True:
        semaforo["cor"] = "verde"
        enviar_para_arduino("VERDE")
        time.sleep(5)

        semaforo["cor"] = "amarelo"
        enviar_para_arduino("AMARELO")
        time.sleep(2)

        semaforo["cor"] = "vermelho"
        enviar_para_arduino("VERMELHO")
        time.sleep(5)

threading.Thread(target=ciclo_semaforo, daemon=True).start()

@app.route("/")
def index():
    return render_template("index.html", cor=semaforo["cor"])

@app.route("/status")
def status():
    return semaforo["cor"]

if __name__ == "__main__":
    app.run(debug=True)
