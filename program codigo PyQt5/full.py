import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Establecer el título de la ventana
        self.setWindowTitle("Mi primera ventana")

        # Crear una etiqueta
        label = QLabel("Hola, mundo!")

        # Añadir la etiqueta a la ventana
        self.setCentralWidget(label)

        # Mostrar la ventana
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Crear una instancia de la ventana
    my_window = MyWindow()

    # Ejecutar la aplicación
    sys.exit(app.exec_())