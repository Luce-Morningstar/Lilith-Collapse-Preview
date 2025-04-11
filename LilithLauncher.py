# launcher.py — Entry point for Lilith Collapse Engine

import argparse
import os
from datetime import datetime
import matplotlib.pyplot as plt
from lilithcore import LilithCore
from lilithrenderer import render_pressure_slices

def run_simulation(size, alpha, timesteps):
    output_dir = f"lilith_output_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    os.makedirs(output_dir, exist_ok=True)

    engine = LilithCore(size=size)

    for t in range(timesteps):
        engine.decay_imaginary(alpha, t)
        pressure = engine.get_numpy_pressure()
        render_pressure_slices(pressure, output_dir, t)

    print(f"✅ Lilith run complete. Output saved to {output_dir}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="🔥 Lilith Collapse Engine Launcher")
    parser.add_argument("--size", type=int, default=128, help="Grid size (default: 128)")
    parser.add_argument("--alpha", type=float, default=0.5, help="Collapse decay rate (default: 0.5)")
    parser.add_argument("--steps", type=int, default=10, help="Number of timesteps (default: 10)")

    args = parser.parse_args()
    run_simulation(args.size, args.alpha, args.steps)
