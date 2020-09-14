import datetime
import pymysql
import pandas as pd
import numpy as np

HOST = '127.0.0.1'
PORT = 3306
USER = 'root'
DB = 'stock_prediction'
PASSWORD = 'vk2sjf12'

pymysql.converters.encoders[np.int64] = pymysql.converters.escape_float
pymysql.converters.conversions = pymysql.converters.encoders.copy()
pymysql.converters.conversions.update(pymysql.converters.decoders)

conn = pymysql.connect(host=HOST, port=PORT, user=USER, password=PASSWORD, db=DB)

cursor = conn.cursor(pymysql.cursors.DictCursor)

now = datetime.datetime.now()
now_str = now.strftime("%Y-%m-%d")

csv_data = pd.read_csv('C:/dev/react/stock_predict/LSTM_Stock_Prediction/csv/'+now_str+'.csv')

for date, high, low in zip(csv_data['Date'], csv_data['High'], csv_data['Low']):
    convert_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
    sql = "insert into csv values(%s, %s, %s)"
    cursor.execute(sql, (convert_date, high, low))

cursor.close()
conn.commit()