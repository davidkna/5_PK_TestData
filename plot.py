import os
import glob
import locale
import pandas as pd
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt

locale.setlocale(locale.LC_ALL, "de_de")
mpl.rcParams['axes.formatter.use_locale'] = True
sns.set_context("paper")


files = [fn for fn in glob.iglob(
    '*/*.csv') if not os.path.basename(fn).startswith('dist')]

for fileName in files:
    print("Plotting " + fileName + "…")
    data = pd.io.parsers.read_csv(
        fileName, names=["x", "y"], header=None)
    savePath = os.getcwd() + "/" + fileName.replace(".csv", "") + '.png'

    fig = plt.figure()
    ax = fig.add_subplot(111)

    ax.scatter(x=data["x"], y=data["y"], s=1)

    ax.set_xlabel("Länge")
    ax.set_ylabel("Zeit in s")

    ax.set_xlim(0, 100000)
    ax.set_ylim(0)

    fig.savefig(savePath, bbox_inches='tight', dpi=300)
    plt.close(fig)
