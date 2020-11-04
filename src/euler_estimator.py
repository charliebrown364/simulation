class EulerEstimator():

    def __init__(self, derivative):
        self.derivative = derivative
    
    def calc_derivative_at_point(self, point):
        x = point[0]
        return self.derivative(x)

    def step_forward(self, point, step_size):
        x = point[0]
        y = point[1]
        new_x = x + step_size
        new_y = y + (self.calc_derivative_at_point(point) * step_size)
        return (new_x, new_y)

    def calc_estimated_points(self, point, step_size, num_steps):
        ans = []
        for i in range(num_steps + 1):
            ans.append(point)
            point = self.step_forward(point, step_size)
        return ans