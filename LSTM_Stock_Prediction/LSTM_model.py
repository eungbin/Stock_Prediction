# 2020년도 3학년 2학기 LINC+ 캡스톤 디자인 프로젝트
# LSTM_model.py
# LSTM 모델 작성, 훈련

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import LSTM, Dropout, Dense, Activation, CuDNNLSTM
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

# csv_data = pd.read_csv('C:/dev/react/stock_predict/LSTM_Stock_Prediction/csv/005930.KS.csv')
load_pickle = pd.read_pickle("real_data.pickle")

cursor = conn.cursor(pymysql.cursors.DictCursor)

# --- DB에서 주가정보 불러오기 ---#
def load_db(code):
    sql = "select close from `{0}`".format(code)
    cursor.execute(sql)

    rows = cursor.fetchall()
    close_prices = []
    for i in rows:
        close_prices.append(i['close'])
    return close_prices
# ------------------------------#

# 배열에 모두저장 #
close_prices = []
for code in load_pickle.values:
    close_prices.append(load_db(code[1]))
# ------------- #

conn.close()

def model_create_and_run(code, price): #모델 정의, 데이터 전처리, 훈련
    seq_len = 50
    sequence_length = seq_len + 1

    result = []
    for index in range(len(price) - sequence_length):
        result.append(price[index: index + sequence_length])

    # 데이터 정규화
    normalized_data = []
    for window in result:
        normalized_window = [((float(p) / float(window[0])) - 1) for p in window]
        normalized_data.append(normalized_window)

    result = np.array(normalized_data)

    # train데이터와 test데이터 나누는 과정
    row = int(round(result.shape[0] * 0.9))
    train = result[:row, :]
    np.random.shuffle(train)

    x_train = train[:, :-1]
    x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
    y_train = train[:, -1]

    x_test = result[row:, :-1]
    x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))
    y_test = result[row:, -1]

    # LSTM 모델 설계
    model = Sequential()
    model.add(CuDNNLSTM(50, return_sequences=True, input_shape=(50, 1)))
    model.add(CuDNNLSTM(64, return_sequences=False))
    model.add(Dense(1, activation='linear'))
    model.compile(loss='mse', optimizer='rmsprop')
    model.summary()

    # 모델 훈련
    model.fit(x_train, y_train,
              validation_data=(x_test, y_test),
              batch_size=10,
              epochs=20)

    # 가중치파일 저장
    model.save('./models/{0}.h5'.format(code))

# 5개 종목에 대한 모델 훈련 반복문
for code, price in zip(load_pickle.values, close_prices):
    model_create_and_run(code[1], price)