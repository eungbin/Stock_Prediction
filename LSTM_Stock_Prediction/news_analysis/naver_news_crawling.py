from urllib.request import urlopen
from bs4 import BeautifulSoup


for i in range(10):
    html = urlopen("https://finance.naver.com/news/news_list.nhn?mode=LSS2D&section_id=101&section_id2=258&page={0}".format(str(i)))

    bsObject = BeautifulSoup(html, "html.parser")

    test = bsObject.select('body > div#wrap > div#newarea > div#contentarea > div#contentarea_left > ul.realtimeNewsList > li.newsList a')

    for data in test:
        print(data.get_text())