from skimage.io import imread
import datetime as dt
from matplotlib.pyplot import imshow

class Pessoa:

    __slots__ = ['_nome', '_cpf', '_addres', '_telefone']

    def __init__(self, nome,  cpf, endereco, tel):
        self._nome = nome
        self._cpf = cpf
        self._addres = endereco
        self._telefone = tel

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome    

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, cpf):
        self._cpf = cpf    

    @property
    def addres(self):
        return self._addres

    @addres.setter
    def addres(self, addres):
        self._addres = addres    

    @property
    def telefone(self):
        return self._telefone

    @telefone.setter
    def telefone(self, tel):
        self._telefone = tel

    def imprimir(self):
        print('Nome: {}'.format(self.nome))
        print('CPF: {} '.format(self.cpf))
        print('Endereço: {}'.format(self._addres))
        print('Telefone: {} '.format(self.telefone))

class Fotografia:

    _qtd_fotos = 0
    __slots__ = ['_foto', '_fotografo', '_proprietario', 'data']

    def __init__(self, foto, fotografo, proprietario):
        self._foto = imread(foto)
        self._fotografo = fotografo
        self._proprietario = proprietario
        self.data = dt.date.today()
        Fotografia._qtd_fotos += 1

    @property
    def foto(self):
        return self._foto

    @foto.setter
    def foto(self, novafoto):
        self._foto = imread(novafoto)    

    @property
    def fotografo(self):
        return self._fotografo

    @fotografo.setter
    def fotografo(self, fotografo):
        self._fotografo = fotografo    

    @property
    def proprietario(self):
        return self._proprietario
   
    @proprietario.setter
    def proprietario(self, prop):
        self.foto.setter = prop
        
    @staticmethod
    def get_qtd_fotos():
        return Fotografia._qtd_fotos

    def mostrar_fotografia(self):
        imshow(self._foto)

    def prop_foto(self):
        print('Tamanho: {}'.format(self.foto.shape))
        self.fotografo.imprimir()
        print('Data: ', str(self.data))

pessoa1 = Pessoa('David', '888', 'Casa1', '11111111')
pessoa2 = Pessoa('Natan', '321', 'Casa2', '222222222')
fotografia = Fotografia('flower.jpg', pessoa1, pessoa2)
fotografia.mostrar_fotografia()