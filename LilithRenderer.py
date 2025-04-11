# lilithrenderer.py — Collapse Field Frame Renderer

import matplotlib.pyplot as plt
import os
import numpy as np

def render_pressure_slices(pressure_field, output_dir, timestep):
    size = pressure_field.shape[2]  # Assume shape = (x, y, z)
    os.makedirs(output_dir, exist_ok=True)

    for z in range(size):
        plt.figure(figsize=(6, 5))
        plt.imshow(pressure_field[:, :, z], cmap="inferno", origin="lower")
        plt.colorbar(label="|\u2207P|^2")
        plt.title(f"Collapse Pressure z={z}, t={timestep}")
        plt.tight_layout()
        frame_path = os.path.join(output_dir, f"pressure_t{timestep:02d}_z{z:03d}.png")
        plt.savefig(frame_path)
        plt.close()

    print(f"✅ Rendered timestep {timestep} to {output_dir}")
