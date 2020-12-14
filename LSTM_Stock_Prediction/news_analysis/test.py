import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# from konlpy.tag import Okt
from keras.preprocessing.text import Tokenizer
from keras.layers import Embedding, Dense, CuDNNLSTM
from keras.models import Sequential
from keras.preprocessing.sequence import pad_sequences
from keras.models import load_model


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