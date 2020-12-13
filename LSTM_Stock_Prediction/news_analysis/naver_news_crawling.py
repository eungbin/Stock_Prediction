from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

news_list = []
find_keyword = ''
real_news_list = []
stock_in_use = []
dic_stock = {}
max_length = 0

# pickle파일 로드
load_pickle = pd.read_pickle("../real_data.pickle")

# 현재 사용중인 종목들의 이름 stock_in_use 배열에 저장, dic_stock 딕셔너리에 {종목이름: 종목코드} 쌍으로 저장
for data in load_pickle.values:
    stock_in_use.append(data[0])
    dic_stock[data[0]] = data[1]
    globals()['news_list_{}'.format(data[1])] = []

# 네이버 금융 실시간 속보 크롤링
for i in range(10):
    html = urlopen("https://finance.naver.com/news/news_list.nhn?mode=LSS2D&section_id=101&section_id2=258&page={0}".format(str(i)))

    bsObject = BeautifulSoup(html, "html.parser")

    test = bsObject.select('body > div#wrap > div#newarea > div#contentarea > div#contentarea_left > ul.realtimeNewsList > li.newsList a[title]')

    for data in test:
        print(data.get_text())
        news_list.append(data.get_text())   # 실시간 속보 배열에 저장

# 모든 뉴스중 키워드가 포함된 뉴스만 배열에 저장
for news in news_list:
    for keyword in dic_stock.keys():
        if news.find(keyword) != -1:
            globals()['news_list_{}'.format(dic_stock[keyword])].append(news)

# 각 키워드가 포함된 뉴스 배열 중 가장 긴 배열의 길이를 찾아서 max_length에 저장
for keyword in dic_stock.keys():
    print(globals()['news_list_{}'.format(dic_stock[keyword])])
    if max_length < globals()['news_list_{}'.format(dic_stock[keyword])].__len__():
        max_length = globals()['news_list_{}'.format(dic_stock[keyword])].__len__()

# 빈 DataFrame 생성
df_news = pd.DataFrame()

# 가장 긴 뉴스 배열의 길이를 이용하여 나머지값 '' 채워줌 (배열들의 길이를 맞춰준다.)
for keyword in dic_stock.keys():
    list_len = globals()['news_list_{}'.format(dic_stock[keyword])].__len__()
    for i in range((max_length-list_len)):
        globals()['news_list_{}'.format(dic_stock[keyword])].append('')

# DataFrame에 각 키워드가 포함된 뉴스들을 추가
for keyword in dic_stock.keys():
    df_news[keyword] = globals()['news_list_{}'.format(dic_stock[keyword])]

df_news.to_csv('./dataset/naver_news/news.csv', encoding='utf-8-sig')