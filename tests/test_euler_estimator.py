import sys
sys.path.append('src')
from euler_estimator import EulerEstimator

# def rounding(this_dict): return {key:round(value, 5) for key, value in this_dict.items()}

derivatives = {
                'A': (lambda t,x: x['A'] + 1),
                'B': (lambda t,x: x['A'] + x['B']),
                'C': (lambda t,x: 2*x['B']) 
              }

euler = EulerEstimator(derivatives = derivatives)

initial_values = {'A': 0, 'B': 0, 'C': 0}
initial_point = (0, initial_values)

euler.plot(point=initial_point, step_size=0.01, num_steps=500)

print("passed")