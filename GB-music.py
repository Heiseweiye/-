from PyQt5.QtWidgets import QApplication, QWidget
from GB_music.GUI.D_Display import Main_window
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Main_window()
    ui.show()
    sys.exit(app.exec_())