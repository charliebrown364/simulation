import sys
sys.path.append('src')
from euler_estimator import EulerEstimator

"""

- There are initially 1000 susceptible people and 1 infected person.

- The number of meetings between susceptible and infected people each day is proportional to the product of the numbers of susceptible and infected people, by a factor of 0.01. The transmission rate of the disease is 3%. (In other words, 3% of meetings result in transmission.)

- Each day, 2% of infected people recover.

Check: If you've written the system correctly, then at t=0, you should have dS/dt = -0.3, dI/dt = 0.28, dR/dt = 0.02.
 
"""

derivatives = {
                'S': (lambda t,x: -1 * 0.03 * 0.01 * x['S'] * x['I']),
                'I': (lambda t,x: 0.03 * 0.01 * x['S'] * x['I'] - 0.02 * x['I']),
                'R': (lambda t,x: 0.02 * x['I']) 
              }

euler = EulerEstimator(derivatives = derivatives)
e
initial_values = {'S': 1000, 'I': 1, 'R': 0}
initial_point = (0, initial_values)

print(euler.calc_derivative_at_point(initial_point))

euler.plot(point=initial_point, step_size=1, num_steps=400)