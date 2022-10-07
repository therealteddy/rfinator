from flask import render_template, request, Flask
import random, threading, webbrowser, calc

__author__ = 'Ted Jerin'

app = Flask(__name__)

# First thing to run 
@app.route('/')
def index(): 
    return render_template("index.html")

@app.route("/error", methods=["POST"])
def error(): 
    return render_template('error.html')

# The actual get/post 
@app.route("/receive", methods=['POST']) 
def receive(): 
    solvent_front = float(request.form['solvent_front'])
    amino_acid_displacement = float(request.form['amino_acid'])
    retardation_factor = calc.retardation(amino_acid_displacement,solvent_front)
    rounded_rfac = round(retardation_factor, 2)
    amino_acid_name = calc.checkamino(rounded_rfac)
    return render_template("receive.html", output="The retardation factor is {}".format(str(rounded_rfac)), output1=f"The amino acid is: {amino_acid_name}")

if __name__ == "__main__":
    
    #PORT 
    port = 5000 + random.randint(0,999)

    #LOCALHOST
    url = 'http://127.0.0.1:{0}'.format(port)

    threading.Timer(1.25, lambda: webbrowser.open(url)).start()
    app.run(host='127.0.0.1',port=port, debug=False)
    
    