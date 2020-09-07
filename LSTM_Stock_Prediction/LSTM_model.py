import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
import numpy as np
from sklearn.model_selection import train_test_split

from keras.models import Sequential
from keras.layers import Dense
from keras.callbacks import EarlyStopping, ModelCheckpoint
from keras.layers import LSTM

import os

csv_data = pd.read_csv('C:/dev/react/stock_predict/LSTM_Stock_Prediction/csv/005930.KS.csv')

csv_data['Date'] = pd.to_datetime(csv_data['Date'], format='%Y-%m-%d')

# plt.figure(figsize=(16, 9))
# sns.lineplot(y=csv_data['Average'], x=csv_data['Date'])
# plt.xlabel('time')
# plt.ylabel('average_price')
# plt.show()

scaler = MinMaxScaler()
scale_cols = ['High', 'Low', 'Close', 'Average']

csv_scaled = scaler.fit_transform(csv_data[scale_cols])

csv_scaled = pd.DataFrame(csv_scaled)
csv_scaled.columns = scale_cols

# plt.figure(figsize=(16, 9))
# sns.lineplot(y=csv_scaled['Average'], x=csv_data['Date'])
# plt.xlabel('time')
# plt.ylabel('mean_price')
# plt.show()

TEST_SIZE = 200

train = csv_scaled[:-TEST_SIZE]
test = csv_scaled[-TEST_SIZE:]

print(csv_scaled.shape)
print(train.shape)
print(test.shape)

def make_dataset(data, label, window_size=20):
    feature_list = []
    label_list = []
    for i in range(len(data) - window_size):
        feature_list.append(np.array(data.iloc[i:i+window_size]))
        label_list.append(np.array(label.iloc[i+window_size]))
    return np.array(feature_list), np.array(label_list)

feature_cols = ['High', 'Low', 'Close']
label_cols = ['Average']

train_feature = train[feature_cols]
train_label = train[label_cols]

train_feature, train_label = make_dataset(train_feature, train_label, 20)

x_train, x_valid, y_train, y_valid = train_test_split(train_feature, train_label, test_size=0.2)

print('x_train.shape : {0}'.format(x_train.shape))
print('x_valid.shape : {0}'.format(x_valid.shape))

test_feature = test[feature_cols]
test_label = test[label_cols]

test_feature, test_label = make_dataset(test_feature, test_label, 20)
print('test_feature.shape : {0}'.format(test_feature.shape))
print('test_label.shape : {0}'.format(test_label.shape))

model = Sequential()
model.add(LSTM(16,
               input_shape=(train_feature.shape[1], train_feature.shape[2]),
               activation='relu',
               return_sequences=False)
          )
model.add(Dense(1))

model_path = 'C:/dev/react/stock_predict/LSTM_Stock_Prediction/'
model.compile(loss='mean_squared_error', optimizer='adam')
early_stop = EarlyStopping(monitor='val_loss', patience=5)
filename = os.path.join(model_path, 'tmp_checkpoint.h5')
checkpoint = ModelCheckpoint(filename, monitor='val_loss', verbose=1, save_best_only=True, mode='auto')

# history = model.fit(x_train, y_train,
#                     epochs=200,
#                     batch_size=16,
#                     validation_data=(x_valid, y_valid),
#                     callbacks=[early_stop, checkpoint])

model.load_weights(filename)
pred = model.predict(test_feature)

plt.figure(figsize=(12, 9))
plt.plot(test_label, label='actual')
plt.plot(pred, label='prediction')
plt.legend()
plt.show()
