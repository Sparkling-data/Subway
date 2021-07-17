import pandas as pd
from selenium import webdriver 
from bs4 import BeautifulSoup 
import time
import pandas as pd
import matplotlib.pyplot as plt
# import seaborn as sns
import json
import glob
from matplotlib import font_manager, rc
import platform
from fbprophet import Prophet




def chart():

    nyc_subway_data = glob.glob('./dataset/2020년*')
    print(nyc_subway_data)



    subway1 = pd.read_excel(nyc_subway_data[0], sheet_name="지하철 노선별 역별 이용현황")
    subway2 = pd.read_excel(nyc_subway_data[1], sheet_name="지하철 노선별 역별 이용현황")
    subway3 = pd.read_excel(nyc_subway_data[2], sheet_name="지하철 노선별 역별 이용현황")
    subway4 = pd.read_excel(nyc_subway_data[3], sheet_name="지하철 노선별 역별 이용현황")
    subway5 = pd.read_excel(nyc_subway_data[4], sheet_name="지하철 노선별 역별 이용현황")
    subway6 = pd.read_excel(nyc_subway_data[5], sheet_name="지하철 노선별 역별 이용현황")
    subway7 = pd.read_excel(nyc_subway_data[6], sheet_name="지하철 노선별 역별 이용현황")
    subway8 = pd.read_excel(nyc_subway_data[7], sheet_name="지하철 노선별 역별 이용현황")
    subway9 = pd.read_excel(nyc_subway_data[8], sheet_name="지하철 노선별 역별 이용현황")
    subway10 = pd.read_excel(nyc_subway_data[9], sheet_name="지하철 노선별 역별 이용현황")
    subway11 = pd.read_excel(nyc_subway_data[10], sheet_name="지하철 노선별 역별 이용현황")
    subway12 = pd.read_excel(nyc_subway_data[11], sheet_name="지하철 노선별 역별 이용현황")

    df4 = pd.concat([subway1, subway2, subway3, subway4, subway5, subway6, subway7, subway8, subway9, subway10, subway11, subway12])


    df4["승차승객수"] = df4["승차승객수"].apply(lambda x: x.replace(',', ''))
    df4["하차승객수"] = df4["하차승객수"].apply(lambda x: x.replace(',', ''))
    df4["승차승객수"] = df4["승차승객수"].astype(int)
    df4["하차승객수"] = df4["하차승객수"].astype(int)
    del df4["작업일시"]
    del df4["역ID"]


    df4 = df4[df4.호선명 != "9호선2~3단계"]
    df4 = df4[df4.호선명 != "공항철도 1호선"]
    df4 = df4[df4.호선명 != "9호선"]
    df4 = df4[df4.호선명 != "8호선"]
    df4 = df4[df4.호선명 != "7호선"]
    df4 = df4[df4.호선명 != "6호선"]
    df4 = df4[df4.호선명 != "경강선"]
    df4 = df4[df4.호선명 != "수인선"]
    df4 = df4[df4.호선명 != "경춘선"]
    df4 = df4[df4.호선명 != "경의선"]
    df4 = df4[df4.호선명 != "장항선"]
    df4 = df4[df4.호선명 != "중앙선"]
    df4 = df4[df4.호선명 != "일산선"]
    df4 = df4[df4.호선명 != "분당선"]
    df4 = df4[df4.호선명 != "과천선"]
    df4 = df4[df4.호선명 != "안산선"]
    df4 = df4[df4.호선명 != "경원선"]
    df4 = df4[df4.호선명 != "경인선"]
    df4 = df4[df4.호선명 != "경부선"]
    df4 = df4[df4.호선명 != "우이신설선"]


    v1 = df4.query("사용월 == '2020-11'") 
    v2 = df4.query("사용월 == '2020-12'")

    v1["평균"] = v1["승차승객수"].mean()
    v1["평균"] = v1["평균"].astype('int')

    del v1["호선명"]
    del v1["지하철역"]
    del v1["승차승객수"]
    del v1["하차승객수"]

    v1 = v1.head(1)


    v2["평균"] = v2["승차승객수"].mean()
    v2["평균"] = v2["평균"].astype('int')

    del v2["호선명"]
    del v2["지하철역"]
    del v2["승차승객수"]
    del v2["하차승객수"]
    v2 = v2.head(1)

    v3 = pd.concat([v1,v2], ignore_index=True)

    v3["사용월"][0] = ("2020년11월")
    v3["사용월"][1] = ("2020년12월")

    # sns.catplot(x="사용월", y="평균", data=v3, kind="bar")
    # plt.savefig('./static/images/chart01.png')



    # 1년뒤 데이터 예측


    nyc_subway_data = glob.glob('./dataset/c*')

    subway1 = pd.read_excel(nyc_subway_data[0])
    subway2 = pd.read_excel(nyc_subway_data[1])
    subway3 = pd.read_excel(nyc_subway_data[2])
    subway4 = pd.read_excel(nyc_subway_data[3])
    subway5 = pd.read_excel(nyc_subway_data[4])
    subway6 = pd.read_excel(nyc_subway_data[5])
    subway7 = pd.read_excel(nyc_subway_data[6])
    subway8 = pd.read_excel(nyc_subway_data[7])
    subway9 = pd.read_excel(nyc_subway_data[8])
    subway10 = pd.read_excel(nyc_subway_data[9])
    subway11 = pd.read_excel(nyc_subway_data[10])
    subway12 = pd.read_excel(nyc_subway_data[11])

    df = pd.concat([subway1, subway5, subway6, subway7, subway8, subway9, subway10, subway11, subway12, subway2, subway3, subway4])

    s1 = df.query("노선명 =='2호선' & 역명=='시청'") 

    del s1["노선명"]
    del s1["역명"]
    del s1["하차총승객수"]
    del s1["등록일자"]

    s1 = s1.rename(columns={'사용일자':'ds', '승차총승객수':'y'})

    s1["ds"] = s1["ds"].astype(str)
    s1["ds"] = pd.to_datetime(s1["ds"])


    m = Prophet()
    m.fit(s1)
    future=m.make_future_dataframe(periods=366)
    forecast=m.predict(future)
    # print(forecast)
    
    m.plot(forecast, xlabel= 'Date', ylabel='passengers')
    # plt.savefig('./static/images/chart02.png')

    # plt.show()
chart()