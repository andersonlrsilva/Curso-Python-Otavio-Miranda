from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLineEdit
from variables import BIG_FONTE_SIZE, MINIMUM_WIDTH, TEXT_MARGIN


class Display (QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        # margins = [TEXT_MARGIN for _ in range(4)]
        self.setStyleSheet(f'font-size:{BIG_FONTE_SIZE}px;')
        self.setMinimumHeight(BIG_FONTE_SIZE * 2)
        self.setMinimumWidth(MINIMUM_WIDTH)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(* [TEXT_MARGIN for _ in range(4)])

    def key
