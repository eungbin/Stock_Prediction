import codecs
import pandas as pd
import re

positive = []
negative = []
posneg = []

pos = codecs.open('./positive_words_self.txt', 'rb', encoding='UTF-8')

while True:
    line = pos.readline()
    line = line.replace('\n', '')
    positive.append(line)
    posneg.append(line)

    if not line: break
pos.close()

neg = codecs.open('./negative_words_self.txt', 'rb', encoding='UTF-8')

while True:
    line = neg.readline()
    line = line.replace('\n', '')
    negative.append(line)
    posneg.append(line)

    if not line: break
neg.close()

label = [0] * 210596
title_dic = {"title":[], "label":label}
j = 0
start = 2006
end = 2018
csv_title_lists = []
titles = []
count = 0

while start <= end:
    csv_data = pd.read_csv('./dataset/'+str(start)+'/MBN00003U_10_'+str(start)+'.csv', encoding='CP949')
    csv_title_lists.append(csv_data['ART_SJ_CN'])
    start += 1

for title_list in csv_title_lists:
    for text in title_list:
        titles.append(text)

for title in titles:
    title_data = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…\"\“》]', '', title)
    if title_data == "뉴욕 증시" or title_data == "10시 시황" or title_data == "12시 시황" or title_data == "2시 시황" or \
        title_data == "뉴욕증시" or title_data == "10시시황" or title_data == "12시시황" or title_data =="2시시황" or \
        title_data == "마감시황" or title_data == "11시 시황" or title_data == "11시시황" or title_data == "증시 하이라이트" or \
        title_data == "이시각 주식시장" or title_data == "이 시각 주식시장":
        continue
    title_dic['title'].append(title_data)
    count += 1

    for i in range(len(posneg)):
        if posneg[i] == '':
            continue
        posFlag = False
        negFlag = False
        if i < (len(positive)-1):
            if title_data.find(posneg[i]) != -1:
                posFlag = True
                print(i, "positive?", "테스트 : ", title_data.find(posneg[i]), "비교단어 : ", posneg[i], "인덱스 : ", i, title_data)
                break
        if i > (len(positive)-2):
            if title_data.find(posneg[i]) != -1:
                negFlag = True
                print(i, "negative?", "테스트 : ", title_data.find(posneg[i]), "비교단어 : ", posneg[i], "인덱스 : ", i, title_data)
                break
    if posFlag == True:
        label[j] = 1
    elif negFlag == True:
        label[j] = -1
    elif negFlag == False and posFlag == False:
        label[j] = 0
    j += 1
# print(count)
title_dic['label'] = label
title_df = pd.DataFrame(title_dic)

def dftoCsv(df, num):
    df.to_csv(('./title_datas'+ str(num) +'.csv'), sep=',', na_rep='NaN', encoding='CP949')

dftoCsv(title_df, 2)
print(posneg)
print(len(positive))
print(len(posneg))