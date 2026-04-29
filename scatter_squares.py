import matplotlib.pyplot as plt
figure, ax =plt.subplots()

values = list(range(1, 101))
squares = []
for val in values:
    squares.append(val ** 2)

ax.scatter(values, squares, s=10)

ax.set_title("Square Number", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

ax.axis([0, 110, 0, 11000]) #x min, xmax, ymin, ymax

plt.show()