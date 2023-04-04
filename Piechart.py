import matplotlib.pyplot as plt

# defining labels
sports = ['cricket', 'soccer', 'tennis', 'badminton', 'hockey']

# portion covered by each label
slices = [25, 9, 12, 15, 11]

# colour for each label
colors = ['red', 'blue', 'orange', 'green', 'purple']

# plotting the pie chart
plt.pie(slices, labels = sports, colors=colors,
        startangle=30, shadow = True, explode = (0, 0, 0, 0),
        radius = 1.2, autopct = '%2.2f%%')

# plotting legend
plt.legend()

# showing the plot
plt.show()