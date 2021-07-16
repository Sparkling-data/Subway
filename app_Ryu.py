from flask import Flask, request, render_template
from chart_Ryu import hourchart, TAE

app=Flask(__name__)

@app.route("/", methods=["GET"])
def get():
    return render_template("templates_analytics.html")

@app.route("/mychart", methods=["GET"])
def mychart():
    return render_template("mychart.html")


@app.route("/showchart", methods=["GET"])
def showchart():
    
    return TAE()




if __name__=="__main__":
    app.run(debug=True, host="127.0.0.1", port="5000")