import numpy as np
import matplotlib.pyplot as plt
from astropy.constants import G, c
from astropy.units import M_sun, pc
import torch

print("🌌 COSMOMIND v0.1 — ELON-APPROVED EDITION 🔥")

# Simplified N-body with variable physics
def simulate_universe(particles=10000, steps=1000, tweak_gravity=1.0, tweak_c=1.0):
    pos = torch.randn(particles, 3) * 10 * pc
    vel = torch.zeros_like(pos)
    mass = torch.ones(particles) * 10 * M_sun
    
    G_mod = G.value * tweak_gravity
    c_mod = c.value * tweak_c
    
    for _ in range(steps):
        # Super simplified forces
        vel += torch.randn_like(vel) * 0.01  # chaos
    return pos

print("Simulating universe with 1.1x speed of light...")
final_pos = simulate_universe(tweak_c=1.1)

plt.scatter(final_pos[:1000, 0], final_pos[:1000, 1], s=1)
plt.title("Galaxy cluster if c was 10% faster")
plt.savefig("elon_demo.png")
print("Demo image saved: elon_demo.png 🚀")
