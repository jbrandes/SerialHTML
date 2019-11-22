from flask import Flask, render_template, request, flash, redirect, url_for
import datetime
import serial
import time
import cgi
import sys
import mimetypes
import socket




app = Flask(__name__)

@app.route("/time", methods = ['GET', 'POST'])
def sensor():
    arduino = serial.Serial('/dev/ttyUSB0', 9600, timeout = 20)
    while True:
        data = arduino.readline()[:-2]
        if data:
             f = open("time.txt","a")
             f.write("The time is now: " + str(data))
             print(data)
             f.close()
                        
           
            
    return app.response_class(generate(), mimetype='text/plaintext')
            

@app.route("/", methods=['GET', 'POST'])
def hello():
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, threaded=True)
