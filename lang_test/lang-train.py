from sklearn import svm, metrics
import glob, os.path, re, json

# 텍스트를 읽어 들이고 출현 빈도 조사하기
def check_freq(fname): # 빈도 수 체크
    name = os.path.basename(fname)
    #print(name)
    lang = re.match(r'^[a-z]{2,}', name).group()
    #print(lang)
    with open(fname, "r", encoding="utf-8") as f:
        text = f.read()
    text = text.lower() # 소문자 변환
    # 숫자 세기 변수(cnt) 초기화하기
    cnt = [0 for n in range(0, 26)]
    #print(cnt)
    code_a = ord("a") # ASCII 값으로 전환
    #print(code_a)
    code_z = ord("z")
    #print(code_z)

    # 알파벳 출현 횟수 구하기
    for ch in text:
        n = ord(ch) # ASCII 값으로 전환
        if code_a <= n <= code_z: # a~z 사이에 있을 때
            cnt[n - code_a] += 1 # 횟수
    # 정규화하기
    total = sum(cnt)
    freq = list(map(lambda n: n / total, cnt))
    #print(lang, end="\n")
    return (freq, lang)

# 각 파일 처리하기
def load_files(path):
    freqs = []
    labels = []
    file_list = glob.glob(path) # 특정 파일만 모아서 출력하기 http://wifidocs.net/3746
    for fname in file_list:
        r = check_freq(fname) # 함수 호출
        #print(r, end="\n")
        #print(type(r), end=" ")
        freqs.append(r[0])
        labels.append(r[1])
    return {"freqs":freqs, "labels":labels}
data = load_files("./lang/train/*.txt") # 모든 txt파일을 다 가져오겠다.
test = load_files("./lang/test/*.txt")

# 이후를 대비해서 JSON으로 결과 저장하기
with open("./lang/freq.json", "w", encoding="utf-8") as fp:
    json.dump([data, test], fp)

# 학습하기
clf = svm.SVC()
clf.fit(data["freqs"], data["labels"])

# 예측하기
predict = clf.predict(test["freqs"])

# 결과 테스트하기
ac_score = metrics.accuracy_score(test["labels"], predict)
cl_report = metrics.classification_report(test["labels"], predict)
print("정답률 =", ac_score)
print("리포트 =")
print(cl_report)