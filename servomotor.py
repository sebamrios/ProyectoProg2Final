# ProyectoProg2Final
class ServoMotor(object):
  
  """docstring para servomotor de puertas"""
  #atributos:
  #    id: identificacion del servomotor a comandar
  #    estado: estado del servomotor           
  
  def __init__(self,id):
    self.id=id
    self.estado=0              #incialmente cerrada la puerta
    
  def abrir(self,id):
    self.estado=1
    print "Puerta abierta"     #mensaje de apertura de la puerta con la id
    radio.send(id,1)
    return 1

  def cerrar(self,id):
    self.estado=0
    print "Puerta cerrada"     #mensaje de cierre de la puerta con la id
    radio.send(id,0)
    return 0
 
  def posicion(self):
    radio.send(id,self.estado) 
    if (self.estado=0):
      print "La puerta esta abierta"
    else:
      print "La puerta esta cerrada"
   return self.estado
