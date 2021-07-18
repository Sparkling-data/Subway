import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import glob
from matplotlib import font_manager, rc
# from fbprophet import Prophet




def chart():

    nyc_subway_data = glob.glob('./전처리/dataset/2020년*')
    # print(nyc_subway_data)



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

    ### 여기까지가 정제


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

    

    sns.catplot(x="사용월", y="평균", data=v3, kind="bar")
    plt.savefig('./static/img/chart01.png')





    # 신림역 1년뒤 데이터 예측
    # nyc_subway_data = glob.glob('./전처리/dataset/c*')

    # subway1 = pd.read_excel(nyc_subway_data[0])
    # subway2 = pd.read_excel(nyc_subway_data[1])
    # subway3 = pd.read_excel(nyc_subway_data[2])
    # subway4 = pd.read_excel(nyc_subway_data[3])
    # subway5 = pd.read_excel(nyc_subway_data[4])
    # subway6 = pd.read_excel(nyc_subway_data[5])
    # subway7 = pd.read_excel(nyc_subway_data[6])
    # subway8 = pd.read_excel(nyc_subway_data[7])
    # subway9 = pd.read_excel(nyc_subway_data[8])
    # subway10 = pd.read_excel(nyc_subway_data[9])
    # subway11 = pd.read_excel(nyc_subway_data[10])
    # subway12 = pd.read_excel(nyc_subway_data[11])

    # df = pd.concat([subway1, subway5, subway6, subway7, subway8, subway9, subway10, subway11, subway12, subway2, subway3, subway4])

    # s1 = df.query("노선명 =='2호선' & 역명=='신림'") 

    # del s1["노선명"]
    # del s1["역명"]
    # del s1["하차총승객수"]
    # del s1["등록일자"]

    # s1 = s1.rename(columns={'사용일자':'ds', '승차총승객수':'y'})

    # s1["ds"] = s1["ds"].astype(str)
    # s1["ds"] = pd.to_datetime(s1["ds"])


    # m = Prophet(yearly_seasonality=True, daily_seasonality=True)
    # m.fit(s1)
    # future=m.make_future_dataframe(periods=366)
    # forecast=m.predict(future)
    
    # m.plot(forecast, xlabel= 'Date', ylabel='passengers')
    # # plt.savefig('./static/img/chart02.png')

    # # 노원역 1년뒤 예상 승차승객수 시각화

    # s2 = df.query("노선명 =='4호선' & 역명=='노원'") 

    # del s2["노선명"]
    # del s2["역명"]
    # del s2["하차총승객수"]
    # del s2["등록일자"]

    # s2 = s2.rename(columns={'사용일자':'ds', '승차총승객수':'y'})

    # s2["ds"] = s2["ds"].astype(str)
    # s2["ds"] = pd.to_datetime(s2["ds"])


    # m = Prophet(yearly_seasonality=True, daily_seasonality=True)
    # m.fit(s2)
    # future=m.make_future_dataframe(periods=366)
    # forecast=m.predict(future)
    
    # m.plot(forecast, xlabel= 'Date', ylabel='passengers')
    # plt.savefig('./static/img/chart03.png')

    # plt.show()



    # 2019년 5월의 첫재주 주말과 평일의 승차승객수 vs 2021 5월 

    # 2021 05 데이터 정제
    df = pd.read_csv("./전처리/dataset/CARD_SUBWAY_MONTH_202105.csv")
    df.reset_index(drop=False, inplace=True)

    df.columns = ["사용일자", "노선명", "역명", "탄사람", "내린사람", "검사일"]
    df.drop(["검사일"], axis=1, inplace=True)

    df['사용일자']= df['사용일자'].astype('str')

    df["사용일자"] = pd.to_datetime(df["사용일자"])

    v1 = df[df["사용일자"].isin(pd.date_range("2021-05-03", "2021-05-07"))]

    # 평일 탄사람의 합,평균을  사람합,사람평균,으로 컬럼 만듬
    v1["사람합"] = v1["탄사람"].sum()
    v1["사람평균"] = v1["탄사람"].mean()
    s1 = v1.head(1)

    #  사람평균의 타입을 int로 변환
    s1["사람평균"] = s1["사람평균"].astype(int)

    # 5/8~5/9일(주말) 데이터
    v2 = df[df["사용일자"].isin(pd.date_range("2021-05-08", "2021-05-09"))]

    # 주말 탄사람의 합,평균을  사람합,사람평균,으로 컬럼 만듬
    v2["사람합"] = v2["탄사람"].sum()
    v2["사람평균"] = v2["탄사람"].mean()
    s2 = v2.head(1)
    s2["사람평균"] = s2["사람평균"].astype(int)

    lee = pd.concat([s1,s2], ignore_index=True)[["사용일자", "사람합", "사람평균"]]
    lee["사용일자"] = lee["사용일자"].astype(str)

    # 사용일자의 value값을 변경

    lee["사용일자"][0] = ("21년5월평일")
    lee["사용일자"][1] = ("21년5월주말")

    lee.rename(columns={"사용일자":"날짜"}, inplace=True)

    # 201905 데이터정제
    df1 = pd.read_csv("./전처리/dataset/CARD_SUBWAY_MONTH_201905.csv", encoding='cp949')

    df1.columns = ["사용일자", "노선명", "역명", "탄사람", "내린사람", "검사일"]

    df1.drop(["검사일"], axis=1, inplace=True)


    # 타입 float에서 int로 변경
    df1["탄사람"] = df1["탄사람"].astype(int)
    df1["내린사람"] = df1["내린사람"].astype(int)

    df1['사용일자']= df1['사용일자'].astype('str')

    df1["사용일자"] = pd.to_datetime(df1["사용일자"])

    # 5월6일부터 5월10일까지(평일)의 데이터만 뽑기
    d1= df1[df1["사용일자"].isin(pd.date_range("2019-05-06", "2019-05-10"))]

    # 평일 탄사람의 합,평균을  사람합,사람평균,으로 컬럼 만듬
    d1["사람합"] = d1["탄사람"].sum()
    d1["사람평균"] = d1["탄사람"].mean()
    s1 = d1.head(1)

    #  사람평균의 타입을 int로 변환
    s1["사람평균"] = s1["사람평균"].astype(int)

    # 5/11~5/12일(주말) 데이터
    d2 = df1[df1["사용일자"].isin(pd.date_range("2019-05-11", "2019-05-12"))]

    # 주말 탄사람의 합,평균을  사람합,사람평균,으로 컬럼 만듬
    d2["사람합"] = d2["탄사람"].sum()
    d2["사람평균"] = d2["탄사람"].mean()
    s2 = d2.head(1)

    #  사람평균 타입을 int로 변환
    s2["사람평균"] = s2["사람평균"].astype(int)

    #  평일과 주말을 merge 사용할 컬럼 : 사용일자, 사람합, 사람평균 
    lee1 = pd.concat([s1,s2], ignore_index=True)[["사용일자", "사람합", "사람평균"]]

    # 사용일자의 value값을 변경
    lee1["사용일자"][0] = ("19년5월평일")
    lee1["사용일자"][1] = ("19년5월주말")

    # 2019년 5월과 2021년 5월  비교 & 시각화
    table = pd.concat([lee,lee1], ignore_index=True)[["날짜", "사람합", "사람평균"]]

    #  2019년5월 평일,주말과 21년 5월 평일,주말 시각화

    sns.catplot(x="날짜", y="사람합", data=table, kind="bar")
    plt.savefig('./static/img/chart04.png')
    
    


chart()