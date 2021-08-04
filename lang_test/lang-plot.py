import matplotlib.pyplot as plt
import pandas as pd
import json

# 알파벳 출현 빈도 데이터 읽어 들이기
with open("./lang/freq.json", "r", encoding="utf-8") as fp:
    freq = json.load(fp)

# 언어마다 계산하기
lang_dic = {}
#print(type(freq))
for i, lbl in enumerate(freq[0]["labels"]): #0-data를 의미 0번째 라인의 값을 가져다 쓰겠다.
    fq = freq[0]["freqs"][i]
    #print(lbl)
    #print(fq)
    if not (lbl in lang_dic):
        lang_dic[lbl] = fq
        continue
    for idx, v in enumerate(fq):
        #print(idx, v)
        lang_dic[lbl][idx] = (lang_dic[lbl][idx] + v) / 2

# Pandas의 DataFrame에 데이터 넣기
asclist = [[chr(n) for n in range(97, 97+26)]]
#print(asclist)
df = pd.DataFrame(lang_dic, index=asclist)
#print(df)

# 그래프 그리기
plt.style.use('ggplot')
#df.plot(kind="bar", subplots=True, ylim=(0, 0.15))
df.plot(kind="line")
plt.show()
plt.savefig("lang-plot.png")
