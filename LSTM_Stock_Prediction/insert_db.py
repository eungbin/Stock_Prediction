# 2020년도 3학년 2학기 LINC+ 캡스톤 디자인 프로젝트
# insert_db.py
# csv파일을 이용하여 최신 주가정보를 DB에 저장

import datetime
from pandas_datareader import data
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
now = datetime.datetime.now()
now_str = now.strftime("%Y-%m-%d")

#얘는 어제날짜
yesterday = now + datetime.timedelta(days=-1)
str_yesterday = yesterday.strftime("%Y-%m-%d")
# ----------------------- #


# csv_data = pd.read_csv('C:/dev/react/stock_predict/LSTM_Stock_Prediction/csv/'+now_str+'.csv')

# pickle 이용하여 data.pickle 파일 load #
# load_pickle = pd.read_pickle('./modify-data.pickle')
# ----------------------------------- #

# 실제 사용할 종목 코드 pickle 파일 load #
load_pickle = pd.read_pickle("real_data.pickle")
# ----------------------------------- #

# pickle 데이터를 이용하여 반복하여 테이블 생성 #
# for data in load_pickle.values:
#     csv_data = pd.read_csv('./kospi/' + data[1] + '.csv')
#     sql = "create table `%s`(date date not null primary key, high int(11) not null, low int(11) not null, " \
#           "open int(11) not null, close int(11) not null, volume bigint(11) not null)"%(data[1])
#     cursor.execute(sql)
# ----------------------------------------- #

# csv파일을 이용하여 db에 주가정보[약 700여개 기업] 저장 [초기 실행] #
def init_insert_DB(market):
    file_list = glob.glob('./{}/*.csv'.format(market))
    for file_name in file_list:
        file = pd.read_csv(file_name)
        real_file_name = file_name[8:14]
        print(file_name)
        for date, high, low, open, close, volume in zip(file['Date'], file['High'], file['Low'], file['Open'], file['Close'], file['Volume']):
            integer_high = int(high)
            integer_low = int(low)
            integer_open = int(open)
            integer_close = int(close)
            integer_volume = int(volume)
            convert_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
            sql = "insert into `{0}` values(%s, %s, %s, %s, %s, %s)".format(real_file_name)
            cursor.execute(sql, (convert_date, integer_high, integer_low, integer_open, integer_close, integer_volume))
        print("{0}.csv insert completed!!".format(real_file_name))
# -------------------------------------------------------- #
count = 0
def updateDB(stock_code):
    global count
    sql = "select date from `{0}` order by date desc limit 1".format(stock_code)
    cursor.execute(sql)
    row = cursor.fetchone()
    if row['date'] >= now.date():
        print("이미 최신화되어있는 상태입니다.")
    else:
        next_row = row['date'] + datetime.timedelta(days=1)
        str_row_date = str(next_row)
        update_data = data.get_data_yahoo(stock_code+".ks", str_row_date, now_str)
        print(update_data.index)
        print(update_data['High'].values)
        for date, high, low in zip(update_data.index, update_data['High'], update_data['Low']):
            convert_date = datetime.datetime.strftime(date, "%Y-%m-%d")
            sql = "insert into `{0}` values(%s, %s, %s)".format(stock_code)
            cursor.execute(sql, (convert_date, high, low))
        print("{0}  |  {1} is complete".format(count, stock_code))
        count += 1


# DB에 csv파일을 이용하여 데이터를 insert #
# for date, high, low in zip(csv_data['Date'], csv_data['High'], csv_data['Low']):
#     convert_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
#     sql = "insert into csv values(%s, %s, %s)"
#     cursor.execute(sql, (convert_date, high, low))
# ------------------------------------ #

# init_insert_DB("kospi")

# DB 최신화 [실행할 경우 각 종목별로 주가정보 업데이트] #
for code in load_pickle.values:
    updateDB(code[1])
# # ---------------------------------------------- #

# 주식 종목이 존재하는지 확인 [DB이용] #
# count = 0
# for code in load_pickle.values:
#     sql = "select * from `{0}` order by date desc limit 1".format(code[1])
#     cursor.execute(sql)
#     row = cursor.fetchone()
#     print("{0}  |  {1}  |  {2}".format(count, code[1], row))
#     count += 1
# --------------------------------- #

# pickle 수정하고 저장 #
# modify_pickle = load_pickle.drop([load_pickle.index[739]])
# pd.to_pickle(modify_pickle, './modify-data.pickle')
# ------------------- #

# 실제 사용할 데이터들 pickle파일로 만들기 #
# dict_pickle = [{'kor_name': '삼성전자', 'ticker': '005930'},
#                {'kor_name': 'LG전자', 'ticker': '066570'},
#                {'kor_name': 'SK이노베이션', 'ticker': '096770'},
#                {'kor_name': '기업은행', 'ticker': '024110'},
#                {'kor_name': '기아자동차', 'ticker': '000270'},]
#
# df_pickle = pd.DataFrame(dict_pickle)
# print(df_pickle)
# df_pickle.to_pickle("파일명")
# ------------------------------------- #

# for code in modify_pickle.values:
#     print("{0}  |  {1}".format(code[0], code[1]))
cursor.close()
conn.commit()