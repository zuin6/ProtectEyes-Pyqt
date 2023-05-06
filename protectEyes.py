import time
from ctypes.wintypes import HWND

from PyQt5 import QtCore
from PyQt5.QtCore import Qt, QTimer, pyqtSignal
from PyQt5.QtWidgets import QWidget, QLabel
from win32con import HWND_TOPMOST, SWP_NOMOVE, SWP_NOSIZE


class ProtectEye(QWidget):
    # 重新计时信号
    restartTime = pyqtSignal(int)

    def __init__(self, parent=None):
        super(ProtectEye, self).__init__(parent)
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.Tool | QtCore.Qt.WindowStaysOnTopHint)
        self.setStyleSheet("background-color:transparent;")
        self.showFullScreen()
        self.hide()

