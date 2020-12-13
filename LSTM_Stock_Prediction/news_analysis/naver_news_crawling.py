from urllib.request import urlopen
from bs4 import BeautifulSoup

news_list = []
find_keyword = '삼성전자'
real_news_list = []

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
    if news.find(find_keyword) != -1:
        real_news_list.append(news)

print(real_news_list)