import threading
import time

class myThread(threading.Thread):

    __slots__ = [ '_nome', '_contador', '_delay' '_sinc']

    def __init__(self, nome, contador, delay, sinc):
        threading.Thread.__init__(self)
        self._nome = nome
        self._contador = contador
        self._delay = delay
        self._sinc = sinc

        @property
        def get_nome(self):
            return self._nome

        @property
        def get_contador(self):
            return self._contador

        @property
        def get_delay(self):
            return self._delay

        @property
        def get_sinc(self):
            return self._sinc       

        def run(self):
            print('Iniciando'+ self._nome)
        self.sinc.acquire()
        print_time(self._nome, self._contador, self._delay)
        self._sinc.release()
        print('Finalizando' + self._nome)

def print_time(threadName, contador, delay):
    while contador:
        time.sleep(delay)
        print('{}: {}'.format(threadName,time.ctime(time.time())))
        contador -= 1

    sinc = threading.Lock()
    thread1 = myThread('Thread-1', 5,1,sinc)  
    thread2 = myThread('Thread-2', 5,1,sinc)
    '''Criando threads'''
    thread1.star()
    thread2.star()

    print('Finalizando a thread principal')