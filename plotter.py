import csv
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm

groups = {}
ignored_sims = ["bp-taken", "bp-nottaken"]
with open("step1_results.csv") as csvfile:
  reader = csv.reader(csvfile, delimiter=',')
  # skip header row
  next(reader, None)
  titles = {
    "func": "Functional Unit Modifications",
    "mem-dl1": "L1 Data Cache Modifications",
    "mem-il1": "L1 Instruction Cache Modifications",
    "bp": "Branch Predictor Modifications",
    "dp": "Data Path Modifications",
    "mem-dl2-separated": "L2 Data Cache Modifications",
    "mem-il2-separated": "L2 Instruction Cache Modifications",
    "mem-l2-unified": "Unified L2 Cache Modifications",
  }
  for row in reader:
    group = row[0]
    config = row[1]
    if config in ignored_sims:
      continue
    if group == "mem":
      mem_group = row[1].split("-")
      group = mem_group[0] + "-" + mem_group[1]
      config = config.replace(group + "-", "")
      if "l2" in group:
        if "separated" in config:
          group += "-separated"
          config = config.replace("separated-", "")
        else:
          group = group.replace("dl2", "l2")
          group += "-unified"
    if not group in groups:
      groups[group] = {
        "x": [],
        "y": [],
        "labels": []
      }
    groups[group]["x"].append(float(row[2]))
    groups[group]["y"].append(float(row[3]))
    groups[group]["labels"].append(config)

for group_key, data in groups.iteritems():
  if group_key == "base":
    continue
  x = data["x"]
  y = data["y"]
  labels = data["labels"]
  labels.insert(0, "base")
  colors = cm.rainbow(np.linspace(0, 1, len(y)))
  fig = plt.figure()
  #fig = plt.figure(num=1, figsize=(13, 13), dpi=80, facecolor='w', edgecolor='k')
  points = [plt.scatter(groups["base"]["x"][0], groups["base"]["y"][0], color="black", marker="x")]
  for i in range(0, len(y)):
    points.append(plt.scatter(x[i], y[i], color=colors[i]))
  ax = plt.subplot(111)
  plt.sca
  ax.set_title(titles[group_key])
  ax.set_xlabel("Performance")
  ax.set_ylabel("EDP")
  ax.ticklabel_format(useOffset=False, style="plain")
  plt.legend(points,
           labels,
           scatterpoints=1,
           loc="upper left",
           bbox_to_anchor=(1, 1),
           fontsize=8)
  fig.subplots_adjust(right=0.75)
  plt.savefig(group_key + ".png")
  plt.close(fig)



# lo = plt.scatter(random(10), random(10), marker='x', color=colors[0])
# ll = plt.scatter(random(10), random(10), marker='o', color=colors[0])
# l  = plt.scatter(random(10), random(10), marker='o', color=colors[1])
# a  = plt.scatter(random(10), random(10), marker='o', color=colors[2])
# h  = plt.scatter(random(10), random(10), marker='o', color=colors[3])
# hh = plt.scatter(random(10), random(10), marker='o', color=colors[4])
# ho = plt.scatter(random(10), random(10), marker='x', color=colors[4])


plt.show()