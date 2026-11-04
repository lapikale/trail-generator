import importlib

from PySide6 import QtWidgets, QtCore

import trailgen
importlib.reload(trailgen)
from trailgen import StepStones

# StepStones:
# individual stone rotate
# individuale stone depth+width (scale)
# group rotate

class StepStonesGUI(QtWidgets.QDialog):

    def __init__(self):
            super().__init__()
            self.step_stones = StepStones()
            self.setWindowTitle("Generate a Trail!")
            self.create_layout()

    def create_layout(self):
            self.main_lay = QtWidgets.QVBoxLayout()
            self._form_ui()
            self.create_btn = QtWidgets.QPushButton("Create")
            self.main_lay.addWidget(self.create_btn)
            self.setLayout(self.main_lay)

    def _form_ui(self):
            self.form_lay = QtWidgets.QFormLayout()
            self.main_lay.addLayout(self.form_lay)

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