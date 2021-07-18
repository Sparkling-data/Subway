from flask.json import jsonify
from flask import Flask, render_template, request
from chart import chart
# from myself import js, scrape

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/', methods=["GET"])
def basic():


    if request.method =="GET":
        return render_template('main.html')
    
@app.route('/sigak', methods=['POST'])
def plot():

  return '{"img01" : "./static/images/chart02.png"}'



if __name__=="__main__":
    app.run(debug=True, host="127.0.0.1", port="5000")

