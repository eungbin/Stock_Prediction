import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import LSTM, Dropout, Dense, Activation
# from keras.callbacks import TensorBoard, ModelCheckpoint, ReduceLROnPlateau
import datetime
from keras.models import load_model
import pymysql
from urllib.request import urlopen
from yahoo_finance import Share
from pandas_datareader import data

HOST = '127.0.0.1'
PORT = 3306
USER = 'root'
DB = 'stock_prediction'
PASSWORD = 'vk2sjf12'

pymysql.converters.encoders[np.int64] = pymysql.converters.escape_float
pymysql.converters.conversions = pymysql.converters.encoders.copy()
pymysql.converters.conversions.update(pymysql.converters.decoders)

conn = pymysql.connect(host=HOST, port=PORT, user=USER, password=PASSWORD, db=DB)

csv_data = pd.read_csv('C:/dev/react/stock_predict/LSTM_Stock_Prediction/csv/005930.KS.csv')

cursor = conn.cursor(pymysql.cursors.DictCursor)


#--- yahoo finance API ---#
samsung_data = data.DataReader('005930.KS', 'yahoo', '2020-09-01', '2020-09-14')
print(samsung_data)
#-------------------------#


#--- CSV파일 DB저장 ---#
# for date, high, low in zip(csv_data['Date'], csv_data['High'], csv_data['Low']):
#     convert_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
#     sql = "insert into csv values(%s, %s, %s)"
#     cursor.execute(sql, (convert_date, high, low))
#
# conn.commit()
#---------------------#

#--- DB에서 주가정보 불러오기 ---#
# sql = "select high, low from csv"
# cursor.execute(sql)
#
# rows = cursor.fetchall()
# mid_prices = []
# for i in rows:
#     mid_prices.append( (i['low'] + i['high'])/2 )
#
# conn.close()
#------------------------------#

# high_prices = csv_data['High'].values
# low_prices = csv_data['Low'].values
# mid_prices = (high_prices + low_prices) / 2

# seq_len = 50
# sequence_length = seq_len + 1
#
# result = []
# for index in range(len(mid_prices) - sequence_length):
#     result.append(mid_prices[index: index + sequence_length])
#
#
# normalized_data = []
# for window in result:
#     normalized_window = [((float(p) / float(window[0])) - 1) for p in window]
#     normalized_data.append(normalized_window)
#
# result = np.array(normalized_data)
#
# row = int(round(result.shape[0] * 0.9))
# train = result[:row, :]
# np.random.shuffle(train)
#
# x_train = train[:, :-1]
# x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
# y_train = train[:, -1]
#
# x_test = result[row:, :-1]
# x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))
# y_test = result[row:, -1]
#
# model = Sequential()
# model.add(LSTM(50, return_sequences=True, input_shape=(50, 1)))
# model.add(LSTM(64, return_sequences=False))
# model.add(Dense(1, activation='linear'))
# model.compile(loss='mse', optimizer='rmsprop')
# model.summary()
#
# model.fit(x_train, y_train,
#           validation_data=(x_test, y_test),
#           batch_size=10,
#           epochs=20)
#
# model.save('stock_predict_test.h5')