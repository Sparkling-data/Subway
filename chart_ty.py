import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json
import matplotlib as mpl
import seaborn as sns
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

# plt.rcParams['font.family'] = 'Malgun Gothic'

# dataframe을 json으로!! :  https://www.delftstack.com/ko/howto/python-pandas/pandas-dataframe-to-json/


def TAE():
    df3 = pd.read_excel('./dataset/dataset/2020년_07월_교통카드_유무임통계자료.xlsx', thousands = ',')
    df3 = df3[['호선명', '지하철역', '유임승차', '유임하차', '무임승차', '무임하차']]
    
    # 각각의 평균값
    linedf = df3['무임승차'].groupby(df3['호선명'])
    linedf_mean = linedf.mean()
    linedf_mean = linedf_mean.astype(int)
    linedf_mean_up = linedf_mean.sort_values(ascending=False)
    linedf_mean_up.head(9)
    
def selectnum(line):
    df3 = pd.read_excel('./전처리/dataset/2020년_07월_교통카드_유무임통계자료.xlsx', thousands = ',')
    df3 = df3[['호선명', '지하철역', '유임승차', '유임하차', '무임승차', '무임하차']]
    # 1호선관련
    #
    if line == '1호선':
        dff1 = df3.loc[df3['호선명'] == line]
        #dff1 = df3.loc[df3['호선명'] == '1호선']
        dff11 = dff1.sort_values(by='무임승차', ascending=False)
        dfmean1 = dff1['무임승차'].mean()
        dfmean11 = dff11[(dff11['무임승차'] > dfmean1)]
        dfmean11['지하철역'] = dfmean11['지하철역'].replace(['청량리(서울시립대입구)'],'청량리')
        plt.figure(figsize=(40,30))
        pp1 = sns.catplot(x='지하철역', y='무임승차', data=dfmean11, kind='bar')
        plt.rcParams['lines.linewidth'] = 4
        plt.xticks(rotation=90)
        pp1.savefig("static/output1.jpeg", bbox_inches='tight', pad_inches=0.5)
    

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
        pp2.savefig("static/output1.jpeg", bbox_inches='tight', pad_inches=0.5)


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
        pp3.savefig("static/output1.jpeg", bbox_inches='tight', pad_inches=0.5)


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
        pp4.savefig("static/output1.jpeg", bbox_inches='tight', pad_inches=0.5)

    else :
        # # 5호선
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
        pp5.savefig("static/output1.jpeg", bbox_inches='tight', pad_inches=0.5)

    # # 1,2,3,4,5 합친것
    # pp10 = pd.concat([dfmean11, dfmean22, dfmean33, dfmean44, dfmean55], axis=0)
    # pp10 = pp10.sort_values(by='무임승차', ascending=False)
    # pp101 = pp10['무임승차'].mean()
    # pp201 = pp10[(pp10['무임승차'] > pp101)]
    # pp201 = pp201.sort_values(by='무임승차', ascending=False)
    # plt.figure(figsize=(15,12))
    # plt.rcParams['lines.linewidth'] = 4
    # plt.xticks(rotation=90)
    # plt.ylim([100000, 300000])
    # pp202 = sns.catplot(x='지하철역', y='무임승차', data=pp201, kind='bar')
    # pp202.figure.savefig("static/output6.jpeg", bbox_inches='tight', pad_inches=0.5)


    # return df3.to_json(orient = 'records', force_ascii=False)
    #print(df3)
    # return df3.to_json(orient = 'records', force_ascii=False)
    #return df3.to_html()
    


# if __name__=="__main__":
#     hourchart()
    # TAE()