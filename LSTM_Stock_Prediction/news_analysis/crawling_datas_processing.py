import pandas as pd
from keras.models import load_model
import numpy as np
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences

# 크롤링한 naver news csv 파일 load
csv_craw_data = pd.read_csv('dataset/naver_news/news.csv', encoding='utf-8-sig')

# pickle file load
load_pickle = pd.read_pickle("../real_data.pickle")

# nan 값을 ''[공백]으로 대체
csv_craw_data.fillna('', inplace=True)

# 각 종목의 코드를 이용한 배열 선언 및 뉴스데이터 매치
for stock in load_pickle.values:
    globals()['news_list_{}'.format(stock[1])] = []
    for data in csv_craw_data[stock[0]]:
        if data != "":
            globals()['news_list_{}'.format(stock[1])].append(data)

for stock in load_pickle.values:
    for data in globals()['news_list_{}'.format(stock[1])]:
        print("{0}'s data : {1}".format(stock[0], data))

model = load_model('./news_model2.h5')
model.summary()

data = ["삼성전자 주가 상승"]
x_data = []

for sentence in data:
    x_data.append(sentence)

x_data = np.array(x_data)
x_data = tokenizer.texts_to_sequences(x_data)

max_len = 15
x_data = pad_sequences(x_data, maxlen=max_len)

pred = model.predict(x_data)
print("input data : {0}".format(x_data))
print("original data : {0}".format(data))
print(pred)

pred_result = []

for list in pred:
    for data in list:
        pred_result.append(data)

for data in pred_result:
    print(data*100)