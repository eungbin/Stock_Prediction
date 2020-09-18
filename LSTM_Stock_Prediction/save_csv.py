# 2020년도 3학년 2학기 LINC+ 캡스톤 디자인 프로젝트
# save_csv.py
# Yahoo Finance API를 이용하여 최신 주가정보를 가져와, csv파일로 저장

import datetime
from pandas_datareader import data
import pymysql
import numpy as np

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
sql = "select date from csv order by date desc limit 1"
cursor.execute(sql)
row = cursor.fetchone()
cursor.close()
if row['date'] >= now.date():
    print("날짜 같아...")
else :
    next_row = row['date'] + datetime.timedelta(days=1)
    str_row_date = str(next_row)
    print(str_row_date)

    samsung_data = data.get_data_yahoo('005930.KS', str_row_date, now_str)
    samsung_data.to_csv('C:/dev/react/stock_predict/LSTM_Stock_Prediction/csv/'+now_str+'.csv')     # csv파일로 변환하여 저장
#-------------------------#