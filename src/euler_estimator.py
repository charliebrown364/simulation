import matplotlib.pyplot as plt
plt.style.use('bmh')

class EulerEstimator():

    def __init__(self, derivatives):
        self.derivatives = derivatives
    
    def calc_derivative_at_point(self, point):
        ans = {}
        for (key, value) in self.derivatives.items():
            ans[key] = value(point[0], point[1])
        return ans

    def step_forward(self, point, step_size):
        new_x = point[0] + step_size
        new_y = {}
        for (key, value) in self.calc_derivative_at_point(point).items():
            new_y[key] = round(point[1][key] + step_size*value, 5)
        return (new_x, new_y)

    def calc_estimated_points(self, point, step_size, num_steps):
        ans = []
        for i in range(num_steps + 1):
            ans.append(point)
            point = self.step_forward(point, step_size)
        return ans
    
    def plot(self, point, step_size, num_steps, other_functions={}):

        points = self.calc_estimated_points(point, step_size, num_steps)
        t = [pair[0] for pair in points]

        self_derivatives_values = list(self.derivatives.values())
        for i in range(len(self_derivatives_values)):
            key = [list(point[1].keys()) for point in points][0][i]
            arr = [pair[1][key] for pair in points]
            plt.plot(t, arr, label=key)

        for (name, f) in other_functions.items():
            y = [f(pair[0]) for pair in points]
            plt.plot(t, y, label=name)
        
        plt.legend()
        plt.savefig('euler_estimation.png')