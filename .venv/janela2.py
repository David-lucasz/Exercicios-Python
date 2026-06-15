from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
import sys

class janela2(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("minha janela")
        #largura, altura, posiçao dajanela
        self.setGeometry(10,20,800,400)
        self.texto = QLabel("clique no botao abaixo")
        self.botao = QPushButton("clique aki")
        # para organizar os controles(label) usaremos o comando
        #QVBoxLayout, para distribuir os controles de forma vertical na tela
        layout_vertical = QVBoxLayout()
        layout_vertical.addWidget(self.texto)
        layout_vertical.addWidget(self.botao)
        #adicionar um layout vertical na tela 
        self.setLayout(layout_vertical)

app = QApplication(sys.argv)
tela = janela2()
tela.show()
app.exec()