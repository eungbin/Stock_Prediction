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

mid_prices = load_db(code)
conn.close()

seq_len = 50
sequence_length = seq_len + 1

print(len(mid_prices))
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
print("result : ", (pred+1)*origin)