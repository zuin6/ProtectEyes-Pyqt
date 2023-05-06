# -*- coding: utf-8 -*-
import sys

from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QIcon, QColor
from PyQt5.QtWidgets import QSystemTrayIcon, QMainWindow, QApplication, QMenu, QAction, QLabel, QPushButton

from Setting import Setting
from Brightness import setBrightness
from protectEyes import ProtectEye


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # 图标修改
        import ctypes
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")
        self.runTime = 1
        self.isRelaxFlag = False
        self.relaxTime = 5
        self.workTime = 60
        self.setWindowTitle("小助手")
        self.showProtectEys()
        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.addRunTime)
        self.setWindowTitle("小助手")
        # 设置
        self.settingButton = QPushButton(self)
        self.settingButton.setText("亮度调整")
        self.settingButton.clicked.connect(self.show_ScreenBrightView)
        self.settingButton.setGeometry(740, 570, 60, 30)
        self.resize(800, 600)
        self.setWindowIcon(QIcon("logo.ico"))

        # 创建托盘图标
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon("logo.ico"))  # 设置图标
        self.tray_icon.setToolTip("小助手")  # 设置提示信息
        self.tray_icon.activated.connect(self.on_tray_icon_activated)  # 设置点击事件
        self.tray_icon.show()  # 显示托盘图标
        # 创建一个QMenu对象
        self.menu = QMenu()
        self.initMenu()


    def show_ScreenBrightView(self):
        self.settingView.show()
        pass

    def on_tray_icon_activated(self, reason):
        # 点击托盘图标时的响应
        if reason == QSystemTrayIcon.Trigger:  # 单击左键
            if self.isHidden():  # 如果窗口隐藏了，就显示出来
                self.show()
            else:  # 如果窗口显示了，就隐藏起来
                self.hide()

    #
    def addRunTime(self):
        # print(60 * self.workTime)
        # print(60 * self.relaxTime)
        print(self.runTime)
        if self.isRelaxFlag and self.runTime % (self.relaxTime * 60) == 0:
            self.isRelaxFlag = False
            self.runTime = 0
            self.protectEye.hide()
        elif self.runTime % (self.workTime * 60) == 0:
            self.protectEye.show()
            self.isRelaxFlag = True
            self.runTime = 0
        self.runTime = self.runTime + 1

    def showProtectEys(self):
        self.protectEye = ProtectEye()

    #
    def chooseWorkTime1(self):
        self.workTime = 60
        self.refreshMenu()

    def chooseWorkTime2(self):
        self.workTime = 120
        self.refreshMenu()

    def chooseRelaxTime1(self):
        self.relaxTime = 5
        self.refreshMenu()

    def chooseRelaxTime2(self):
        self.relaxTime = 15
        self.refreshMenu()

    # 退出程序
    def closeApp(self):
        QApplication.quit()

    def refreshMenu(self):
        self.menu.clear()
        # 添加一些菜单项
        self.liveTime1 = QAction("活力时间1小时")
        if self.workTime == 60:
            self.liveTime1.setIcon(QIcon("checked.png"))
        self.liveTime1.triggered.connect(self.chooseWorkTime1)
        self.menu.addAction(self.liveTime1)

        self.liveTime2 = QAction("活力时间2小时")
        if self.workTime == 120:
            self.liveTime2.setIcon(QIcon("checked.png"))
        self.liveTime2.triggered.connect(self.chooseWorkTime2)
        self.menu.addAction(self.liveTime2)

        self.relaxTime1 = QAction("休息时间5分钟")
        if self.relaxTime == 5:
            self.relaxTime1.setIcon(QIcon("checked.png"))
        self.relaxTime1.triggered.connect(self.chooseRelaxTime1)
        self.menu.addAction(self.relaxTime1)

        self.relaxTime2 = QAction("休息时间15分钟")
        if self.relaxTime == 15:
            self.relaxTime2.setIcon(QIcon("checked.png"))
        self.relaxTime2.triggered.connect(self.chooseRelaxTime2)
        self.menu.addAction(self.relaxTime2)

        self.exitAction = QAction("退出")
        self.exitAction.triggered.connect(self.closeApp)
        self.menu.addAction(self.exitAction)
        # 设置托盘图标的上下文菜单
        self.tray_icon.setContextMenu(self.menu)

    #
    def createMenu(self):
        # 添加一些菜单项
        self.liveTime1 = QAction("活力时间1小时")
        if self.workTime == 60:
            self.liveTime1.setIcon(QIcon("checked.png"))
        self.liveTime1.triggered.connect(self.chooseWorkTime1)
        self.menu.addAction(self.liveTime1)

        self.liveTime2 = QAction("活力时间2小时")
        if self.workTime == 120:
            self.liveTime2.setIcon(QIcon("checked.png"))
        self.liveTime2.triggered.connect(self.chooseWorkTime2)
        self.menu.addAction(self.liveTime2)

        self.relaxTime1 = QAction("休息时间5分钟")
        if self.relaxTime == 5:
            self.relaxTime1.setIcon(QIcon("checked.png"))
        self.relaxTime1.triggered.connect(self.chooseRelaxTime1)
        self.menu.addAction(self.relaxTime1)

        self.relaxTime2 = QAction("休息时间15分钟")
        if self.relaxTime == 15:
            self.relaxTime2.setIcon(QIcon("checked.png"))
        self.relaxTime2.triggered.connect(self.chooseRelaxTime2)
        self.menu.addAction(self.relaxTime2)

        self.exitAction = QAction("退出")
        self.exitAction.triggered.connect(self.closeApp)
        self.menu.addAction(self.exitAction)
        # 设置托盘图标的上下文菜单
        self.tray_icon.setContextMenu(self.menu)

    def initMenu(self):
        self.createMenu()
        self.settingView = Setting()

    def closeEvent(self, event):
        # 重写关闭事件，使窗口关闭时最小化到托盘
        self.hide()  # 隐藏窗口
        event.ignore()  # 忽略关闭事件

    # def showEvent(self, event):
    #     # 重写显示事件，使窗口显示时不在任务栏显示
    #     event.accept()  # 接受显示事件
    #     self.setWindowFlags(Qt.Tool)  # 设置窗口标志为工具类型，不在任务栏显示


# 主程序
if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = MainWindow()
    # MainWindow.show()
    sys.exit(app.exec_())
