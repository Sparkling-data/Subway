from flask.json import jsonify
from flask import Flask, render_template, request
from chart import chart
# from myself import js, scrape


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False



#  재선 & 유경
@app.route('/', methods=["GET"])
def basic():


    if request.method =="GET":
        return render_template('main.html')
    
@app.route('/sigak2', methods=['POST'])
def plot2():

  return '{"img01" : "./static/img/chart02.png"}'

@app.route('/sigak1', methods=['POST'])
def plot1():

  return '{"img02" : "./static/img/chart03.png"}'

# -----------------------------

if __name__=="__main__":
    app.run(debug=True, host="127.0.0.1", port="5000")

