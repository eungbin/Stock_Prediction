# Stock_Prediction
### Stock_Prediction with React.js, Python

#### Python Part

+ 2020.09.07  -->  파이썬 csv파일 불러와서 차트 띄우기
+ 2020.09.07  -->  불러온 csv파일 데이터 정규화 [ Data Normalization ]
+ 2020.09.07  -->  LSTM 모델 생성
+ 2020.09.10  -->  작성된 모델을 이용하여 최근50일을 기준으로 내일 가격 예측 완료
+ 2020.09.11  -->  csv파일 Date, High, Low값들 DB저장 완료
+ 2020.09.14  -->  csv파일을 이용하지 않고 DB에서 불러온 데이터로 학습을 진행, DB내의 최근 50개의 데이터를 기준으로 다음날 가격 예측성공
+ 2020.09.14  -->  yahoo finance API를 이용하여 최신 주가정보 가져와, csv파일로 변환하고 DB에 저장
+ 현재까지 시스템 흐름
+ save_csv.py  [최신 주가정보 가져와 csv파일로 변환하여 저장] -> insert_db.py [변환한 csv파일을 로드하여 db에 저장] -> LSTM_model.py [최신 주가정보가 반영된 db를 기준으로 모델파일 생성] -> model_predict.py [생성된 모델파일을 이용하여 다음날 주가 예측]

예정) 생성된 kears 모델 파일 tensorflow.js를 이용하여 javascript에서 사용 가능한 모델파일로 변환

------

#### React.js Part

+ 2020.09.14  -->  React.js 프로젝트 생성
예정) 프론트 디자인 + 백엔드 node.js 연결
