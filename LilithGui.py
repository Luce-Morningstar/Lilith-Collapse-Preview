# lilith_gui.py — Lilith Collapse Engine GUI (PyQt5)

import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout,
    QSpinBox, QDoubleSpinBox, QFileDialog, QTextEdit, QCheckBox
)
from PyQt5.QtCore import Qt
from launcher import run_simulation

class LilithGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lilith: Collapse Engine GUI")
        self.setGeometry(100, 100, 400, 460)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Grid size
        size_layout = QHBoxLayout()
        size_label = QLabel("Grid Size:")
        self.size_spin = QSpinBox()
        self.size_spin.setRange(32, 512)
        self.size_spin.setValue(128)
        size_layout.addWidget(size_label)
        size_layout.addWidget(self.size_spin)

        # Alpha
        alpha_layout = QHBoxLayout()
        alpha_label = QLabel("Decay Rate (alpha):")
        self.alpha_spin = QDoubleSpinBox()
        self.alpha_spin.setRange(0.01, 5.0)
        self.alpha_spin.setSingleStep(0.05)
        self.alpha_spin.setValue(0.5)
        alpha_layout.addWidget(alpha_label)
        alpha_layout.addWidget(self.alpha_spin)

        # Time steps
        step_layout = QHBoxLayout()
        step_label = QLabel("Time Steps:")
        self.step_spin = QSpinBox()
        self.step_spin.setRange(1, 100)
        self.step_spin.setValue(10)
        step_layout.addWidget(step_label)
        step_layout.addWidget(self.step_spin)

        # Observer injection
        observer_layout = QHBoxLayout()
        observer_layout.addWidget(QLabel("Inject Observer at X:"))
        self.obs_x = QSpinBox()
        self.obs_x.setRange(0, 512)
        observer_layout.addWidget(self.obs_x)

        observer_layout.addWidget(QLabel("Y:"))
        self.obs_y = QSpinBox()
        self.obs_y.setRange(0, 512)
        observer_layout.addWidget(self.obs_y)

        observer_layout.addWidget(QLabel("Z:"))
        self.obs_z = QSpinBox()
        self.obs_z.setRange(0, 512)
        observer_layout.addWidget(self.obs_z)

        self.inject_button = QPushButton("Inject Observer")
        self.inject_button.clicked.connect(self.inject_observer)
        observer_layout.addWidget(self.inject_button)

        # Live preview toggle
        preview_layout = QHBoxLayout()
        self.preview_check = QCheckBox("Enable Live Preview (slower)")
        self.preview_check.setChecked(False)
        preview_layout.addWidget(self.preview_check)

        # Status display
        output_path_layout = QHBoxLayout()
        self.output_label = QLabel("Output Dir: Not yet generated")
        self.browse_button = QPushButton("Browse Output")
        self.browse_button.clicked.connect(self.browse_output)
        output_path_layout.addWidget(self.output_label)
        output_path_layout.addWidget(self.browse_button)

        self.status_display = QTextEdit()
        self.status_display.setReadOnly(True)

        # Launch button
        self.run_button = QPushButton("Run Lilith")
        self.run_button.clicked.connect(self.run_lilith)

        layout.addLayout(size_layout)
        layout.addLayout(alpha_layout)
        layout.addLayout(step_layout)
        layout.addLayout(observer_layout)
        layout.addLayout(preview_layout)
        layout.addWidget(self.run_button)
        layout.addLayout(output_path_layout)
        layout.addWidget(QLabel("Output Console:"))
        layout.addWidget(self.status_display)

        self.setLayout(layout)

    def run_lilith(self):
        size = self.size_spin.value()
        alpha = self.alpha_spin.value()
        steps = self.step_spin.value()
        live_preview = self.preview_check.isChecked()

        self.status_display.append(f"\n🩸 Running Lilith...\nGrid: {size}³ | Alpha: {alpha} | Steps: {steps} | Preview: {live_preview}")
        try:
            output_dir = run_simulation(size, alpha, steps)  # Add return to launcher.py
            self.status_display.append("✅ Lilith run complete.")
            self.output_label.setText(f"Output Dir: {output_dir}")
        except Exception as e:
            self.status_display.append(f"💀 Error: {e}")

    def inject_observer(self):
        x, y, z = self.obs_x.value(), self.obs_y.value(), self.obs_z.value()
        self.status_display.append(f"🔬 Injected observer at: ({x}, {y}, {z})")
        # NOTE: Hook this into your collapse engine to actually insert the observer

    def browse_output(self):
        directory = QFileDialog.getExistingDirectory(self, "Select Output Directory")
        if directory:
            self.output_label.setText(f"Output Dir: {directory}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LilithGUI()
    window.show()
    sys.exit(app.exec_())
