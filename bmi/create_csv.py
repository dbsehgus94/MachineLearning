import random

def calc_epi(c, u): # c : Consumer Inflation Rate : 소비자 물가 상승률(%), u : Unemployment Rate : 실업률(%)
    epi = c + u # Economic Pain Index 경제고통지수
    if epi < 10: return "livable"
    if epi < 45: return "unstable"
    return "hell"

fp = open("epi.csv", "w", encoding="utf-8")
fp.write("cir,ur,label\r\n")

cnt = {"livable":0, "unstable":0, "hell":0}
for i in range(25000): # 국가는 250개 정도 되지만 표본이 적어 25000으로 늘렸습니다.
    c = random.randint(int(0.3), int(30.6)) # 소비자 물가 상승률(%)
    u = random.randint(int(3.1), int(61.3)) # 실업률(%)
    label = calc_epi(c, u)
    cnt[label] += 1
    fp.write("{0},{1},{2}\r\n".format(c, u, label))
fp.close()
print("ok", cnt)

