from PyQt5 import QtQuick, QtCore, QtQml
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtGui import QIcon
import json
import os
import sys
#app = QGuiApplication([])


class MainView(QtQuick.QQuickView):
    def __init__(self):
        QtQuick.QQuickView.__init__(self)
        # self.CurrentAppInstance = App.GetCurrentInstance()
        self.rootContext().setContextProperty("MainView", self)
        self.setSource(QtCore.QUrl("MainWindow.qml"))
        self.engine().quit.connect(QtCore.QCoreApplication.quit)


def runQML():
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    app.setWindowIcon(QIcon("icon.png"))
    engine.load('MainWindow.qml')

    if not engine.rootObjects():
        return -1

    return app.exec_()


if __name__ == '__main__':

    sys.exit(runQML())
