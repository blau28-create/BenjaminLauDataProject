from random import choice
import matplotlib.pyplot as plt

class RandomWalk:
    def __init__(self, num_points=500):
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2 , 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance


            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

random_walk = RandomWalk()
random_walk.fill_walk()
figure, ax =plt.subplots()
ax.set_title("Random Walk", fontsize=24)
ax.set_xlabel("Horizontal Movement", fontsize=14)
ax.set_ylabel("Vertical Movement", fontsize=14)
ax.plot(random_walk.x_values, random_walk.y_values, linewidth=1)
ax.scatter(random_walk.x_values, random_walk.y_values, s=2)
plt.show()