import mainUI as ui
from PyQt5 import QtWidgets, QtGui
import logging
from functools import partial
import Synthesis as syn


class Instruments (ui.Ui_MainWindow):
    """
    Synthetic Instruments.
    An application that synthesis some of the basic
    musical instruments that ever existed.

    ================================================

    **includes**

    - Guitar (basic)
    - Grand Piano (17 Keys)

    ================================================
    """
    def __init__(self, starter_window):
        super(Instruments, self).setupUi(starter_window)
        self.piano_keys = [widget for widget in self.tab_2.children() if isinstance(widget, QtWidgets.QPushButton)]
        self.guitar_keys = [widget for widget in self.tab.children() if isinstance(widget, QtWidgets.QPushButton)]
        self.rate = 44100

        # connections
        for key in self.piano_keys + self.guitar_keys:
            key.clicked.connect(partial(self.play, key.property("key_number")))

    def play(self, key):
        try:
            # Piano
            if self.tabWidget.currentIndex() == 1:
                syn.play_sound(syn.piano_note(syn.key_freq(key)), self.rate)

            # Guitar
            if self.tabWidget.currentIndex() == 0:
                syn.play_sound(syn.karplus_strong(syn.create_wave_table(self.rate, syn.key_freq(key)), self.rate),
                               self.rate)
        except :
            pass


if __name__ == '__main__':
    import sys
    logging.basicConfig(filename="logs/logfile.log",
                        format='%(asctime)s %(message)s',
                        filemode='w')

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Instruments(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
