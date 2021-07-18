from chart_ty import selectnum
from flask import Flask, render_template, jsonify, request
import json
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from chart_maker import chart_maker
from flask.json import jsonify
from flask import Flask, render_template, request
from flask import Flask, request, render_template
from chart_Ryu import hourchart

import pandas as pd
import numpy as np

app=Flask(__name__)
app.config['JSON_AS_ASCII'] = False


# 선영
@app.route("/", methods=["GET"])
def get():
    return render_template("templates_analytics.html")

@app.route("/mychart", methods=["GET"])
def mychart():
    return render_template("mychart_Ryu.html")


@app.route("/showchart", methods=["GET"])
def showchart():
    return hourchart()

@app.route("/selectstop", methods=["POST"])
def selectstop():
    stops = request.form.get('stoplist')
    stops = stops.split(',')
    print(stops)
    return '가즈아'



#태영

@app.route("/mychart_park", methods=["GET"])
def mychart_park():
    return render_template("mychart_park.html")


@app.route("/showchart9", methods=["POST"])
def showchart9():
    stops = request.form.get('line')
    selectnum(stops)
    


# 재선&유경
@app.route('/', methods=["GET"])
def basic():
    if request.method =="GET":
        return render_template('mychart_JU.html')
    
@app.route('/sigak2', methods=['POST'])
def plot2():

  return '{"img01" : "./static/img/chart02.png"}'

@app.route('/sigak1', methods=['POST'])
def plot1():

  return '{"img02" : "./static/img/chart03.png"}'

@app.route('/sigak3', methods=['POST'])
def plot3():

  return '{"img03" : "./static/img/chart01.png"}'


@app.route('/sigak4', methods=['POST'])
def plot4():

  return '{"img04" : "./static/img/chart04.png"}'









if __name__=="__main__":
    app.run(debug=True, host="127.0.0.1", port="5000")