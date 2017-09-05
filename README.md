# ProyectoProg2Final
class ServoMotor(object):
  
  """docstring para servomotor de puertas"""
  #atributos:
  #id
  #estado           
  
  def __init__(self,id):
    self.id=id
    self.estado=0     #incialmente cerrada la puerta
    
  def abrir(self,id):
    self.estado=1
    print "Puerta abierta"
    radio.send(id,1)
    return 1

  def cerrar(self,id):
    self.estado=0
    print "Puerta cerrada"
    radio.send(id,0)
    return 0
 
  def posicion(self):
    radio.send(id,self.estado)
    return self.estado
