'''from __future__ import division
from sympy import *

x, y, z = symbols('x y z')
init_printing(use_unicode=True)

print(diff(cos(x), x))
'''

# -*- coding: utf-8 -*-
from __future__ import division

import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import InterpolatedUnivariateSpline
from scipy.interpolate import splrep, splder, splev

## Useful Links
## https://stackoverflow.com/questions/9876290/how-do-i-compute-derivative-using-numpy
## https://stackoverflow.com/questions/42197460/numpy-diff-and-scipy-fftpack-diff-giving-different-results-when-differentiat
## ## https://stackoverflow.com/questions/42197460/numpy-diff-and-scipy-fftpack-diff-giving-different-results-when-differentiat

x = np.linspace(0, 1, 361)

# Create sin wave values
sin = np.sin(np.radians(np.linspace(0, 361, 361)))

# Create cosine wave values
cos = np.cos(np.radians(np.linspace(0, 361, 361)))

# Create scale factor for derivative values
scale = 6

## Method 1
# Get a function that evaluates the linear spline at any x
f = InterpolatedUnivariateSpline(x, sin, k=3)

# Get a function that evaluates the derivative of the linear spline at any x
dfdx = f.derivative()

# Evaluate the derivative dydx at each x location...
dydx_1_no_scaled = dfdx(x)
dydx_1_scaled = dfdx(x) / scale

## Method 2
# Calculate time step
dx = x[1] - x[0]

# Gradient method :  central differences
dydx_2_no_scaled = (np.gradient(sin, dx))
dydx_2_scaled = (np.gradient(sin, dx)) / 6

## Method 3
# Approximations of derivatives
dydx_3_no_scaled = (np.diff(sin) / np.diff(x))
dydx_3_scaled = (np.diff(sin) / np.diff(x)) / 6

# Method 4 : Spline
time = np.linspace(0, 1, 361)

# Calculate signal spline func 'tck'
func = splrep(time, sin, s=0, k=3)

# Calculate derivative spline func 'tck'
der_func = splder(func, n=1)

# Calculate derivative values
dydx_4_no_scaled = splev(x, der_func, der=0, ext=0)
dydx_4_scaled = splev(x, der_func, der=0, ext=0) / 6

plt.plot(sin)
plt.plot(cos)
plt.plot(dydx_1_no_scaled)
plt.plot(dydx_1_scaled)
plt.plot(dydx_2_no_scaled)
plt.plot(dydx_2_scaled)
plt.plot(dydx_3_no_scaled)
plt.plot(dydx_3_scaled)
plt.plot(dydx_4_no_scaled)
plt.plot(dydx_4_scaled)
plt.axvline(90)
plt.axvline(180)
plt.axvline(270)
plt.title('Sine Wave and respective derivative with 4 different methods')
plt.legend(['sin',
            'cos',
            'dydx_1_no_scaled', 'dydx_1_scaled',
            'dydx_2_no_scaled', 'dydx_2_scaled',
            'dydx_3_no_scaled', 'dydx_3_scaled',
            'dydx_4_no_scaled', 'dydx_4_scaled'])
plt.show()
