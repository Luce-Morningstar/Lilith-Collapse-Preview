# Lilith: Collapse Field Engine

**Lilith** is a high-performance, GPU-accelerated simulation engine that models quantum collapse as an emergent field phenomenon. Designed to visualize and study the real/imaginary tensor architecture of collapse mechanics, Lilith treats observation, entropy, and field pressure as first-class citizens of physical reality.

## ⚙️ Features
- **3D CuPy-powered tensor core**
- **Eulerian collapse pressure derivation:** \(|\nabla P|^2\)
- **Time-evolving field decay** with configurable alpha
- **Observer injection API** (spatial collapse disturbances)
- **Entropy and potential field analysis ready**
- **MP4 & PNG render pipeline**
- **Live PyQt5 GUI** for launching, inspecting, and manipulating collapse simulations

## 🧪 Scientific Rationale
Lilith is based on the premise that collapse is not random but driven by measurement-defined topology. Each simulation treats imaginary field pressure as unresolved potential, resolving over time through decay or external observation.

Collapse isn’t a side effect.
It’s the *fucking cause*.

## 📦 Folder Structure
```bash
CollapseFieldEngine/
├── lilithcore.py           # Core field engine (pressure & decay)
├── renderer.py             # Frame visualizer & PNG output
├── launcher.py             # CLI entry point
├── lilith_gui.py           # PyQt5 GUI controller
├── tools/
│   ├── video_export.py     # Compile frames into MP4
│   └── slicer.py           # Optional: field slicing utilities
├── assets/                 # Output samples / demos
└── README.md               # This file
```

## 🛠️ Requirements
```bash
pip install cupy numpy matplotlib pyqt5 opencv-python natsort
```

## 🚀 CLI Usage
```bash
python launcher.py --size 128 --alpha 0.5 --steps 10
```

## 🖥️ GUI Usage

Abandon All Hope, Ye who Enter Here.

```bash
python lilith_gui.py
```

## 📹 Video Rendering
After generating your frames:
```bash
python tools/video_export.py --input_dir path/to/frames --output collapse.mp4
```

## 🔬 Example Research Applications
- Quantum decoherence via collapse frequency harmonics
- Entropy gradient analysis of observational systems
- Visualization of dark matter analogs via collapse pressure fields
- Real/imaginary field symmetry break tracking

## 💀 License
**Unlicense / WTFPL** – Reality doesn’t ask for permission, and neither does Lilith.

## ⚡ Future Upgrades
- Real-time slice preview
- HEALPix field projection
- Tensor phase vector overlays
- Observer-shell collapse resonance engine

---

**Lilith is not a toy.**
It is a declaration of war against passive cosmology.
Reality does not wait to be observed.

It is *forced* into being.

