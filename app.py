from flask import Flask, render_template
import os
app = Flask(__name__, template_folder="/Users/gopaljuneja/Desktop/Assignment5/server/")

HOST = '127.0.0.1'
PORT = int(os.environ.get('PORT', 5000))
DEBUG_MODE = True




@app.route('/ibsHW')
def ibsHW():
    return render_template("ibsHW.html")

if __name__ ==  '__main__':
    app.run(debug=DEBUG_MODE,host=HOST, port=PORT)
