from flask import Flask, render_template, request
import serial
import time

# Altere 'COM3' conforme a porta do seu Arduino (veja no Gerenciador de Dispositivos)
arduino = serial.Serial('COM4', 9600)
time.sleep(2)  # Aguarda o Arduino reiniciar

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/led/<comando>')
def controle_led(comando):
    if comando in ['A', 'a', 'B', 'b']:
        arduino.write(comando.encode())
        return f"Comando {comando} enviado com sucesso!"
    return "Comando inválido"

if __name__ == '__main__':
    app.run(debug=True)
