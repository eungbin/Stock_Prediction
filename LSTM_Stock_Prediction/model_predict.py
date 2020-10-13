# 2020년도 3학년 2학기 LINC+ 캡스톤 디자인 프로젝트
# model_predict.py
# 최근 50일동안의 주가정보를 이용하여 다음 날 주가 예측

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from keras.models import load_model
import pymysql

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

load_pickle = pd.read_pickle("real_data.pickle")

#--- DB에서 주가정보 불러오기 ---#
def load_db(code):
    sql = "select high, low from `{0}` order by date desc limit 50".format(code)
    cursor.execute(sql)

    rows = cursor.fetchall()
    mid_prices = []
    for i in rows:
        mid_prices.append( (i['low'] + i['high'])/2 )
    return mid_prices
#------------------------------#

# 여기서 종목코드 지정해주면 됨 #
code = "005930"
# -------------------------- #
# 모델 예측 함수 #
def model_predict(code):
    mid_prices = load_db(code)

    seq_len = 50
    sequence_length = seq_len + 1

    # print(len(mid_prices))
    result = []

    for i in mid_prices:
        result.append(i)

    result.reverse()

    origin = result[0]

    normalized_data = []
    for window in result:
        normalized_window = [(float(window) / float(result[0]) - 1)]
        normalized_data.append(normalized_window)

    result = np.array(normalized_data)

    x_test = result[:]
    x_test = np.reshape(x_test, (1, x_test.shape[0], 1))

    model = load_model('./models/{0}.h5'.format(code))
    model.summary()
    pred = model.predict(x_test)
    print(pred)
    pred_result = (pred+1)*origin
    print("{0}'s result : ".format(code), pred_result)
    return pred_result
# ------------ #

# 예측 결과를 DB에 저장해주는 함수 #
def insert_db(dict_result, code_list):
    for code, result in zip(code_list, dict_result):
        sql = "insert into pred_result values(%s, %s)" #아마 주식코드 + 값
        cursor.execute(sql, (code[1], dict_result[result]))

arr_result = []

# 예측 함수를 실행하여 배열에 결과 저장 #
# for code in load_pickle.values:
#     arr_result.append(int(model_predict(code[1])[0][0]))
# --------------------------------- #
print("Predict Result")
# 예측결과를 종목코드와 쌍으로 딕셔너리 생성 #
# dict_result = {}
# for data, code in  zip(arr_result, load_pickle.values):
#     dict_result[code[1]] = data
#
# for test in dict_result:
#     print(dict_result[test])

sql = "select exists(select * from `{0}` where date = '2020-09-07')".format(code)
cursor.execute(sql)

row = cursor.fetchone()
print(row)
indexing_sql = sql[14:-1]   # select * from `005930` where date = '2020-09-07'
print(indexing_sql)

conn.close()