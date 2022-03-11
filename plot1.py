import numpy as np
import matplotlib.pyplot as plot

x = np.linspace(0, 2, 50)

fig, ax = plot.subplots()

ax.plot(x, x, label= "linear")
ax.plot(x, x**2, label = "quadratic")
ax.plot(x, x**3, label = "cubic")
ax.set_xlabel("xlabel")
ax.set_ylabel("ylabel")
ax.set_title("simpleplot")
ax.legend()

plot.show()
