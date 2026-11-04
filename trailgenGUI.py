import importlib

from PySide6 import QtWidgets, QtCore

import trailgen
importlib.reload(trailgen)
from trailgen import StepStones

# different tabs for different models

# StepStones:
# individual stone rotate
# individuale stone depth+width (scale)
# group rotate

class StepStonesGUI(QtWidgets.QDialog):

    def __init__(self):
            super().__init__()
            self.ss_gen = StepStones()
            self.setWindowTitle("Generate a Trail!")
            self.create_layout()
            self.create_connections()

    def create_layout(self):
            self.main_lay = QtWidgets.QVBoxLayout()
            self._form_ui()
            self.create_btn = QtWidgets.QPushButton("Create")
            self.main_lay.addWidget(self.create_btn)
            self.setLayout(self.main_lay)

    def _form_ui(self):
            self.form_lay = QtWidgets.QFormLayout()
            self._grp_rotate()
            self.main_lay.addLayout(self.form_lay)

    def _grp_rotate(self):
            self.grp_rotate_slider = QtWidgets.QSlider()
            self.grp_rotate_slider.setValue(0.5)
            self.form_lay.addRow("Rotate", self.grp_rotate_slider)
    
    def create_connections(self):
            self.create_btn.clicked.connect(self.create)
    
    @QtCore.Slot()
    def create(self):
        self.ss_gen.ss_rotate = self.grp_rotate_slider.value()
        self.ss_gen.create()

# Trees:
# toggle between type of tree
# group scale
# group rotate
# individual trunk height

# Fence:
# individual plank rotation
# group rotation
# group depth (length)

# Flower:
# group scale
# group rotate