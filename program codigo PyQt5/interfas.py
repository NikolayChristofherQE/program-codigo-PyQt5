import sys
from PyQt5.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsItem
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter


class DrawingScene(QGraphicsScene):
    
 
def __init__(self, parent = None):
        
        supe

    
super().__init__(parent)

        self.current_shape = 

        self.current_sha


        self.c


     
None
        self.start_point = 
        self.start_point = Non

        self.start_p

        se
None

    def mousePressEvent(self, event):
        self.start_point = event.scenePos()
        
        self.start_point = event.scenePos()
       

        self.start_point = event.scenePos()
    

        self.start_point = event.scenePos()
 

        self.start_point = event.scen

        self.start_point = ev

        self.start_po

        self.

     
if self.current_shape == 'Rectangle':
            self.addRect(event.scenePos().x(), event.scenePos().y(), 
            self.addRect(event.scenePos().x(), event.scenePos().y

            self.addRect(event.scenePos().x(), event.scen

            self.addRect(event.scenePos().x(), ev

            self.addRect(event.scenePos().x

            self.addRect(event.sceneP

            self.addRect(event

            self.addRec

            self.

           

   
100, 50)
        
  
elif self.current_shape == 'Ellipse':
            self.addEllipse(event.scenePos().x(), event.scenePos().y(), 
            self.addEllipse(event.scenePos().x(), event.scenePos().

            self.addEllipse(event.scenePos().x(), event.sc

            self.addEllipse(event.scenePos().x(),

            self.addEllipse(event.scene

            self.addEllipse(e

            self.addEll

            self

        
100, 50)
        
        
elif self.current_shape == 'Line':
            self.start_point = event.scenePos()
        
            self.start_point = event.scenePos()

            self.start_point = event

            self.start_poi

            self

    
else:
            
        
super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        
     
if self.current_shape == 'Line' and self.start_point is not None:
            end_point = event.scenePos()
            self.addLine(self.start_point.x(), self.start_point.y(), end_point.x(), end_point.y())

    
            end_point = event.scenePos()
            self.addLine(self.start_point.x(), self.start_point.y(), end_point.x(), end_point.y())


            end_point = event.scenePos()
            self.addLine(self.start_point.x(), self.start_point.y(), end_point.x(), end

            end_point = event.scenePos()
            self.addLine(self.start_point.x(), self.start_point.y(), end_po

            end_point = event.scenePos()
            self.addLine(self.start_point.x(), self.start_point

            end_point = event.scenePos()
            self.addLine(self.start_point.x(), self

            end_point = event.scenePos()
            self.addLine(self.start_point.

            end_point = event.scenePos()
            self.addLine(self.st

            end_point = event.scenePos()
            self.addLi

            end_point = event.scenePos()
           

            end_point = event.scenePos()

            end_point = event.s

            end_point

          
def set_shape(self, shape):
        self.current_shape = shape



        self.current_shape = shape


        self.current_shap

        self.cu

     
class DrawingApplication(QApplication):
    
   
def __init__(self, sys_argv):
        
        supe

       

   
super().__init__(sys_argv)

        self.initUI()

    

        self.initUI()


        self.


     
def initUI(self):
        self.window = DrawingWindow()
        self.window.show()



        self.window = DrawingWindow()
        self.window.sho

        self.window = DrawingWindow()
        sel

        self.window = DrawingWindow()

        self.window = Draw

        self.win

     
class DrawingWindow(QGraphicsView):
    
  
def __init__(self):
        
 
super().__init__()

        self.setWindowTitle(

        self.setWindowTi


        self.

       
'Geometric Shapes Drawing')
        self.setGeometry(
        self.setGeo

        se

 
100, 100, 800, 600)

        self.scene = DrawingScene()
        self.setScene(self.scene)

    

        self.scene = DrawingScene()
        self.setScene(self.scene)

  


        self.scene = DrawingScene()
        self.setScene(self


        self.scene = DrawingScene()
        self.se


        self.scene = DrawingScene()
     


        self.scene = DrawingSce


        self.scene = D


        self


 
def keyPressEvent(self, event):
        
  
if event.key() == Qt.Key_R:
            self.scene.set_shape(
            self.scene.set_

            self.s

        
'Rectangle')
        
        eli

 
elif event.key() == Qt.Key_E:
            self.scene.set_shape(
            self.scene.set_

            self.

      
'Ellipse')
        
        el

  
elif event.key() == Qt.Key_L:
            self.scene.set_shape(
            self.scene.set_

            self.

       
'Line')
        
      
else:
            
          

 
super().keyPressEvent(event)


if __name__ == '__main__':
    app = DrawingApplication(sys.argv)
    sys.exit(app.exec_())

    app = DrawingApplication(sys.argv)
    sys.exit(app.e

    app = DrawingApplication(sys.argv)
    sys

    app = DrawingApplication(sys.argv

    app = DrawingApplicatio

    app = Drawing

    app 