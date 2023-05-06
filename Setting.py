from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QLabel, QWidget

from BrightSetting_UI import Ui_Form
from Brightness import setBrightness


class Setting(QWidget, Ui_Form):
    def __init__(self):
        super(Setting, self).__init__()
        self.uiForm = Ui_Form()
        self.uiForm.setupUi(self)
        self.uiForm.horizontalSlider.valueChanged.connect(self.setBright)
        self.uiForm.horizontalSlider.setValue(0)

    def setBright(self):
        self.uiForm.label_2.setText(str(self.uiForm.horizontalSlider.value()))
        setBrightness(self.uiForm.horizontalSlider.value())
