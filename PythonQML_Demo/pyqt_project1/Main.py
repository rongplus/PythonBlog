from PyQt5 import QtQuick, QtCore, QtQml
from PyQt5.QtGui import QGuiApplication
import PyQt5.QtGui
from PyQt5.QtQml import QQmlApplicationEngine
import multiprocessing
from PyQt5.QtGui import QIcon
import time
import threading
import json
import os
import sys
# app = QGuiApplication([])
# print("==log:=list =", self.catalogueProductList)
# with open('result.txt', 'w') as outfile:
#    json.dump(result, outfile)


class Singleton(object):
    lock = threading.Lock()
    _instance = None
    lv = None

    @classmethod
    def instance(cls):
        with cls.lock:
            if not cls._instance:
                print("creating new class of " + cls.__name__)
                cls._instance = cls()

        return cls._instance

    @classmethod
    def getMain(self):
        self.win = MainView()
        self.win.show()
        return self.win

    @classmethod
    def getOderView(self):
        self.orderWin = OrderView()
        self.win.show()
        return self.win


class TaskThread(QtCore.QThread):
    taskFinished = QtCore.pyqtSignal()

    def run(self):
        time.sleep(5)
        self.taskFinished.emit()


class MainView(QtQuick.QQuickView):
    def __init__(self):
        QtQuick.QQuickView.__init__(self)
        # self.CurrentAppInstance = App.GetCurrentInstance()
        self.rootContext().setContextProperty("mainView", self)
        self.setSource(QtCore.QUrl("MainWindow.qml"))
        self.engine().quit.connect(QtCore.QCoreApplication.quit)
        self.orderWin = OrderView()
        # self.orderWin.setParent(self) # will put the window into parent

        self.myLongTask = TaskThread()
        self.myLongTask.taskFinished.connect(self.onFinished)

    @QtCore.pyqtSlot(int)
    def onStart(self, index):
        #self.progressBar.setRange(0, 0)
        self.setMouseGrabEnabled(False)
        self.orderWin.show()
        self.enabled = False
        self.hide()

        # grab_set()

        self.myLongTask.start()

    def onFinished(self):
        self.orderWin.hide()
        # self.setMouseGrabEnabled(True)
        win = self.rootObject()
        win.displayNumber()

        self.show()
        # Stop the pulsation
        #self.progressBar.setRange(0, 1)

        # Create a progress bar and a button and add them to the main layout
        #self.progressBar = QProgressBar(self)
        #self.progressBar.setRange(0, 1)

    @QtCore.pyqtSlot(int)
    def showOrders(self, index):
        print("Show Orders")
        self.orderWin.show()


class OrderView(QtQuick.QQuickView):
    def __init__(self):
        QtQuick.QQuickView.__init__(self)
        # self.CurrentAppInstance = App.GetCurrentInstance()
        self.rootContext().setContextProperty("MainView", self)
        self.setSource(QtCore.QUrl("OrderView.qml"))
        self.setFlag(QtCore.Qt.WindowType.FramelessWindowHint)


if __name__ == '__main__':
    multiprocessing.freeze_support()

    app = QGuiApplication(sys.argv)
    ss = Singleton()
    ss.getMain()
    app.exec_()
