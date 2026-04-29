import matplotlib.pyplot as plt
#matplotlib is for data visualization

values = list(range(1, 6))
squares = [1, 4, 9, 16, 25]

figure, ax = plt.subplots()
#tuple decomposistion cause you take a tuple and put into variables
ax.plot( values, squares)

ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

plt.style.use("Solarize_Light2")
plt.show()
