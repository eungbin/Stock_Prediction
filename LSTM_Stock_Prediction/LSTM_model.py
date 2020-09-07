import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler

csv_data = pd.read_csv('C:/dev/react/stock_predict/LSTM_Stock_Prediction/csv/005930.KS.csv')

csv_data['Date'] = pd.to_datetime(csv_data['Date'], format='%Y-%m-%d')

plt.figure(figsize=(16, 9))
sns.lineplot(y=csv_data['Average'], x=csv_data['Date'])
plt.xlabel('time')
plt.ylabel('average_price')
plt.show()

scaler = MinMaxScaler()
scale_cols = ['High', 'Low', 'Close', 'Average']

csv_scaled = scaler.fit_transform(csv_data[scale_cols])

csv_scaled = pd.DataFrame(csv_scaled)
csv_scaled.columns = scale_cols

print(csv_scaled)

plt.figure(figsize=(16, 9))
sns.lineplot(y=csv_scaled['Average'], x=csv_data['Date'])
plt.xlabel('time')
plt.ylabel('mean_price')
plt.show()