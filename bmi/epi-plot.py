import matplotlib.pyplot as plt
import pandas as pd

tbl = pd.read_csv("epi.csv", index_col=2)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

def scatter(lbl, color):
    b = tbl.loc[lbl]
    ax.scatter(b["cir"], b["ur"], c=color, label=lbl)
scatter("hell", "red")
scatter("unstable", "blue")
scatter("livable", "green")

ax.legend()
plt.savefig("epi-test.png")
#plt.show()

