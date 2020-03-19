"""
uso del modulo threading mediante la definición de una sub_clase
la herencia viene de la clase base Thread
"""
import threading
import time
class BThread(threading.Thread):
    #atributo de clase
    Nthread=0
    #overriding el método __init__()
    def __init__(self,name="braintels"):
        #invocar al método __init__() del ancestro
        threading.Thread.__init__(self)
        #agregar un atributo name
        self.name=name
        #atributo de clase paara saber el numero de hilos creados
        self.__class__.Nthread+=1
    def run(self):
        #método run representa al hilo que se desea ejecutar
        print("====HILO N°1 ==== INICIO")
        #==========colocar codigo aqui=======
        print("MI NOMBRE ES:",self.name)
        #================================
        print("===HILO N°1 === FIN")
#crear un hilo
h1=BThread("jorge_miranda")
#iniciar la actividad del hilo
h1.start() #este método invoca al método run ()
#esperar hasta que el hilo termine su ejecución
h1.join()
print("===HILOS CREADOS SON:",BThread.Nthread)