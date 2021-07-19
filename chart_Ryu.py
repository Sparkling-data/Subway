# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json
# -*- conding: utf-8 -*-
plt.rcParams['font.family'] = 'Malgun Gothic'

# dataframe을 json으로!! :  https://www.delftstack.com/ko/howto/python-pandas/pandas-dataframe-to-json/


def hourchart():
    # -*- coding: utf-8 -*-

    hour = pd.read_excel('./datas/monthlytotal_202106Tmoney.xls', sheet_name='지하철 시간대별 이용현황', thousands=',', header=1)
    hour.columns = ['사용월', '호선명', '역ID', '지하철역', '04시승차', '04시하차', '05시승차', '05시하차', '06시승차', '06시하차', '07시승차', '07시하차', '08시승차', '08시하차', '09시승차', '09시하차', '10시승차', '10시하차', '11시승차', '11시하차', '12시승차', '12시하차', '13시승차', '13시하차', '14시승차', '14시하차', '15시승차', '15시하차', '16시승차', '16시하차', '17시승차', '17시하차', '18시승차', '18시하차', '19시승차', '19시하차', '20시승차', '20시하차', '21시승차', '21시하차', '22시승차', '22시하차', '23시승차', '23시하차', '24시승차', '24시하차', '01시승차', '01시하차', '02시승차', '02시하차', '03시승차', '03시하차', '작업일시']
    del hour['작업일시']
    del hour['역ID']
    hour_two = hour[hour['호선명']=='2호선']
    hour_two_on = hour_two[['지하철역','04시승차', '05시승차', '06시승차', '07시승차', '08시승차', '09시승차', '10시승차', '11시승차', '12시승차', '13시승차', '14시승차', '15시승차', '16시승차', '17시승차', '18시승차', '19시승차', '20시승차', '21시승차', '22시승차', '23시승차', '24시승차', '01시승차', '02시승차', '03시승차']]
    
    # 행열을 바꾸지 않은 상태로 쓰려면 해야하는 전처리
    # hour_two_on.columns = hour_two_on.iloc[0]
    # hour_two_on = hour_two_on.drop([10])

    # dataframe을 튜플형태로 변환
    # https://pythonq.com/so/python/966583
    # hour_two_on = hour_two_on.apply(tuple, axis=1).tolist()
    # print(hour_two_on)


    
    # 행열을 바꾸어서 쓸경우 해야하는 전처리
    hour_two_on_change = hour_two_on.transpose()
    hour_two_on_change.columns = hour_two_on_change.iloc[0]
    hour_two_on_change = hour_two_on_change.drop(['지하철역'])
    
    # to_html() : dataframe 형태를 html에 그대로 보내줌!!
    # html에서 json.parse를 하면 안됨!!!
    # return hour_two_on_change.to_html()


    # print(hour_two_on_change)
    # print(hour_two_on_change.to_json(orient = 'records', force_ascii=False))
    return hour_two_on_change.to_json(orient = 'records', force_ascii=False)

    # print(hour_two_on.to_json(orient = 'records', force_ascii=False))
    # return hour_two_on.to_json(orient = 'records', force_ascii=False)
    # return json.dumps(hour_two_on)



def TAE():
    df3 = pd.read_excel('./전처리/dataset/2020년_07월_교통카드_유무임통계자료.xlsx', thousands = ',')
    df3 = df3[['호선명', '지하철역', '유임승차', '유임하차', '무임승차', '무임하차']]
    # return df3.to_json(orient = 'records', force_ascii=False)
    print(df3)
    # return df3.to_json(orient = 'records', force_ascii=False)
    return df3.to_html()
    

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
    plt.savefig('./static/img/line2chart.png')
    # return './static/img/line2chart.png'
    # plt.show()


# -*- conding: utf-8 -*-
if __name__=="__main__":
#     hourchart()
#     TAE()
    Selectstop(['방배'])