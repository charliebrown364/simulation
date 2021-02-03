import sys
sys.path.append('src')
from euler_estimator import EulerEstimator

"""

- Initially, there are 100 deer and 10 wolves.

- In the absence of wolves, the deer population would increase at the instantaneous rate of 60% per year.

- In the absence of deer, the wolf population would decrease at the instantaneous rate of 90% per year.

- The wolves and deer meet at an instantaneous rate of 0.05 times per wolf per deer per year, and every time a wolf meets a deer, it kills and eats the deer.

- The rate at which the wolf population increases is proportional to the number of deer that are killed, by a factor of 0.4. In other words, the wolf population grows by a rate of 0.4 wolves per deer killed per year.

Check your answer: at t = 0, you should have dD/dt = 10 and dW/dt = 11.

"""

# x['predator'] or x['prey']
derivatives = {
                'prey': (lambda t,x: 0.6 * x['prey'] - 0.05 * x['predator'] * x['prey']),
                'predator': (lambda t,x: -0.9 * x['predator'] + 0.4 * 0.05 * x['predator'] * x['prey'])
              }

euler = EulerEstimator(derivatives = derivatives)
initial_values = {'predator': 10, 'prey': 100}
initial_point = (0, initial_values)

print(euler.calc_derivative_at_point(initial_point))

euler.plot(point=initial_point, step_size=0.001, num_steps=100000)