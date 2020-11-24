import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import konlpy
from konlpy.tag import Okt
from keras.preprocessing.text import Tokenizer

data = pd.read_csv("./title_datas2.csv", encoding='CP949')
print(data.groupby('label').size().reset_index(name='count'))

index_mid = data[data['label'] == 0].index
index_pos = data[data['label'] == 1].index
index_neg = data[data['label'] == -1].index
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

okt = Okt()
x_train = []
for sentence in df_train['title']:
    temp_x = []
    temp_x = okt.morphs(sentence, stem=True)    #토큰화
    temp_x = [word for word in temp_x if not word in stopwords] #불용어 제거
    x_train.append(temp_x)

x_test = []
for sentence in df_test['title']:
    temp_x = []
    temp_x = okt.morphs(sentence, stem=True)
    temp_x = [word for word in temp_x if not word in stopwords]
    x_test.append(temp_x)

print(x_train[:3])
print(x_test[:3])

max_words = 35000
tokenizer = Tokenizer(num_words=max_words)
tokenizer.fit_on_texts(x_train)
x_train = tokenizer.texts_to_sequences(x_train)
x_test = tokenizer.texts_to_sequences(x_test)

print(x_train)
print(x_test)