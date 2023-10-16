import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

class SimpleWebBrowser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://www.google.com"))  # URL inicial

        self.setCentralWidget(self.browser)

def main():
    app = QApplication(sys.argv)
    
    # Definir uma fonte padrão para o aplicativo (no exemplo, "Arial")
    font = app.font()
    font.setFamily("Arial")
    app.setFont(font)

    window = SimpleWebBrowser()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
