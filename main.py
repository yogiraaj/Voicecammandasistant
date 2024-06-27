from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from myfrndgui import Ui_leoGui

# ... Your other code ...

class YourApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_leoGui()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)
        self.ui.pushButton_3.clicked.connect(self.openLink)

    def openLink(self):
        
        url = QUrl("https://speechto2text.netlify.app")
        QDesktopServices.openUrl(url)
                

# ... The rest of your code ...

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = YourApp()
    main_window.show()
    sys.exit(app.exec_())