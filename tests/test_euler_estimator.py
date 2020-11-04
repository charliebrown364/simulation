import sys
sys.path.append('src')
from euler_estimator import EulerEstimator

print("Testing Assignment 24-1...")

euler = EulerEstimator(derivative = (lambda t: t+1))

assert euler.calc_derivative_at_point((1, 4)) == 2, euler.calc_derivative_at_point((1, 4))

assert euler.step_forward(point = (1, 4), step_size = 0.5) == (1.5, 5), euler.step_forward(point = (1, 4), step_size = 0.5)

ans = [
        (1, 4), # starting point
        (1.5, 5), # after 1st step
        (2, 6.25), # after 2nd step
        (2.5, 7.75), # after 3rd step
        (3, 9.5) # after 4th step
      ]

assert euler.calc_estimated_points(point = (1, 4), step_size = 0.5, num_steps = 4) == ans, euler.calc_estimated_points(point = (1, 4), step_size = 0.5, num_steps = 4)

print("Passed Assignment 24-1")