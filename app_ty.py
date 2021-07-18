
from chart_ty import selectnum
from flask import Flask, render_template, jsonify, request
import json
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from chart_maker import chart_maker

import pandas as pd
import numpy as np

app=Flask(__name__)

@app.route("/", methods=["GET"])
def get():
    return render_template("templates_analytics.html")

@app.route("/mychart", methods=["GET"])
def mychart():
    return render_template("mychart.html")


@app.route("/showchart", methods=["POST"])
def showchart():
    stops = request.form.get('line')
    # 라인에 할당되어있는 값을 가져와줘!
    # 라인 = 1호선, 2호선을 뜻함
    print('ㄱapp구')
    selectnum(stops)
    return 'agaga'

# 주의
# @app.route('/search', methods=['GET', 'POST'])
# def search():

#     driver_path = '/dataset/motive/Data_Study/202105_lab/driver/chromedriver'
#     url = 'https://youtube-rank.com/board/bbs/board.php?bo_table=youtube'

#     # -------------------make crawling object for specific url
#     c = crawler()
#     browser = c.init_crawler(driver_path, url)


#     # ------------------conduct searching using input
#     to_search = request.form.get('input')
#     search_box_Xpath = '//*[@id="list-skin"]/div[1]/ul/li[22]/form/input[2]'

#     c.search(browser, to_search, search_box_Xpath)

#     browser.implicitly_wait(10)

#     # --------------------------------넘어간 페이지에서 html 긁기
#     results = c.crawl_contents(browser)

#     '''
#     1. 리스트를 zip으로 숫자 붙여서 dict, json으로 반환가능
#     2. 또는 results를 DF로 만들어 차트를 뽑고 이미지 저장. -> js 비동기에서 차트 보여주기 가능
#         - 차트 만들기는 또 복잡하니까 따로 함수를 만들자.
#     '''

#     # ---------- chart_maker 객체 생성
#     maker = chart_maker()

#     # --------- 데이터프레임으로 만들기
#     df = maker.make_DF(results)
#     df = maker.groom_data(df)

#     # --------- 차트 만들어서 저장하기
#     maker.make_barchart(df)

#     ## --------- DF -> dict -> json
#     df_json = maker.jsonify(df)

#     time.sleep(3)
#     browser.close()
#     return df_json




if __name__=="__main__":
    app.run(debug=True, host="127.0.0.1", port="5000")