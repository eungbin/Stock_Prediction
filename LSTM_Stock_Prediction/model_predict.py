import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from keras.models import load_model

csv_data = pd.read_csv('C:/dev/react/stock_predict/LSTM_Stock_Prediction/csv/005930.KS.csv')

high_prices = (csv_data.sort_values(by="Date", ascending=False).head(50))['High'].values
low_prices = (csv_data.sort_values(by="Date", ascending=False).head(50))['Low'].values
mid_prices = (high_prices + low_prices) / 2

seq_len = 49
sequence_length = seq_len + 1

# print(len(mid_prices))
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