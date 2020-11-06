import sys
sys.path.append('src')
from euler_estimator import EulerEstimator

print("Testing Assignment 24-1...")

euler = EulerEstimator(lambda t: t+1)

assert euler.calc_derivative_at_point((1, 4)) == 2, euler.calc_derivative_at_point((1, 4))

assert euler.step_forward((1, 4), 0.5) == (1.5, 5), euler.step_forward((1, 4), 0.5)

ans = [
        (1, 4), # starting point
        (1.5, 5), # after 1st step
        (2, 6.25), # after 2nd step
        (2.5, 7.75), # after 3rd step
        (3, 9.5) # after 4th step
      ]

assert euler.calc_estimated_points((1, 4), 0.5, 4) == ans, euler.calc_estimated_points((1, 4), 0.5, 4)

euler.plot((-5, 10), 0.1, 100)

print("Passed Assignment 24-1")