import csv
import matplotlib.pyplot as plt

names = []
age = []
weight = []
steps = []

# Read dataset
with open("dataset.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        names.append(row["Name"])
        age.append(int(row["Age"]))
        weight.append(int(row["Weight"]))
        steps.append(int(row["Steps"]))

# Average weight
avg_weight = sum(weight) / len(weight)
print("Average Weight:", avg_weight)

# Find person with highest steps
max_steps = max(steps)
index = steps.index(max_steps)

print("Most Active Person:", names[index])
print("Steps:", max_steps)

# Activity Report
print("\nActivity Report")
for i in range(len(names)):
    if steps[i] > 6000:
        print(names[i], "- Active")
    else:
        print(names[i], "- Less Active")

# Bar Graph
plt.bar(names, steps)
plt.xticks(rotation=90)

plt.title("Daily Steps Analysis")
plt.xlabel("People")
plt.ylabel("Steps")

plt.show()
