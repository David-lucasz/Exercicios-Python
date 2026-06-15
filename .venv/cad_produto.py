from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QLineEdit
import sys

class cadastroproduto(QWidget):                     
    #metodo init para inicializar a nossa janela
    def __init__(self):
        super().__init__()
        #vamos setar um texto para o titulo para a janela
        self.setWindowTitle("cadastro de produtos")
        # setar a posiçao e o tamanho da janela 
        self.setGeometry(100,100,300,450)    

        self.setStyleSheet("background-color:#5BCEFA")

        self.nome_label = QLabel("nome do produto")
        #vamos aplicar uma fotmataçao na label usando
        #comandos da css(cascade style sheet - folha de estilo em cascata)
        self.nome_label.setStyleSheet("QLabel{font-size:20pt;color:#d500f9;font-weight:bold}")
        self.nome_edit = QLineEdit()
        self.nome_edit.setStyleSheet("QLineEdit{border-radius:5px; background-color:#F5A9B8; font-size:20pt;color:#6a1b9a}")
       


        self.tipo_label = QLabel("tipo")
        self.tipo_label.setStyleSheet("QLabel{font-size:20pt;color:#F750FF;font-weight:bold}")
        self.tipo_edit = QLineEdit()
        self.tipo_edit.setStyleSheet("QLineEdit{border-radius:5px; background-color:#ffffff; font-size:20pt;color:#6a1b9a}")



        self.preco_label = QLabel("preço")
        self.preco_label.setStyleSheet("QLabel{font-size:20pt;color:#F750FF;font-weight:bold}")
        self.preco_edit = QLineEdit()
        self.preco_edit.setStyleSheet("QLineEdit{border-radius:5px; background-color:#F5A9B8; font-size:20pt;color:#6a1b9a}")
        

        self.cadastrar_button = QPushButton("cadastrar")
        self.layout_vertical =  QVBoxLayout()

        #adicionar os controles no layout
        self.layout_vertical.addWidget(self.nome_label)
        self.layout_vertical.addWidget(self.nome_edit)

        self.layout_vertical.addWidget(self.tipo_label)
        self.layout_vertical.addWidget(self.tipo_edit)

        self.layout_vertical.addWidget(self.preco_label)
        self.layout_vertical.addWidget(self.preco_edit)     
        
        self.layout_vertical.addWidget(self.cadastrar_button)

        # adicionar o layout vertical com todos os controles a nossa janela
        self.setLayout(self.layout_vertical)


#apresentar a janela
app = QApplication(sys.argv)
cad = cadastroproduto()
cad.show()
app.exec()