import matplotlib.pyplot as plt
import numpy as np
# hard code variables
def quadratic_model(HUMIDITY,WIND,PRECIPITATION,time):
  temperature = HUMIDITY*time*time + WIND*time + PRECIPITATION
  return temperature

time_values=np.linspace(0,10,100)
HUMIDITY =int(input("Enter value of HUMIDITY: "))
WIND =int(input("Enter value of WIND : "))
PRECIPITATION =int(input("Enter value of PRECIPITATION : "))
temperature_hardcoded = quadratic_model(HUMIDITY,WIND,PRECIPITATION,time_values)

plt.plot(time_values,temperature_hardcoded, label='temperature with hard coded coefficients')
plt.xlabel('Time')
plt.ylabel('Temperature')
plt.legend()
plt.title('weather modeling with quadratic equation(keyboard input)')
plt.show()