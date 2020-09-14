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

#--- DB에서 주가정보 불러오기 ---#
sql = "select high, low from csv order by date desc limit 50"
cursor.execute(sql)

rows = cursor.fetchall()
mid_prices = []
for i in rows:
    mid_prices.append( (i['low'] + i['high'])/2 )

print(mid_prices)
conn.close()
#------------------------------#

seq_len = 49
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

model = load_model('C:/dev/react/stock_predict/LSTM_Stock_Prediction/models/stock_predict.h5')
model.summary()
pred = model.predict(x_test)
print(pred)
print("result : ", (pred+1)*origin)