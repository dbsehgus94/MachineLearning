from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import pandas as pd

tbl = pd.read_csv("epi.csv")

label = tbl["label"]
#print(label)
c = tbl["cir"] / 33 # 최대 33%라고 가정
#print(c)
u = tbl["ur"] / 67 # 최대 67%라고 가정
cu = pd.concat([c, u], axis=1)
#print(u)
#print(cu)

data_train, data_test, label_train, label_test = \
    train_test_split(cu, label)

clf = svm.SVC()

clf.fit(data_train, label_train)

predict = clf.predict(data_test)

ac_score = metrics.accuracy_score(label_test, predict)
cl_report = metrics.classification_report(label_test, predict)
print("정답률 =", ac_score)
print("리포트 =\n", cl_report)
