import matplotlib.pyplot as plt
plt.style.use('bmh')

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
    
    def plot(self, point, step_size, num_steps):
        
        x_coords = [round(pair[0], 4) for pair in self.calc_estimated_points(point, step_size, num_steps)]
        y_coords = [round(pair[1], 4) for pair in self.calc_estimated_points(point, step_size, num_steps)]
        
        plt.plot(x_coords, y_coords)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Euler estimation')
        plt.savefig('euler_estimation.png')