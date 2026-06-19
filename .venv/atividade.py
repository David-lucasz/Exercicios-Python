from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import Qt
from sys import argv


class atividade(QWidget):

    def __init__(self):
        super().__init__()

        # ======================================================
        # CONFIGURAÇÃO DA JANELA PRINCIPAL
        # ======================================================
        self.setWindowTitle("Cadastro")
        self.setGeometry(150, 50, 1000, 600)
        self.setFixedSize(1000, 600)
        self.setWindowIcon(QIcon("icone.png"))

        # Define cor de fundo geral da janela
        self.setStyleSheet("QWidget{background-color:#f0f0f0}")

        # ======================================================
        # LAYOUT PRINCIPAL (DIVISÃO ESQUERDA / DIREITA)
        # ======================================================
        self.layout_horizontal = QHBoxLayout()
        self.layout_horizontal.setSpacing(0)

        # ======================================================
        # COLUNA ESQUERDA (IMAGEM)
        # ======================================================
        self.label_logo = QLabel()

        imagem = QPixmap("doggg.png")
        self.label_logo.setPixmap(imagem)

        self.label_logo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_logo.setMinimumWidth(500)

        # Fundo branco da área da imagem
        self.label_logo.setStyleSheet("QLabel{background-color:#ffffff}")

        # ======================================================
        # COLUNA DIREITA (FORMULÁRIO)
        # ======================================================
        area_direita = QVBoxLayout()
        area_direita.setSpacing(5)
        area_direita.setContentsMargins(10, 10, 10, 10)

        # Espaço superior para centralizar melhor o formulário
        area_direita.addSpacing(80)

        # ======================================================
        # TÍTULO DO FORMULÁRIO
        # ======================================================
        mensagem = QLabel("cadastre e nos ajude doando")
        mensagem.setAlignment(Qt.AlignmentFlag.AlignCenter)
        mensagem.setStyleSheet(
            "QLabel{font-size:35px;font-weight:bold;color:#333333;}"
        )

        area_direita.addWidget(mensagem)

        # ======================================================
        # ESTILO PADRÃO DOS CAMPOS
        # ======================================================
        estilo_caixa = """
            QLineEdit{
                background-color:#eeeeee;
                border:2px solid #cccccc;
                border-radius:10px;
                padding:5px;
            }
        """

        # ======================================================
        # CAMPO: NOME
        # ======================================================
        nome_texto = QLabel("Nome")
        nome_texto.setStyleSheet("QLabel{font-size:20px;font-weight:bold;}")

        self.nome = QLineEdit()
        self.nome.setPlaceholderText("Seu Nome")
        self.nome.setFixedHeight(50)
        self.nome.setFixedWidth(250)
        self.nome.setStyleSheet(estilo_caixa)

        # ======================================================
        # CAMPO: EMAIL
        # ======================================================
        email_texto = QLabel("Email")
        email_texto.setStyleSheet("QLabel{font-size:20px;font-weight:bold;}")

        self.email = QLineEdit()
        self.email.setPlaceholderText("Seu Email")
        self.email.setFixedHeight(50)
        self.email.setFixedWidth(250)
        self.email.setStyleSheet(estilo_caixa)

        # ======================================================
        # CAMPO: SENHA
        # ======================================================
        senha_texto = QLabel("Senha")
        senha_texto.setStyleSheet("QLabel{font-size:20px;font-weight:bold;}")

        self.senha = QLineEdit()
        self.senha.setPlaceholderText("Senha")
        self.senha.setEchoMode(QLineEdit.EchoMode.Password)
        self.senha.setFixedHeight(50)
        self.senha.setFixedWidth(250)
        self.senha.setStyleSheet(estilo_caixa)

        # ======================================================
        # BOTÃO CADASTRAR
        # ======================================================
        botao = QPushButton("Cadastrar")
        botao.setFixedWidth(250)
        botao.setFixedHeight(45)

        botao.setStyleSheet("""
            QPushButton{
                background-color:#28a745;
                color:white;
                font-size:18px;
                font-weight:bold;
                border-radius:10px;
            }
            QPushButton:hover{
                background-color:#218838;
            }
        """)

        # ======================================================
        # TEXTO "OU"
        # ======================================================
        ou = QLabel("ou")
        ou.setStyleSheet("QLabel{font-size:18px;font-weight:bold;}")

        # ======================================================
        # BOTÕES SOCIAIS
        # ======================================================
        botoes_social = QHBoxLayout()
        botoes_social.setAlignment(Qt.AlignmentFlag.AlignCenter)

        facebook = QPushButton("Facebook")
        facebook.setFixedWidth(120)
        facebook.setFixedHeight(35)

        google = QPushButton("Google")
        google.setFixedWidth(120)
        google.setFixedHeight(35)

        botoes_social.addWidget(facebook)
        botoes_social.addWidget(google)

        # ======================================================
        # ADICIONANDO ELEMENTOS NA COLUNA DIREITA
        # ======================================================
        area_direita.addWidget(nome_texto, alignment=Qt.AlignmentFlag.AlignCenter)
        area_direita.addWidget(self.nome, alignment=Qt.AlignmentFlag.AlignCenter)

        area_direita.addWidget(email_texto, alignment=Qt.AlignmentFlag.AlignCenter)
        area_direita.addWidget(self.email, alignment=Qt.AlignmentFlag.AlignCenter)

        area_direita.addWidget(senha_texto, alignment=Qt.AlignmentFlag.AlignCenter)
        area_direita.addWidget(self.senha, alignment=Qt.AlignmentFlag.AlignCenter)

        area_direita.addWidget(botao, alignment=Qt.AlignmentFlag.AlignCenter)
        area_direita.addWidget(ou, alignment=Qt.AlignmentFlag.AlignCenter)
        area_direita.addLayout(botoes_social)

        # ======================================================
        # WIDGET DA COLUNA DIREITA
        # ======================================================
        self.widget_direita = QWidget()
        self.widget_direita.setLayout(area_direita)
        self.widget_direita.setMinimumWidth(500)

        # Fundo branco da área do formulário
        self.widget_direita.setStyleSheet("QWidget{background-color:#ffffff}")

        # ======================================================
        # JUNÇÃO DAS DUAS COLUNAS NA TELA
        # ======================================================
        self.layout_horizontal.addWidget(self.label_logo, 1)
        self.layout_horizontal.addWidget(self.widget_direita, 1)

        self.setLayout(self.layout_horizontal)


# ======================================================
# EXECUÇÃO DO PROGRAMA
# ======================================================
app = QApplication(argv)

janela = atividade()
janela.show()

app.exec()