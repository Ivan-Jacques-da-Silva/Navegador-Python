# Navegador-Python

Navegador simples desenvolvido em Python.
Esse Navegador fui realizando aos poucos, estudando mais ou menos o que cada compenente faz, também usei auxilio de ferramente como ChatGPT para corrigir erros que com o tempo encontrei.

# Explicação de cada passo do código

1. `import sys`: Importa o módulo `sys`, que é usado para interagir com o sistema operacional.

2. `from PyQt5.QtWidgets import QApplication, QMainWindow`: Importa as classes `QApplication` e `QMainWindow` do módulo `QtWidgets`, que fazem parte da biblioteca PyQt5 e são usadas para criar a interface gráfica do usuário.

3. `from PyQt5.QtWebEngineWidgets import QWebEngineView`: Importa a classe `QWebEngineView` do módulo `QtWebEngineWidgets`, que é usada para exibir páginas web em um aplicativo PyQt5.

4. `from PyQt5.QtCore import QUrl`: Importa a classe `QUrl` do módulo `QtCore`, que é usada para representar URLs.

5. `class SimpleWebBrowser(QMainWindow):`: Define uma nova classe chamada `SimpleWebBrowser` que herda da classe `QMainWindow`. Essa classe representa a janela do navegador.

6. `def __init__(self):`: Define o método `__init__`, que é o construtor da classe. Ele é executado quando uma instância da classe é criada.

7. `super().__init__()`: Chama o construtor da classe pai (`QMainWindow`) para inicializar a janela.

8. `self.browser = QWebEngineView()`: Cria uma instância de `QWebEngineView`, que será usada para exibir conteúdo web.

9. `self.browser.setUrl(QUrl("http://www.google.com"))`: Define a URL inicial que o navegador irá carregar, neste caso, "http://www.google.com".

10. `self.setCentralWidget(self.browser)`: Define o widget central da janela como o `QWebEngineView`, tornando-o o conteúdo principal da janela.

11. `def main():`: Define uma função chamada `main()`, que será a função principal do aplicativo.

12. `app = QApplication(sys.argv)`: Cria uma instância da classe `QApplication`, que é necessária para iniciar a GUI do aplicativo e gerenciar o ciclo de vida.

13. `font = app.font()`: Obtém a fonte padrão do aplicativo.

14. `font.setFamily("Arial")`: Define a fonte padrão como "Arial". Você pode substituir "Arial" pela fonte de sua escolha.

15. `app.setFont(font)`: Define a fonte padrão para o aplicativo.

16. `window = SimpleWebBrowser()`: Cria uma instância da classe `SimpleWebBrowser`, que é a janela principal do navegador.

17. `window.show()`: Exibe a janela do navegador.

18. `sys.exit(app.exec_())`: Inicia o loop de eventos do aplicativo, mantendo o aplicativo em execução até que o usuário feche a janela.

19. `if __name__ == "__main__":`: Verifica se o script está sendo executado como o programa principal.

20. `main()`: Chama a função `main()` para iniciar o aplicativo.

Espero que esta explicação linha a linha seja útil. Se você tiver mais perguntas, fique à vontade para perguntar.
