import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# from konlpy.tag import Okt
from keras.preprocessing.text import Tokenizer
from keras.layers import Embedding, Dense, CuDNNLSTM
from keras.models import Sequential
from keras.preprocessing.sequence import pad_sequences
from keras.models import load_model
import pymysql

HOST = '127.0.0.1'
PORT = 3306
USER = 'root'
DB = 'stock_prediction'
PASSWORD = 'vk2sjf12'

conn = pymysql.connect(host=HOST, port=PORT, user=USER, password=PASSWORD, db=DB)

cursor = conn.cursor(pymysql.cursors.DictCursor)


data = pd.read_csv("./title_datas3.csv", encoding='CP949')
print(data.groupby('label').size().reset_index(name='count'))

index_mid = data[data['label'] == -1].index
index_pos = data[data['label'] == 1].index
index_neg = data[data['label'] == 0].index
drop_mid_data = data.drop(index_mid)

df_pos = drop_mid_data.drop(index_neg)
df_neg = drop_mid_data.drop(index_pos)

test_data = []
train_data = []

df_train_pos = df_pos.sample(frac=0.9, random_state=2020)
df_test_pos = df_pos.drop(df_train_pos.index)

df_train_neg = df_neg.sample(frac=0.9, random_state=2020)
df_test_neg = df_neg.drop(df_train_neg.index)

df_train = pd.concat([df_train_pos, df_train_neg])
df_test = pd.concat([df_test_pos, df_test_neg])


df_train = df_train.sample(frac=1)
df_test = df_test.sample(frac=1)

stopwords = ['의', '가', '이', '은', '들', '는', '좀', '잘', '걍', '과', '도', '를', '으로', '자', '에', '와', '한', '하다']

# okt = Okt()
x_train = []
for sentence in df_train['title']:
    # temp_x = []
    # temp_x = okt.morphs(sentence, stem=True)    #토큰화
    # temp_x = [word for word in temp_x if not word in stopwords] #불용어 제거
    # x_train.append(temp_x)
    x_train.append(sentence)

x_test = []
for sentence in df_test['title']:
    # temp_x = []
    # temp_x = okt.morphs(sentence, stem=True)
    # temp_x = [word for word in temp_x if not word in stopwords]
    # x_test.append(temp_x)
    x_test.append(sentence)

print(x_train[:3])
print(x_test[:3])
print(len(x_train))
count = 0

max_word = 60000
tokenizer = Tokenizer(num_words=max_word)
tokenizer.fit_on_texts(x_train)
# for data in x_train:
#     tokenizer.fit_on_texts(data)
#     count += 1
#     print(count)

train_x = []
test_x = []

# x_train = tokenizer.texts_to_sequences(x_train)
# x_test = tokenizer.texts_to_sequences(x_test)
# print(x_train[:3])
#
# print("제목의 최대 길이 : ", max(len(l) for l in x_test))
# print("제목의 평균 길이 : ", sum(map(len, x_test))/ len(x_test))
#
# y_train = []
# y_test = []
#
# for i in range(len(df_train['label'])):
#     if df_train['label'].iloc[i] == 1:
#         y_train.append([0, 1])
#     elif df_train['label'].iloc[i] == 0:
#         y_train.append([1, 0])
# for i in range(len(df_test['label'])):
#     if df_test['label'].iloc[i] == 1:
#         y_test.append([0, 1])
#     elif df_test['label'].iloc[i] == 0:
#         y_test.append([1, 0])
# y_train = np.array(y_train)
# y_test = np.array(y_test)
# print(y_train)
# print(y_test)
#
# max_len = 15
# x_train = pad_sequences(x_train, maxlen=max_len)
# x_test = pad_sequences(x_test, maxlen=max_len)
#
# model = Sequential()
# model.add(Embedding(max_word, 100))
# model.add(CuDNNLSTM(128))
# model.add(Dense(2, activation="softmax"))
#
# model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])
# history = model.fit(x_train, y_train, epochs=10, batch_size=10, validation_split=0.1)
#
# print("테스트 정확도 : {:.2f}%".format(model.evaluate(x_test, y_test)[1]*100))
#
# model.save('./news_model2.h5')

# 실제 뉴스 데이터 불러와서 분석
model = load_model('./news_model2.h5')

# 크롤링한 naver news csv 파일 load
csv_craw_data = pd.read_csv('dataset/naver_news/news.csv', encoding='utf-8-sig')

# pickle file load
load_pickle = pd.read_pickle("../real_data.pickle")
dic_pred_result = {}

# nan 값을 ''[공백]으로 대체
csv_craw_data.fillna('', inplace=True)

# 각 종목의 코드를 이용한 배열 선언 및 뉴스데이터 매치
for stock in load_pickle.values:
    globals()['news_list_{}'.format(stock[1])] = []
    globals()['pred_list_{}'.format(stock[1])] = []
    dic_pred_result[stock[0]+'긍정'] = 0
    dic_pred_result[stock[0]+'부정'] = 0
    for data in csv_craw_data[stock[0]]:
        if data != "":
            globals()['news_list_{}'.format(stock[1])].append(data)

for stock in load_pickle.values:
    for data in globals()['news_list_{}'.format(stock[1])]:
        x_data = []
        for sentence in [data]:
            x_data.append(sentence)

        x_data = np.array(x_data)
        x_data = tokenizer.texts_to_sequences(x_data)

        max_len = 15
        x_data = pad_sequences(x_data, maxlen=max_len)

        pred = model.predict(x_data)
        # print("input data : {0}".format(x_data))
        # print("original data : {0}".format(data))
        # print(pred)

        for list in pred:
            globals()['pred_list_{}'.format(stock[1])].append(list)

    # for result in  globals()['pred_list_{}'.format(stock[1])]:
    #     print("{0}의 결과 : {1}".format(stock[0], result*100))
for stock in load_pickle.values:
    for list in globals()['pred_list_{}'.format(stock[1])]:
        if list[0] > list[1]:
            dic_pred_result[stock[0]+'부정'] += 1
        elif list[0] < list[1]:
            dic_pred_result[stock[0]+'긍정'] += 1

print(dic_pred_result)

for code in load_pickle.values:
    sql = "select exists(select * from news_pred_result where code={0})".format(code[1])
    cursor.execute(sql)
    row = cursor.fetchone()
    indexing_sql = sql[7:]
    if(row[indexing_sql] == 1): #만약 DB에 해당 코드의 예측결과가 존재한다면
        print("{0}의 예측결과가 존재하기 때문에 삭제 후 다시 삽입합니다.".format(code[1]))
        sql = "delete from news_pred_result where code={0}".format(code[1])
        cursor.execute(sql)

    print("{0}의 긍정 결과 : ".format(code[0], dic_pred_result[code[0]+'긍정']))
    print("{0}의 부정 결과 : ".format(code[0], dic_pred_result[code[0]+'부정']))

    if dic_pred_result[code[0]+'긍정'] > dic_pred_result[code[0]+'부정']:
        flag = "긍정"
    elif dic_pred_result[code[0]+'긍정'] < dic_pred_result[code[0]+'부정']:
        flag = "부정"
    else:
        flag = "중립"
    sql = "insert into news_pred_result values(%s, %s)" #종목코드 + 값
    cursor.execute(sql, (code[1], flag))
    print("{0}'s inserting is complete".format(code[1]))

cursor.close()
conn.commit()