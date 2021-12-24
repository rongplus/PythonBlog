import os

from PyQt5 import QtQuick, QtCore, QtQml

class MainView(QtQuick.QQuickView):

    def __init__(self):
        QtQuick.QQuickView.__init__(self)
        self.setResizeMode(QtQuick.QQuickView.ResizeMode.SizeRootObjectToView)
        self.setFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        self.engine().quit.connect(QtCore.QCoreApplication.quit)
        self.rootContext().setContextProperty("MainView", self)
        self.setSource(QtCore.QUrl("aa.qml"))
        self.show()
		
		