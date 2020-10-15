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
    sql = "select close from `{0}` order by date desc limit 50".format(code)
    cursor.execute(sql)

    rows = cursor.fetchall()
    close_prices = []
    for i in rows:
        close_prices.append( i['close'] )
    return close_prices
#------------------------------#

# 여기서 종목코드 지정해주면 됨 #
code = "005930"
# -------------------------- #
# 모델 예측 함수 #
def model_predict(code):
    close_prices = load_db(code)

    seq_len = 50
    sequence_length = seq_len + 1

    # print(len(mid_prices))
    result = []

    for i in close_prices:
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
    # model.summary()
    pred = model.predict(x_test)
    # print(pred)
    pred_result = (pred+1)*origin
    print("{0}'s result : ".format(code), pred_result)
    return pred_result
# ------------ #

# 예측 결과를 DB에 저장해주는 함수 #
def insert_db(dict_result, code_list):
    for code, result in zip(code_list, dict_result):
        print("code:{0} || price:{1}".format(code[1], str(dict_result[code[1]])))
        sql = "select exists(select * from pred_result where code={0})".format(code[1])
        cursor.execute(sql)
        row = cursor.fetchone()
        indexing_sql = sql[7:]  # exists(select * from `005930` where date = '2020-09-07')
        if(row[indexing_sql] == 1): #만약 DB에 해당 코드의 예측결과가 존재한다면
            print("{0}의 예측결과가 존재하기 때문에 삭제 후 다시 삽입합니다.".format(code[1]))
            sql = "delete from pred_result where code={0}".format(code[1])
            cursor.execute(sql)

        sql = "insert into pred_result values(%s, %s)" #아마 주식코드 + 값
        cursor.execute(sql, (code[1], dict_result[code[1]]))
        print("{0}'s inserting is complete".format(code[1]))

arr_result = []

# 예측 함수를 실행하여 배열에 결과 저장 #
for code in load_pickle.values:
    arr_result.append(int(model_predict(code[1])[0][0]))
# --------------------------------- #
print("Predict Result")
# 예측결과를 종목코드와 쌍으로 딕셔너리 생성 #
dict_result = {}
for data, code in  zip(arr_result, load_pickle.values):
    dict_result[code[1]] = data

print(dict_result)

insert_db(dict_result, load_pickle.values)

# sql = "select exists(select * from `{0}`)".format(code)
# cursor.execute(sql)
#
# row = cursor.fetchone()
# indexing_sql = sql[7:]      # exists(select * from `005930` where date = '2020-09-07')
# print("result : " + str(row[indexing_sql]))
# print(indexing_sql)

cursor.close()
conn.commit()