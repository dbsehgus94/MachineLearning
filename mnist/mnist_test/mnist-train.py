from sklearn import model_selection, svm, metrics

# CSV 파일을 읽어 들이고 가공하기
def load_csv(fname):
    labels = []
    images = []
    with open(fname, "r") as f:
        for line in f:
            cols=line.split(",")
            if len(cols) < 2:
                continue
            #print(cols.pop(0), end=" ")
            labels.append(int(cols.pop(0))) # pop : 리스트 항목을 지운다. 리턴되는 값은 지운 리스트 값으로 들어간다.
            #print(labels[0])
            vals = list(map(lambda n: int(n) / 256, cols))
            #print(vals, end=" ")
            images.append(vals)
    return {"labels":labels, "images":images}

data = load_csv("./mnist/train.csv") # 상대 경로 # 처음부터 경로를 쓰면 절대 경로
test = load_csv("./mnist/t10k.csv")

# 학습하기
clf = svm.SVC()
clf.fit(data["images"], data["labels"])

# 예측하기
predict = clf.predict(test["images"])

# 결과 확인하기
ac_score = metrics.accuracy_score(test["labels"], predict)
cl_report = metrics.classification_report(test["labels"], predict)
print("정답률 =", ac_score)
print("리포트 =")
print(cl_report)
