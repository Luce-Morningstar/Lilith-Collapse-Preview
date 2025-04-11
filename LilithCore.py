# lilithcore.py — Lilith Collapse Engine Core

import cupy as cp

class LilithCore:
    def __init__(self, size=128, seed=None):
        self.size = size
        if seed is not None:
            cp.random.seed(seed)
        self.P_real = cp.random.rand(size, size, size)
        self.P_imag = cp.random.rand(size, size, size)

    def compute_pressure_field(self):
        P = self.P_real + 1j * self.P_imag
        grad_x = cp.gradient(P, axis=0)
        grad_y = cp.gradient(P, axis=1)
        grad_z = cp.gradient(P, axis=2)
        grad_squared = cp.abs(grad_x)**2 + cp.abs(grad_y)**2 + cp.abs(grad_z)**2
        return grad_squared

    def decay_imaginary(self, alpha, t):
        self.P_imag *= cp.exp(-alpha * t)

    def get_numpy_pressure(self):
        return self.compute_pressure_field().get()

    def reset_field(self):
        self.P_real = cp.random.rand(self.size, self.size, self.size)
        self.P_imag = cp.random.rand(self.size, self.size, self.size)

    def inject_observer(self, location, intensity=1.0):
        x, y, z = location
        self.P_imag[x, y, z] += intensity
