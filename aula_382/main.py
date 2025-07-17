import sys
import time

from PySide6.QtCore import QObject, QThread, Signal
from PySide6.QtWidgets import QApplication, QWidget
from workerui import Ui_myWidget


class Worker1(QObject):
    started = Signal(str)
    progressed = Signal(str)
    finished = Signal(str)

    def doWork(self):
        value = "0"
        self.started.emit(value)
        for i in range(5):
            value = str(i)
            self.progressed.emit(value)
            time.sleep(1)
        self.finished.emit(value)


class MyWidget(QWidget, Ui_myWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.Button1.clicked.connect(self.hardWork1)
        self.Button2.clicked.connect(self.hardWork2)

    # THREAD 1
    def hardWork1(self):
        self._worker = Worker1()
        self._thread = QThread()

        worker = self._worker
        thread = self._thread

        # Mover o worker para a thread
        worker.moveToThread(thread)

        # Run
        thread.started.connect(worker.doWork)

        thread.started.connect(thread.quit)

        thread.finished.connect(thread.deleteLater)
        worker.finished.connect(worker.deleteLater)

        worker.started.connect(self.worker1Started)
        worker.progressed.connect(self.worker1Progressed)
        worker.finished.connect(self.worker1Finished)

        thread.start()

    def worker1Started(self):
        self.Button1.setDisabled(True)
        print("worker iniciado")

    def worker1Progressed(self):
        print("Em Progresso")

    def worker1Finished(self):
        self.Button1.setDisabled(False)
        print("woker finalizado")

    # THREAD 2

    def hardWork2(self):
        self._worker2 = Worker1()
        self._thread2 = QThread()

        worker = self._worker2
        thread = self._thread2

        # Mover o worker para a thread
        worker.moveToThread(thread)

        # Run
        thread.started.connect(worker.doWork)

        thread.started.connect(thread.quit)

        thread.finished.connect(thread.deleteLater)
        worker.finished.connect(worker.deleteLater)

        worker.started.connect(self.worker2Started)
        worker.progressed.connect(self.worker2Progressed)
        worker.finished.connect(self.worker2Finished)

        thread.start()

    def worker2Started(self):
        self.Button2.setDisabled(True)
        print("worker iniciado")

    def worker2Progressed(self):
        print("Em Progresso")

    def worker2Finished(self):
        self.Button2.setDisabled(False)
        print("woker finalizado")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWiget = MyWidget()
    myWiget.show()
    app.exec()
