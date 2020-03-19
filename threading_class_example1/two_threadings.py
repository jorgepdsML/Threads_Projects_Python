#uso del modulo threading para invocar a dos hilos y que
#en cada hilo se le pida 2 argumentos , nombre y tiempo
#el tiempo indica el tiempo sin hacer nada
#en total deberia demorar el hilo que toma mayor tiempo
import threading
import numpy as np
import time
#variable global1 igual a 0
global1=0
def func1(name,tiempo):
    global global1
    global1 = global1+1
    time.sleep(tiempo)
    print("NOMBRE ES:",name)
def func2(name,tiempo):
    global global1
    global1 =global1+1
    time.sleep(tiempo)
    print("NOMBRE ES:",name)
#crear hilo N°1
thread1=threading.Thread(target=func1,args=("jorge_miranda",2))
#crear hilo N°2
thread2=threading.Thread(target=func2,args=("braintels_labs",3))
t1=time.time()
#inciar el proceso de hilo N°1
thread1.start()#metodo invoca al método run()
#inciar el proceso de hilo N°2
thread2.start()#método invoca al método run()
#método join() para esperar hasta que el hilo acabe
thread1.join()
thread2.join()
t2=time.time()
print("====RESULTADOS========")
print("===VARIABLE GLOBAL global1=== :",global1)
print("==TIEMPO TRANSCURRIDO APROXIMADO==",t2-t1)