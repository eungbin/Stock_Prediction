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

+ 2020.09.23  -->  수정사항) 여러개의 주식데이터를 가져오기 위해 pickle 이용 -> 약 700여개 기업의 주가데이터를 가져와서 csv파일로 저장함 [파일이름 : 코드번호] -> 해당 기업들의 코드번호를 이용하여 MySQL DB 테이블 작성함

+ 2020.09.24  -->  약 700여개 기업에 대한 주가정보 MySQL DB Insert

+ 2020.09.26  -->  진행중) Yahoo Finance API를 이용하여 주가정보 최신화 작업

+ 변경된 점 : 기존에는 Yahoo Finance API를 이용하여 주가정보를 가져온 뒤, csv파일로 변환한 뒤, csv파일을 이용하여 DB에 저장했지만, 기업의 수가 너무 많은 관계로 csv파일로 변환하지 않고 바로 DB에 저장함               [초기작업 시에만 csv파일로 변환하여 저장함]

+ 2020.10.04  -->  실제 사용할 데이터만 뽑아냄 [ real_data.pickle] 5개

+ 예정) 5개 기업에 대한 각각의 혹은 하나의 모델 파일  작성 [하나로 통합된 모델이 존재하게끔]

+ 2020.10.04  -->  각 5개 기업에 대한 각각의 모델파일 생성 [하나로 통합 못했음]

  한 Batch당 6초 20번 120초 => 하나의 모델파일 생성하는데 2분 => 총10분
  => 그래픽카드 사용
  
+ 2020.10.14  -->  LSTM 주가예측값 DB저장 완료 -Plan B Python part 끝-

+ 수정사항) 기존DB date, high, low 3개  ==> + open close volume 총 6개 column



------

#### React.js Part

+ 2020.09.14  -->  React.js 프로젝트 생성
+ 2020.10.14  -->  Reach - Node - MySQL 연동
+ 2020.10.15  -->  대강적인 UI구현, 차트연동
+ 예정) 요청게시판, 
