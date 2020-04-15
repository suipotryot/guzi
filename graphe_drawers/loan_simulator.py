""" Calculate and print which loans are "cheat" to find where users could :
    1. Make a loan
    2. Put the loan amount on his or her account
    3. Have a better daily income then
"""

import matplotlib.pyplot as plt
from pylab import *
import numpy as np

# Now graph under this first draw
z = np.linspace(33*33*33, 500**3, 10000)

plt.plot(z, 11060*np.float_power(z, 1/3)-420000)

x_points = []
y_points = []

for total_accumulated in range(33*33*33, 500**3, 1000):
    daily_earn = total_accumulated ** (1/3)
    max_loan = int(daily_earn) - 32
    point_added = False
    for time in range(1, 30):
        new_total_accumulated = total_accumulated + time * max_loan * 365
        if new_total_accumulated ** (1/3) - max_loan - total_accumulated ** (1/3) > 2:
            #print(total_accumulated, total_accumulated ** (1/3), new_total_accumulated ** (1/3) - max_loan, max_loan, time)
            x_points.append(total_accumulated)
            y_points.append(time*max_loan*365)
            point_added = True
            break
    if not point_added:
        x_points.append(total_accumulated)
        y_points.append(30*max_loan*365)
    else:
        point_added = False


x = array(x_points)
y = array(y_points)

plt.xlabel('Total accumulé')
#plt.ylabel('Temps d\'emprunt max')
plt.ylabel('Valeur d\'emprunt max')

plt.plot(x, y)


plt.show()
