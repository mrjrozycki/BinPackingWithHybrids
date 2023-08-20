import matplotlib.pyplot as plt
import numpy as np

# Open csv file
# It has the following format:
# First column is the name of the algorithm
# Second column is percentage error of the algorithm
# Third column is the time taken by the algorithm
file = open("results.csv", "r")

# Read the csv file
# Create a dictionary with key as the name of the algorithm
# and value as a list of tuples (percentage error, time taken)
# for each algorithm
data = {}
for line in file:
    line = line.strip().split(",")
    if line[0] not in data:
        data[line[0]] = [(float(line[1]), float(line[2]))]
    else:
        data[line[0]].append((float(line[1]), float(line[2])))
file.close()

# Create a figure
fig = plt.figure()

# Create a subplot
ax = fig.add_subplot(111)

# Set the title of the graph
ax.set_title("Percentage Error of hybrid algorithms")

# Set the x-axis label
ax.set_xlabel("Name of the algorithm")

# Set the y-axis label
ax.set_ylabel("Percentage error")

# Show only percantage error data with algo names on the graph
# for each algorithm
for algo in data:
    x = []
    y = []
    for i in range(len(data[algo])):
        x.append(algo)
        y.append(data[algo][i][0])
    ax.plot(x, y, label = algo)


# Show the legend
ax.legend()

# Save the graph
plt.savefig("graph.png")

# Show the graph
plt.show()