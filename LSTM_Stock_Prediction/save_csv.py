# 2020년도 3학년 2학기 LINC+ 캡스톤 디자인 프로젝트
# save_csv.py
# Yahoo Finance API를 이용하여 최신 주가정보를 가져와, csv파일로 저장

import datetime
from pandas_datareader import data
import pymysql
import numpy as np
import pandas as pd
import glob
import re
import pickle

HOST = '127.0.0.1'
PORT = 3306
USER = 'root'
DB = 'stock_prediction'
PASSWORD = 'vk2sjf12'

pymysql.converters.encoders[np.int64] = pymysql.converters.escape_float
pymysql.converters.conversions = pymysql.converters.encoders.copy()
pymysql.converters.conversions.update(pymysql.converters.decoders)

conn = pymysql.connect(host=HOST, port=PORT, user=USER, password=PASSWORD, db=DB)

cursor = conn.cursor(pymysql.cursors.DictCursor)

now = datetime.datetime.now()
now_str = now.strftime("%Y-%m-%d")

#--- yahoo finance API ---#
# 이미 사용하고 있는 주식코드인 경우 #
# sql = "select date from csv order by date desc limit 1"
# cursor.execute(sql)
# row = cursor.fetchone()
# cursor.close()
# if row['date'] >= now.date():
#     print("날짜 같아...")
# else :
#     next_row = row['date'] + datetime.timedelta(days=1)
#     str_row_date = str(next_row)
#     print(str_row_date)
#
#     samsung_data = data.get_data_yahoo('005930.KS', str_row_date, now_str)
#     samsung_data.to_csv('C:/dev/react/stock_predict/LSTM_Stock_Prediction/csv/'+now_str+'.csv')     # csv파일로 변환하여 저장
#-------------------------#

# 처음 사용하는 주식코드일 경우 #
# start_date = '1996-05-06'
kospi = pd.read_pickle('./kospi.pickle')
#
# kospi_array = []
# kospi_array_0, kospi_array_1, kospi_array_2, kospi_array_3, kospi_array_4, kospi_array_5, kospi_array_6, kospi_array_7 = [], [], [], [], [], [], [], []
# loop_num = 0
#
# for i in kospi.values:
#     kospi_array.append(i)
#
# for i in kospi_array:
#     loop_num += 1
#     if loop_num <= 100:
#         kospi_array_0.append(i)
#     elif loop_num <= 200:
#         kospi_array_1.append(i)
#     elif loop_num <= 300:
#         kospi_array_2.append(i)
#     elif loop_num <= 400:
#         kospi_array_3.append(i)
#     elif loop_num <= 500:
#         kospi_array_4.append(i)
#     elif loop_num <= 600:
#         kospi_array_5.append(i)
#     elif loop_num <= 700:
#         kospi_array_6.append(i)
#     else:
#         kospi_array_7.append(i)
#
#
#
kospi_2 = kospi.drop([kospi.index[49], kospi.index[88], kospi.index[153], kospi.index[227], kospi.index[239], kospi.index[345],
                      kospi.index[582], kospi.index[597], kospi.index[622], kospi.index[637], kospi.index[721], ])

# pd.to_pickle(kospi_2, './data.pickle')    # pickle파일로 변환

kospi_3 = pd.read_pickle('./data.pickle')
print(kospi_3)

# del kospi_array_0[49]
# del kospi_array_0[87]   #98개
# del kospi_array_1[53]   #99개
# del kospi_array_2[27]
# del kospi_array_2[38]   #98개
# del kospi_array_3[45]   #99개
# del kospi_array_5[82]
# del kospi_array_5[96]   #98개
# del kospi_array_6[22]
# del kospi_array_6[36]   #98개
# del kospi_array_7[21]
#
#
# def save_kospi():
#     for stock in kospi_array_7:
#         kor_name = stock[0]
#         ticker = stock[1]
#         df = data.get_data_yahoo(ticker + '.KS', start_date, now_str)
#         df.to_csv('./kospi/{}.csv'.format(ticker))
#         print('{}.csv is saved'.format(ticker))
#
# save_kospi()
#
# def reload_empty(market):
#     file_list = glob.glob('./{}/*.csv'.format(market))
#     six_digit = re.compile('\d{6}')
#     for file_name in file_list:
#         file = pd.read_csv(file_name)
#         if file.empty:
#             print("empty file {} is updated".format(file_name))
#             ticker = six_digit.findall(file_name)[0]
#             tmp_df = data.get_data_yahoo(ticker+'.KS', start_date, now_str)
#             tmp_df.to_csv(file_name)
#
# reload_empty('kospi')