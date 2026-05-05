import random
import plotly.express as px

class Dice:
    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        return random.randint(1, self.num_sides)


results = []
dice1 = Dice()
dice2 = Dice()

for i in range(10000):
    results.append(dice1.roll() + dice2.roll())

frequencies = []
for side in range(2, dice1.num_sides + dice2.num_sides + 1):
    frequency = results.count(side)
    frequencies.append(frequency)
labels = {'x':'Result', 'y': 'Frequency'}
figure = px.bar(x=range(2, dice1.num_sides + dice2.num_sides + 1), y=frequencies, title ="Frequency of The Sum of Two Dice Rolls", labels=labels)
figure.show()

figure.write_html("graph.html")