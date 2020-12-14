import pandas as pd

# 크롤링한 naver news csv 파일 load
csv_craw_data = pd.read_csv('dataset/naver_news/news.csv', encoding='utf-8-sig')

# pickle file load
load_pickle = pd.read_pickle("../real_data.pickle")

# nan 값을 ''[공백]으로 대체
csv_craw_data.fillna('', inplace=True)

# 각 종목의 코드를 이용한 배열 선언 및 뉴스데이터 매치
for stock in load_pickle.values:
    globals()['news_list_{}'.format(stock[1])] = []
    for data in csv_craw_data[stock[0]]:
        if data != "":
            globals()['news_list_{}'.format(stock[1])].append(data)

for stock in load_pickle.values:
    for data in globals()['news_list_{}'.format(stock[1])]:
        print("{0}'s data : {1}".format(stock[0], data))