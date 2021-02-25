import math
import sys
sys.path.append('src')
from euler_estimator import EulerEstimator

################################## constants

C = 1.0
V_Na = 115
V_K = -12
V_L = 10.6

g_line_Na = 120
g_line_K = 36
g_line_L = 0.3

################################## main variables: V, n, m, h

def dV_dt(t,x):
    return (s(t) - I_Na(t,x) - I_K(t,x) - I_L(t,x)) / C

def dn_dt(t,x):
    n = x['n']
    return alpha_n(t,x) * (1-n) - beta_n(t,x) * n

def dm_dt(t,x):
    m = x['m']
    return alpha_m(t,x) * (1-m) - beta_m(t,x) * m

def dh_dt(t,x):
    h = x['h']
    return alpha_h(t,x) * (1-h) - beta_h(t,x) * h

################################## intermediate variables: alphas, betas, stimulus (s), currents (I's), ...


def g_Na(t,x):
    m = x['m']
    h = x['h']
    return g_line_Na * (m ** 3) * h

def g_K(t,x):
    n = x['n']
    return g_line_K * (n ** 4)

def g_L(t,x):
    return g_line_L


def I_Na(t,x):
    V = x['V']
    return g_Na(t,x) * (V - V_Na)

def I_K(t,x):
    V = x['V']
    return g_K(t,x) * (V - V_K)

def I_L(t,x):
    V = x['V']
    return g_L(t,x) * (V - V_L)


def alpha_n(t,x):
    V = x['V']
    return (0.01 * (10 - V)) / (math.exp(0.1 * (10 - V)) - 1)

def beta_n(t,x):
    V = x['V']
    return 0.125 * math.exp(V / -80)


def alpha_m(t,x):
    V = x['V']
    return (0.1 * (25 - V)) / (math.exp(0.1 * (25 - V)) - 1)

def beta_m(t,x):
    V = x['V']
    return 4 * math.exp(V / -18)


def alpha_h(t,x):
    V = x['V']
    return 0.07 * math.exp(V / -20)

def beta_h(t,x):
    V = x['V']
    return 1 / (math.exp(0.1 * (30 - V)) + 1)

def s(t):
    num_ranges = [[10,11], [20,21], [30,40], [50,51], [53,54], [56,57], [59,60], [62,63], [65,66]]
    for num_range in num_ranges:
        if num_range[0] <= t and t <= num_range[1]:
            return 150
    return 0

################################### input into EulerEstimator

derivatives = {
    'V': dV_dt,
    'n': dn_dt,
    'm': dm_dt,
    'h': dh_dt
}

V_0 = 0
t_0 = 0
x_0 = {'V': V_0}

n_0 = (alpha_n(t_0, x_0)) / (alpha_n(t_0, x_0) + beta_n(t_0, x_0))
m_0 = (alpha_m(t_0, x_0)) / (alpha_m(t_0, x_0) + beta_m(t_0, x_0))
h_0 = (alpha_h(t_0, x_0)) / (alpha_h(t_0, x_0) + beta_h(t_0, x_0))

initial_values = {'V': V_0, 'n': n_0, 'm': m_0, 'h': h_0}
initial_point = (t_0, initial_values)

euler = EulerEstimator(derivatives = derivatives)
euler.plot(point=initial_point, step_size=0.01, num_steps=8000, other_functions={'stimulus': s})