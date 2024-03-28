import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen, QBrush, QColor
from diagram_scene import DiagramScene

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Diagram Scene en pyqt')
        self.setGeometry(100, 100, 800, 600)

        self.scene = DiagramScene(self)
        self.setCentralWidget(self.scene)

        self.create_flowchart()

    def create_flowchart(self):
        # Create shapes
        start_shape = self.scene.add_shape(100, 100, 'Start')
        process_shape = self.scene.add_shape(300, 100, 'Process')
        decision_shape = self.scene.add_shape(500, 100, 'Decision')
        end_shape = self.scene.add_shape(700, 100, 'End')

        # Create arrows
        self.scene.add_arrow(start_shape, process_shape)
        self.scene.add_arrow(process_shape, decision_shape)
        self.scene.add_arrow(decision_shape, end_shape)

        # Create text
        self.scene.add_text(200, 150, 'Start')
        self.scene.add_text(400, 150, 'Process')
        self.scene.add_text(600, 150, 'Decision')
        self.scene.add_text(800, 150, 'End')

        # Customize colors
        self.scene.set_shape_color(start_shape, QColor(0, 255, 0))
        self.scene.set_shape_color(process_shape, QColor(0, 0, 255))
        self.scene.set_shape_color(decision_shape, QColor(255, 0, 0))
        self.scene.set_shape_color(end_shape, QColor(255, 255, 0))

        self.scene.set_arrow_color(start_shape, process_shape, QColor(0, 255, 0))
        self.scene.set_arrow_color(process_shape, decision_shape, QColor(0, 0, 255))
        self.scene.set_arrow_color(decision_shape, end_shape, QColor(255, 0, 0))

        # Customize fonts
        self.scene.set_text_font(start_shape, 'Start', QFont('Arial', 12, QFont.Bold))
        self.scene.set_text_font(process_shape, 'Process', QFont('Arial', 12, QFont.Bold))
        self.scene.set_text_font(decision_shape, 'Decision', QFont('Arial', 12, QFont.Bold))
        self.scene.set_text_font(end_shape, 'End', QFont('Arial', 12, QFont.Bold))

        # Customize styles
        self.scene.set_text_style(start_shape, 'Start', Qt.AlignCenter)
        self.scene.set_text_style(process_shape, 'Process', Qt.AlignCenter)
        self.scene.set_text_style(decision_shape, 'Decision', Qt.AlignCenter)
        self.scene.set_text_style(end_shape, 'End', Qt.AlignCenter)

        # Customize underlines
        self.scene.set_text_underline(start_shape, 'Start', True)
        self.scene.set_text_underline(process_shape, 'Process', False)
        self.scene.set_text_underline(decision_shape, 'Decision', False)
        self.scene.set_text_underline(end_shape, 'End', True)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()