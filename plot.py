import os
import glob
import locale
import pandas as pd
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt

locale.setlocale(locale.LC_ALL, "de_DE")
mpl.rcParams['axes.formatter.use_locale'] = True
sns.set_context("paper")

for fileName in glob.iglob('*/*.csv'):
	print("Plotting " + fileName + "…")

	data = pd.io.parsers.read_csv(
		fileName, names=["x", "y"], header=None)
	save_path = os.getcwd() + "/" + fileName.replace(".csv", "") + '.png'

	fig = plt.figure()
	ax = fig.add_subplot(111)

	alpha = 0.1
	if fileName.endswith("IS.csv"):
		alpha = 0.5

	ax.scatter(x=data["x"], y=data["y"], s=1, lw = 0, alpha=alpha)

	if os.path.basename(fileName).startswith('dist'):
		ax.set_xlabel("Wiederholungen")
		ax.set_ylabel("Zeit in s")

		ax.set_xlim(0, 10000)
		ax.set_ylim(0)
	else:
		ax.set_xlabel("Länge")
		ax.set_ylabel("Zeit in s")

		ax.set_xlim(0, 100000)
		ax.set_ylim(0)

	fig.savefig(save_path, bbox_inches="tight", dpi=300)
	plt.close(fig)
