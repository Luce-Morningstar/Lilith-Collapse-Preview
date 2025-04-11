# renderer.py — Collapse Field Frame Renderer with Video Export

import matplotlib.pyplot as plt
import os
import numpy as np
import cv2
from natsort import natsorted

def render_pressure_slices(pressure_field, output_dir, timestep, export_video=False, fps=10):
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

    if export_video:
        export_to_video(output_dir, os.path.join(output_dir, "collapse_output.mp4"), fps)


def export_to_video(folder, output_path="collapse_output.mp4", fps=10):
    images = natsorted([f for f in os.listdir(folder) if f.endswith(".png")])
    if not images:
        print("❌ No PNG frames found for video export.")
        return

    first_frame = cv2.imread(os.path.join(folder, images[0]))
    height, width, _ = first_frame.shape
    out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

    for img in images:
        frame = cv2.imread(os.path.join(folder, img))
        out.write(frame)

    out.release()
    print(f"🎥 MP4 video exported to {output_path}")
