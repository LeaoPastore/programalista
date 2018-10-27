class Model:
    def __init__(self):
        self.lista_compras = None

    def get_lista_compras(self):
        return self.lista_compras

    def carregar_lista_compras(self, lista_compras):
        self.lista_compras = lista_compras



    '''def add_lista(self):
        item = input("Insira seu item:")
        qtd = input("Insira quantos deseja")
        self.lista_compras.update({item : qtd})

c1 = Model()
print (c1.lista_compras)
c1.add_lista()
print (c1.lista_compras)
'''