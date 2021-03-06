import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.model_selection import train_test_split

# 데이터 읽어 들이기
mr = pd.read_csv("mushroom.csv", header=None)

# 데이터 내부의 기호를 숫자로 변환하기
label = []
data = []
attr_list = []
for row_index, row in mr.iterrows():
    #label.append(row.ix[0])
    label.append(row.loc[0]) # loc : 인덱스 기준으로 행 읽기
    #label.append(row.iloc[0]) # iloc : 행 기준으로 행 읽기
    row_data = []
    #for v in row.ix[1:]:
    for v in row.loc[1:]: # 위와 같은 이유
    #for v in row.iloc[1:]: # 위와 같은 이유
        row_data.append(ord(v))
    data.append(row_data)

# 학습 전용과 테스트 전용 데이터로 나누기
data_train, data_test, label_train, label_test = \
    train_test_split(data, label)

# 데이터 학습시키기
clf = RandomForestClassifier()
clf.fit(data_train, label_train)

#데이터 예측하기
predict = clf.predict(data_test)

# 결과 테스트하기
ac_score = metrics.accuracy_score(label_test, predict)
cl_report = metrics.classification_report(label_test, predict)
print("정답률 =", ac_score)
print("리포드 =\n", cl_report)


