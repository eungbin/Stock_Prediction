import pandas as pd
import konlpy

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

x_train = []
for sentence in df_train['title']:
    x_train.append(sentence)

x_test = []
for sentence in df_test['title']:
    x_test.append(sentence)

okt = konlpy.tag.Okt()
print(okt.pos(u'이 밤 그날의 반딧불을 당신의 창 가까이 보낼게요'))