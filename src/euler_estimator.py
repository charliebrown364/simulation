import matplotlib.pyplot as plt
plt.style.use('bmh')

class EulerEstimator():

    def __init__(self, derivatives):
        self.derivatives = derivatives
    
    def calc_derivative_at_point(self, point):
        y_init_values = list(point[1].values())
        return {key:value(y_init_values, point[1]) for (key,value) in self.derivatives.items()}

    def step_forward(self, point, step_size):
        new_x = point[0] + step_size
        new_y = {key:round(point[1][key] + step_size*value, 5) for key, value in self.calc_derivative_at_point(point).items()}
        return (new_x, new_y)

    def calc_estimated_points(self, point, step_size, num_steps):
        ans = []
        for i in range(num_steps + 1):
            ans.append(point)
            point = self.step_forward(point, step_size)
        return ans
    
    def plot(self, point, step_size, num_steps):

        t = [pair[0] for pair in self.calc_estimated_points(point, step_size, num_steps)]
        points = self.calc_estimated_points(point, step_size, num_steps)

        for i in range(len(list(self.derivatives.values()))):
            key = [list(point[1].keys()) for point in points][0][i]
            arr = [pair[1][key] for pair in points]
            plt.plot(t, arr)

        plt.xlabel('t')
        plt.ylabel('y')
        plt.title('Euler Estimation')
        plt.savefig('euler_estimation.png')