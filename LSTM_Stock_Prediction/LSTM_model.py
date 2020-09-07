import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

csv_data = pd.read_csv('C:/Users/kim/Desktop/git_folder/LSTM_Stock_Prediction/csv/005930.KS.csv')

csv_data['Date'] = pd.to_datetime(csv_data['Date'], format='%Y-%m-%d')

plt.figure(figsize=(16, 9))
sns.lineplot(y=csv_data['Close'], x=csv_data['Date'])
plt.xlabel('time')
plt.ylabel('price')
plt.show()