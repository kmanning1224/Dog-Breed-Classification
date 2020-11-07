graph = predict("bird2.jpg")

a_one = graph[0][0][1]
a_two = graph[0][1][1]
a_three = graph[0][2][1]
a_four = graph[0][3][1]
one = graph[0][0][2]
two = graph[0][1][2]
three = graph[0][2][2]
four = graph[0][3][2]

animals = [a_one, a_two, a_three, a_four]
probs = [one, two, three, four]
x_axis = np.arange(len(animals))
plt.figure(figsize=(8.25,6))
plt.bar(x_axis, probs, color=['darkgreen', 'lightgreen', 'yellow','orange'], align="edge")
tick_locations = [value for value in x_axis]
plt.xticks(tick_locations, animals, rotation=45, fontsize=15)
for index, value in enumerate(probs):
    plt.text(index + .15, value + .05, str('{:.3f}%'.format(value*100)), color='black', fontweight='bold', rotation=10, fontsize=12)
plt.title("Probabilities of Dog Breed", fontsize=15, fontweight='bold')
plt.xlabel("Dog Breeds", fontsize=15, fontweight='bold')
plt.ylabel("Probabilities", fontsize=15, fontweight='bold')
plt.xlim(-.5, len(x_axis)+.25)
plt.ylim(0, max(probs)+.15)
plt.show()