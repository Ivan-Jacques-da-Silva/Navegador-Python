# Navegador-Python

Navegador simples desenvolvido em Python.
Esse Navegador fui realizando aos poucos, estudando mais ou menos o que cada compenente faz, também usei auxilio de ferramente como ChatGPT para corrigir erros que com o tempo encontrei.

# Explicação de cada passo do código

Claro, vou explicar o código sem usar blocos de código:

1. `import sys`: Importa o módulo `sys`, que é usado para interagir com o sistema operacional.

2. `from PyQt5.QtWidgets import QApplication, QMainWindow, QToolBar, QLineEdit, QAction`: Importa várias classes e widgets da biblioteca PyQt5. Isso inclui `QApplication` para criar a instância da aplicação, `QMainWindow` para a janela principal, `QToolBar` para uma barra de ferramentas, `QLineEdit` para a barra de pesquisa e `QAction` para criar uma ação (como o botão "Pesquisar").

3. `from PyQt5.QtWebEngineWidgets import QWebEngineView`: Importa a classe `QWebEngineView` do módulo `QtWebEngineWidgets`. Essa classe permite exibir conteúdo da web.

4. `from PyQt5.QtCore import QUrl`: Importa a classe `QUrl` do módulo `QtCore`, que é usada para lidar com URLs.

5. `class ImprovedWebBrowser(QMainWindow):`: Define uma nova classe chamada `ImprovedWebBrowser` que herda da classe `QMainWindow`. Essa classe representa a janela do navegador.

6. `def __init__(self):`: Define o método `__init__`, que é o construtor da classe. Esse método é executado quando uma instância da classe é criada.

7. `super().__init__()`: Chama o construtor da classe pai (`QMainWindow`) para inicializar a janela principal.

8. `self.browser = QWebEngineView()`: Cria uma instância de `QWebEngineView`, que é usada para exibir o conteúdo da web.

9. `self.browser.setUrl(QUrl("http://www.google.com"))`: Define a URL inicial que o navegador irá carregar, neste caso, "http://www.google.com".

10. `self.setCentralWidget(self.browser)`: Define o widget central da janela como o `QWebEngineView`, tornando-o o conteúdo principal da janela.

11. `navtb = QToolBar("Navigation")`: Cria uma barra de ferramentas chamada "Navigation" para adicionar elementos nela.

12. `self.addToolBar(navtb)`: Adiciona a barra de ferramentas à janela.

13. `self.urlbar = QLineEdit()`: Cria uma barra de pesquisa (um widget `QLineEdit`) para inserir URLs ou termos de pesquisa.

14. `self.urlbar.returnPressed.connect(self.navigate_to_url)`: Conecta o evento "returnPressed" da barra de pesquisa à função `navigate_to_url`.

15. `navtb.addWidget(self.urlbar)`: Adiciona a barra de pesquisa à barra de ferramentas.

16. `search_action = QAction("Pesquisar", self)`: Cria uma ação chamada "Pesquisar" que será usada como o botão "Pesquisar". Conecta a ação à função `navigate_to_url`.

17. `search_action.setStatusTip("Pesquisar na web")`: Define uma dica de status para a ação.

18. `navtb.addAction(search_action)`: Adiciona a ação (botão "Pesquisar") à barra de ferramentas.

19. `def navigate_to_url(self):`: Define a função `navigate_to_url`, que é chamada quando o usuário pressiona "Enter" na barra de pesquisa ou clica no botão "Pesquisar".

20. `q = QUrl(self.urlbar.text())`: Obtém o texto da barra de pesquisa.

21. `if q.scheme() == "":`: Verifica se a URL não possui um esquema especificado (por exemplo, "http://").

22. `q.setScheme("http")`: Define o esquema como "http" se não estiver especificado.

23. `self.browser.setUrl(q)`: Navega para a URL especificada no `QWebEngineView`.

24. `def main():`: Define a função `main()`, que será a função principal do aplicativo.

25. `app = QApplication(sys.argv)`: Cria uma instância da classe `QApplication`, que é necessária para iniciar a GUI do aplicativo e gerenciar o ciclo de vida.

26. `window = ImprovedWebBrowser()`: Cria uma instância da classe `ImprovedWebBrowser`, que é a janela do navegador.

27. `window.show()`: Exibe a janela do navegador.

28. `sys.exit(app.exec_())`: Inicia o loop de eventos da aplicação, mantendo o aplicativo em execução até que o usuário feche a janela.

29. `if __name__ == "__main__":`: Verifica se o script está sendo executado como o programa principal.

30. `main()`: Chama a função `main()` para iniciar o aplicativo.

Com essas modificações, o código cria um navegador web com uma barra de pesquisa e um botão "Pesquisar" para melhorar a funcionalidade. O usuário

 pode inserir URLs ou termos de pesquisa na barra de pesquisa e navegar na web ao pressionar "Enter" ou clicar no botão "Pesquisar".