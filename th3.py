f = open("file.txt", "r")

import matplotlib.pyplot as plt
import numpy as np
# hard code variables
def quadratic_model(f,time):
  HUMIDITY =int(f.readline())
  WIND =int(f.readline())
  PRECIPITATION =int(f.readline())
  temperature = HUMIDITY*time*time + WIND*time + PRECIPITATION
  return temperature

time_values=np.linspace(0,10,50)
temperature_hardcoded = quadratic_model(f,time_values)

plt.plot(time_values,temperature_hardcoded, label='temperature with hard coded coefficients')
plt.xlabel('Time')
plt.ylabel('Temperature')
plt.legend()
plt.title('weather modeling with quadratic equation(read from file)')
plt.show()