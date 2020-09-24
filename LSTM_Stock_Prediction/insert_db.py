# 2020년도 3학년 2학기 LINC+ 캡스톤 디자인 프로젝트
# insert_db.py
# csv파일을 이용하여 최신 주가정보를 DB에 저장

import datetime
import pymysql
import pandas as pd
import numpy as np
import pickle
import glob

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

# 오늘 날짜 문자열로 치환 #
# now = datetime.datetime.now()
# now_str = now.strftime("%Y-%m-%d")
# ----------------------- #


# csv_data = pd.read_csv('C:/dev/react/stock_predict/LSTM_Stock_Prediction/csv/'+now_str+'.csv')

# pickle 이용하여 data.pickle 파일 load #
load_pickle = pd.read_pickle('./data.pickle')
# ----------------------------------- #

# pickle 데이터를 이용하여 반복하여 테이블 생성 #
# for data in load_pickle.values:
#     csv_data = pd.read_csv('./kospi/' + data[1] + '.csv')
#     sql = "create table `%s`(date date not null primary key, high int(11) not null, low int(11) not null)"%(data[1])
#     cursor.execute(sql)
# ----------------------------------------- #

def insert_DB(market):
    file_list = glob.glob('./{}/*.csv'.format(market))
    for file_name in file_list:
        file = pd.read_csv(file_name)
        real_file_name = file_name[8:14]
        for date, high, low in zip(file['Date'], file['High'], file['Low']):
            integer_high = int(high)
            integer_low = int(low)
            str_high = str(integer_high)
            str_low = str(integer_low)
            convert_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
            sql = "insert into `{0}` values(%s, %s, %s)".format(real_file_name)
            cursor.execute(sql, (convert_date, integer_high, integer_low))
        print("{0}.csv insert completed!!".format(real_file_name))


# DB에 csv파일을 이용하여 데이터를 insert #
# for date, high, low in zip(csv_data['Date'], csv_data['High'], csv_data['Low']):
#     convert_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
#     sql = "insert into csv values(%s, %s, %s)"
#     cursor.execute(sql, (convert_date, high, low))
# ------------------------------------ #

insert_DB("kospi")
cursor.close()
conn.commit()