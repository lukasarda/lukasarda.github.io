"""Generates the decorative picture behind the name on the home page.

A zoom-whirl orbit around a Schwarzschild black hole (G = c = M = 1), from
Darwin's exact parametrisation of bound geodesics:
    r(chi) = p / (1 + e cos chi),
    dphi/dchi = sqrt(p / (p - 6 - 2 e cos chi)).
With p just above the separatrix p = 6 + 2e the orbit whirls around the hole
at each periapsis. The orbital plane is shown inclined, so the orbit reads as
a horizontal band across the header.

Regenerate with:   python3 scripts/hero-pattern.py > assets/hero-pattern.svg
Needs numpy only.
"""

import numpy as np

P, E = 7.62, 0.8          # semi-latus rectum and eccentricity (separatrix: 6 + 2e = 7.6)
N_RADIAL = 7              # radial periods drawn
INCLINATION = 68.0        # viewing angle from the orbital axis, degrees
WIDTH, HEIGHT = 1600, 900

chi = np.linspace(0.0, 2.0 * np.pi * N_RADIAL, 40000)
dphi = np.sqrt(P / (P - 6.0 - 2.0 * E * np.cos(chi)))
phi = np.concatenate([[0.0], np.cumsum(0.5 * (dphi[1:] + dphi[:-1]) * np.diff(chi))])
r = P / (1.0 + E * np.cos(chi))

x = r * np.cos(phi)
y = r * np.sin(phi) * np.cos(np.radians(INCLINATION))

scale = 0.46 * WIDTH / (P / (1.0 - E))
cx, cy = WIDTH / 2, HEIGHT / 2
X, Y = cx + scale * x, cy - scale * y

# Fade the older loops: split into one polyline per radial period.
segments = np.array_split(np.arange(len(chi)), N_RADIAL)
print(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {HEIGHT}">')
for k, idx in enumerate(segments):
    idx = idx[::4]
    points = " ".join(f"{X[i]:.1f},{Y[i]:.1f}" for i in idx)
    opacity = 0.25 + 0.75 * (k + 1) / N_RADIAL
    print(f'  <polyline points="{points}" fill="none" stroke="#ffffff" '
          f'stroke-width="1.6" stroke-opacity="{opacity:.2f}"/>')
print(f'  <ellipse cx="{cx}" cy="{cy}" rx="{2 * scale:.1f}" ry="{2 * scale:.1f}" fill="#00112e"/>')
print(f'  <circle cx="{cx}" cy="{cy}" r="{3 * scale:.1f}" fill="none" stroke="#ffffff" '
      f'stroke-width="1" stroke-opacity="0.35" stroke-dasharray="4 6"/>')
print("</svg>")
