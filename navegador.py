import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolBar, QLineEdit, QAction
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

class ImprovedWebBrowser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://www.google.com"))

        self.setCentralWidget(self.browser)

        # Adicione uma barra de pesquisa e um botão "Pesquisar"
        navtb = QToolBar("Navigation")
        self.addToolBar(navtb)

        self.urlbar = QLineEdit()
        self.urlbar.returnPressed.connect(self.navigate_to_url)
        navtb.addWidget(self.urlbar)

        search_action = QAction("Pesquisar", self)
        search_action.setStatusTip("Pesquisar na web")
        search_action.triggered.connect(self.navigate_to_url)
        navtb.addAction(search_action)

    def navigate_to_url(self):
        q = QUrl(self.urlbar.text())
        if q.scheme() == "":
            q.setScheme("http")
        self.browser.setUrl(q)

def main():
    app = QApplication(sys.argv)
    window = ImprovedWebBrowser()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
