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
        self.logger = logging.getLogger()  # Logger maintainer
        self.logger.setLevel(logging.DEBUG)

        # connections
        for key in self.piano_keys + self.guitar_keys:
            key.clicked.connect(partial(self.play, key.property("key_number")))

    def play(self, key):
        """
        Main Sound Generation function.

        :param key: Key number that is passed to the equation
                    to generate freq.
        """
        try:
            freq = syn.key_freq(key)
            # Piano
            if self.tabWidget.currentIndex() == 1:
                self.logger.debug("Currently playing piano key: %s" % key)
                self.statusbar.showMessage("Playing key: %s freq: %s Hz" % (key, round(freq, 2)))
                syn.play_sound(syn.piano_note(freq), self.rate)

            # Guitar
            if self.tabWidget.currentIndex() == 0:
                self.logger.debug("Currently playing note %s " % key)
                self.statusbar.showMessage("Playing guitar note: %s  freq: %s Hz" % (key, round(freq, 2)))
                syn.play_sound(syn.karplus_strong(syn.create_wave_table(self.rate, freq), self.rate),
                               self.rate)
        except :
            # This is a dead case where the the sound card is not
            # responding to the console, this may be produced by another
            # program that is currently using the card (slave) which is
            # preventing the console from playing the sound.
            #
            # This is just to ensure application`s smooth performance
            # closing or waiting a few seconds for card to respond is the
            # solution for this kind of problem

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
