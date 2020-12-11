from keras.models import load_model
from konlpy.tag import Okt
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
import numpy as np

model = load_model('./news_model.h5')

data = ["몰라 몰라용"]
x_data = []

for sentence in data:
    x_data.append(sentence)

x_data = np.array(x_data)

pred = model.predict(x_data)
print(pred)

pred_result = []

for list in pred:
    for data in list:
        pred_result.append(data)

for data in pred_result:
    print(data*100)