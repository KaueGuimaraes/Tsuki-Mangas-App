import sys


from files import *


from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


user = ''
name = 'Tsuki Mangas App'

home = 'https://tsukimangas.com/login'
profile = 'https://tsukimangas.com/perfil/[]'
config = 'https://tsukimangas.com/perfil/[]/editar'
prime = 'https://tsukimangas.com/prime'

developer = 'https://tsukimangas.com/perfil/kaue-guimaraes'

if exist('user.txt'):
    user = read('user.txt')
else:
    write('user.txt', '')

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl(home))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        navbar = QToolBar()
        self.addToolBar(navbar)

        # Definindo itens
        back_btn = QAction('<', self)
        back_btn.triggered.connect(self.browser.back)

        forward_btn = QAction('>', self)
        forward_btn.triggered.connect(self.browser.forward)

        reload_btn = QAction('Recarregar', self)
        reload_btn.triggered.connect(self.browser.reload)

        home_btn = QAction('Início', self)
        home_btn.triggered.connect(self.navigate_home)

        self.user = QLineEdit()
        self.user.setText(user)

        set_user_btn = QAction('Adicionar usuário', self)
        set_user_btn.triggered.connect(self.set_user)

        profile_btn = QAction('Perfil', self)
        profile_btn.triggered.connect(self.go_to_profile)

        config_btn = QAction('Configurações', self)
        config_btn.triggered.connect(self.go_to_config)

        developer_btn = QAction('Developer', self)
        developer_btn.triggered.connect(self.go_to_developer)

        prime_btn = QAction('Prime', self)
        prime_btn.triggered.connect(self.go_to_prime)

        # Adicionando a navbar
        navbar.addAction(back_btn)
        navbar.addAction(forward_btn)
        navbar.addAction(reload_btn)
        navbar.addAction(home_btn)
        navbar.addWidget(self.user)
        navbar.addAction(set_user_btn)
        navbar.addAction(profile_btn)
        navbar.addAction(config_btn)
        navbar.addAction(developer_btn)
        navbar.addAction(prime_btn)

    def navigate_home(self):
        self.browser.setUrl(QUrl(home))
    
    # Atalhos
    def go_to_profile(self):
        new_url = profile.replace('[]', user)
        print(new_url)
        self.browser.setUrl(QUrl(new_url))
    
    def go_to_config(self):
        new_url = config.replace('[]', user)
        print(new_url)
        self.browser.setUrl(QUrl(new_url))

    def go_to_prime(self):
        self.browser.setUrl(QUrl(prime))
    #Atalhos

    def go_to_developer(self):
        self.browser.setUrl(QUrl(developer))

    def set_user(self):
        global user

        user = self.user.text()
        delete('user.txt')
        write('user.txt', user)
        print(user)

        return user

    def update_url(self, q):
        self.url_bar.setText(q.toString())

app = QApplication(sys.argv)
QApplication.setApplicationName(name)
window = MainWindow()
app.exec_()


