import os
import glob
import locale
import pandas as pd
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt


sns.set_palette("husl")

for dirName in glob.iglob('*/'):

	for sorter in ["IS", "QS", "RS"]:
		fig = plt.figure()
		ax = fig.add_subplot(111)
		print("Plotting  "+ dirName + sorter +"…")
		savePath = os.getcwd() + "/" + dirName + 'combine' + sorter + '.png'

		alpha = 0.1
		if sorter == "IS":
			alpha = 0.5
		for list_spawner in [["almostSorted", "fast sortiert"], ["almostReverse", "fast Rückwärts sortiert"], ["shuffled", "Zufällig"], ["rand", "Zufällig gemischt"], ["normal", "Normalverteilt"], ["fewUnique", "Wenige eigenständige"], ["equal", "gleich"]]:
			label = list_spawner[1]
			data = pd.io.parsers.read_csv(
		        dirName + list_spawner[0] + "Keys" + sorter + ".csv", names=["x", "y"], header=None)
			ax.scatter(x=data["x"], y=data["y"], s=1, alpha = alpha, label = label)

		ax.set_xlabel("Wiederholungen")
		ax.set_ylabel("Zeit in s")
		ax.set_xlim(0, 10000)
		ax.set_ylim(0, 0.5)
		fig.savefig(savePath, bbox_inches='tight', dpi=300)
		plt.close(fig)
