import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json
import matplotlib as mpl
import seaborn as sns
from matplotlib import font_manager, rc
import glob
# from fbprophet import Prophet

# -*- conding: utf-8 -*-
plt.rcParams['font.family'] = 'Malgun Gothic'
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)


#선영
def hourchart():
    # -*- conding: utf-8 -*-
    hour = pd.read_excel('./datas/monthlytotal_202106Tmoney.xls', sheet_name='지하철 시간대별 이용현황', thousands=',', header=1)
    hour.columns = ['사용월', '호선명', '역ID', '지하철역', '04시승차', '04시하차', '05시승차', '05시하차', '06시승차', '06시하차', '07시승차', '07시하차', '08시승차', '08시하차', '09시승차', '09시하차', '10시승차', '10시하차', '11시승차', '11시하차', '12시승차', '12시하차', '13시승차', '13시하차', '14시승차', '14시하차', '15시승차', '15시하차', '16시승차', '16시하차', '17시승차', '17시하차', '18시승차', '18시하차', '19시승차', '19시하차', '20시승차', '20시하차', '21시승차', '21시하차', '22시승차', '22시하차', '23시승차', '23시하차', '24시승차', '24시하차', '01시승차', '01시하차', '02시승차', '02시하차', '03시승차', '03시하차', '작업일시']
    del hour['작업일시']
    del hour['역ID']
    hour_two = hour[hour['호선명']=='2호선']
    hour_two_on = hour_two[['지하철역','04시승차', '05시승차', '06시승차', '07시승차', '08시승차', '09시승차', '10시승차', '11시승차', '12시승차', '13시승차', '14시승차', '15시승차', '16시승차', '17시승차', '18시승차', '19시승차', '20시승차', '21시승차', '22시승차', '23시승차', '24시승차', '01시승차', '02시승차', '03시승차']]
    
    hour_two_on_change = hour_two_on.transpose()
    hour_two_on_change.columns = hour_two_on_change.iloc[0]
    hour_two_on_change = hour_two_on_change.drop(['지하철역'])
    
    return hour_two_on_change.to_json(orient = 'records', force_ascii=False)

    
def Selectstop(stops):
    hour = pd.read_excel('./datas/monthlytotal_202106Tmoney.xls', sheet_name='지하철 시간대별 이용현황', thousands=',', header=1)
    hour.columns = ['사용월', '호선명', '역ID', '지하철역', '04시승차', '04시하차', '05시승차', '05시하차', '06시승차', '06시하차', '07시승차', '07시하차', '08시승차', '08시하차', '09시승차', '09시하차', '10시승차', '10시하차', '11시승차', '11시하차', '12시승차', '12시하차', '13시승차', '13시하차', '14시승차', '14시하차', '15시승차', '15시하차', '16시승차', '16시하차', '17시승차', '17시하차', '18시승차', '18시하차', '19시승차', '19시하차', '20시승차', '20시하차', '21시승차', '21시하차', '22시승차', '22시하차', '23시승차', '23시하차', '24시승차', '24시하차', '01시승차', '01시하차', '02시승차', '02시하차', '03시승차', '03시하차', '작업일시']
    del hour['작업일시']
    del hour['역ID']
    hour_two = hour[hour['호선명']=='2호선']
    hour_two_on = hour_two[['지하철역','04시승차', '05시승차', '06시승차', '07시승차', '08시승차', '09시승차', '10시승차', '11시승차', '12시승차', '13시승차', '14시승차', '15시승차', '16시승차', '17시승차', '18시승차', '19시승차', '20시승차', '21시승차', '22시승차', '23시승차', '24시승차', '01시승차', '02시승차', '03시승차']]
    hour_two_on_change = hour_two_on.transpose()
    hour_two_on_change.columns = hour_two_on_change.iloc[0]
    hour_two_on_change = hour_two_on_change.drop(['지하철역'])

    hour_two_on_change.plot(y=stops, kind='line', figsize=(15,10), fontsize=18)
    plt.title('202106 시간별 2호선역 승하차객수', fontsize=30)
    plt.savefig('./static/line2chart.png')



#태영
def selectnum(line):
    # -*- conding: utf-8 -*-
    df3 = pd.read_excel('./전처리/dataset/2020년_07월_교통카드_유무임통계자료.xlsx', thousands = ',')
    df3 = df3[['호선명', '지하철역', '유임승차', '유임하차', '무임승차', '무임하차']]
    # 1호선관련
    if line == '1호선':
        #dff1 = df3.loc[df3['호선명'] == '1호선']
        dff1 = df3.loc[df3['호선명'] == line]
        dff11 = dff1.sort_values(by='무임승차', ascending=False)
        dfmean1 = dff1['무임승차'].mean()
        dfmean11 = dff11[(dff11['무임승차'] > dfmean1)]
        dfmean11['지하철역'] = dfmean11['지하철역'].replace(['청량리(서울시립대입구)'],'청량리')
        plt.figure(figsize=(40,30))
        pp1 = sns.catplot(x='지하철역', y='무임승차', data=dfmean11, kind='bar')
        plt.rcParams['lines.linewidth'] = 4
        plt.xticks(rotation=90)
        pp1.savefig("./static/img/output1.jpeg", bbox_inches='tight', pad_inches=0.5)
    

    elif line == '2호선':
        # 2호선
        #dff2 = df3.loc[df3['호선명'] == '2호선']
        dff2 = df3.loc[df3['호선명'] == line]
        dff22 = dff2.sort_values(by='무임승차', ascending=False)
        dfmean2 = dff2['무임승차'].mean()
        dfmean22 = dff22[(dff22['무임승차'] > dfmean2)]
        dfmean22 = dfmean22[(dfmean22['무임승차'] > 100000)]
        dfmean22['지하철역'] = dfmean22['지하철역'].replace(['서울대입구(관악구청)'],'서울대입구')
        dfmean22['지하철역'] = dfmean22['지하철역'].replace(['잠실(송파구청)'],'잠실')
        dfmean22['지하철역'] = dfmean22['지하철역'].replace(['구로디지털단지'],'구로디지털')
        dfmean22['지하철역'] = dfmean22['지하철역'].replace(['교대(법원.검찰청)'],'교대')
        dfmean22['지하철역'] = dfmean22['지하철역'].replace(['대림(구로구청)'],'교대')
        plt.figure(figsize=(38,28))
        pp2 = sns.catplot(x='지하철역', y='무임승차', data=dfmean22, kind='bar')
        plt.rcParams['lines.linewidth'] = 4
        plt.xticks(rotation=90)
        pp2.savefig("./static/img/output1.jpeg", bbox_inches='tight', pad_inches=0.5)


    elif line == '3호선':
        # # 3호선
        #dff3 = df3.loc[df3['호선명'] == '3호선']
        dff3 = df3.loc[df3['호선명'] == line]
        dff33 = dff3.sort_values(by='무임승차', ascending=False)
        dff33 = dff33.query('지하철역 !="충무로"')
        dfmean3 = dff33['무임승차'].mean()
        dfmean33 = dff33[(dff33['무임승차'] > dfmean3)]
        dfmean33['지하철역'] = dfmean33['지하철역'].replace(['양재(서초구청)'],'양재')
        dfmean33['지하철역'] = dfmean33['지하철역'].replace(['남부터미널(예술의전당)'],'남부터미널')
        plt.figure(figsize=(36,26))
        pp3 = sns.catplot(x='지하철역', y='무임승차', data=dfmean33, kind='bar')
        plt.rcParams['lines.linewidth'] = 4
        plt.xticks(rotation=90)
        pp3.savefig("./static/img/output1.jpeg", bbox_inches='tight', pad_inches=0.5)


    elif line == '4호선':
        # # 4호선
        # dff4 = df3.loc[df3['호선명'] == '4호선']
        dff4 = df3.loc[df3['호선명'] == line]
        dfmean4 = dff4['무임승차'].mean()
        dfmean44 = dff4[(dff4['무임승차'] > dfmean4)]
        dfmean44 = dfmean44[(dfmean44['무임승차'] > 100000)]
        dfmean44['지하철역'] = dfmean44['지하철역'].replace(['수유(강북구청)'],'수유')
        dfmean44['지하철역'] = dfmean44['지하철역'].replace(['회현(남대문시장)'],'회현')
        dfmean44['지하철역'] = dfmean44['지하철역'].replace(['총신대입구(이수)'],'총신대입구')
        dfmean44 = dfmean44.sort_values(by='무임승차', ascending=False)
        plt.figure(figsize=(34,24))
        pp4 = sns.catplot(x='지하철역', y='무임승차', data=dfmean44, kind='bar')
        plt.rcParams['lines.linewidth'] = 4
        plt.xticks(rotation=90) 
        pp4.savefig("./static/img/output1.jpeg", bbox_inches='tight', pad_inches=0.5)

    else :
        # 5호선
        # dff5 = df3.loc[df3['호선명'] == '5호선']
        dff5 = df3.loc[df3['호선명'] == line]
        dfmean5 = dff5['무임승차'].mean()
        dfmean55 = dff5[(dff5['무임승차'] > dfmean5)]
        dfmean55 = dfmean55[(dfmean55['무임승차'] > 100000)]
        dfmean55['지하철역'] = dfmean55['지하철역'].replace(['천호(풍납토성)'],'천호')
        dfmean55 = dfmean55.sort_values(by='무임승차', ascending=False)
        plt.figure(figsize=(32,22))
        pp5 = sns.catplot(x='지하철역', y='무임승차', data=dfmean55, kind='bar')
        plt.rcParams['lines.linewidth'] = 4
        plt.xticks(rotation=90) 
        pp5.savefig("./static/img/output1.jpeg", bbox_inches='tight', pad_inches=0.5)




# 유경,재선
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


    #신림역 1년뒤 데이터 예측
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

    # # m = Prophet(yearly_seasonality=True, daily_seasonality=True)
    # m.fit(s1)
    # future=m.make_future_dataframe(periods=366)
    # forecast=m.predict(future)
    
    # m.plot(forecast, xlabel= 'Date', ylabel='passengers')
    # plt.savefig('./static/img/chart02.png')

    # # 노원역 1년뒤 예상 승차승객수 시각화

    # s2 = df.query("노선명 =='4호선' & 역명=='노원'") 

    # del s2["노선명"]
    # del s2["역명"]
    # del s2["하차총승객수"]
    # del s2["등록일자"]

    # s2 = s2.rename(columns={'사용일자':'ds', '승차총승객수':'y'})

    # s2["ds"] = s2["ds"].astype(str)
    # s2["ds"] = pd.to_datetime(s2["ds"])


    # # m = Prophet(yearly_seasonality=True, daily_seasonality=True)
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



# -*- conding: utf-8 -*-
# if __name__=="__main__":
#     # -*- conding: utf-8 -*-
# #     hourchart()
# #     TAE()
# #     Selectstop()
#     selectnum('1호선')




