import numpy as np
import matplotlib.pyplot as plt

# is there a relationship between absolute magnitude and radius of a star?
data = np.genfromtxt('6 class csv.csv', delimiter=',')


plt.plot(data[:-1, 2], data[:-1, 3], 'ro')
plt.xlabel('Radius (R/Ro)')
plt.ylabel('Absolute Magnitude (Mv)')

plt.axis([0, 1, 0, 22])
plt.show()