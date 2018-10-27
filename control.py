class Control:
    def __init__(self, view, model):
        self.view = view
        self.model = model
        self.carregar_lista_compras()

    def exibir_menu(self):
        #Acionar o metodo da classe
        self.view.exibir_menu()

    #Metodo para recuperar lista
    def get_lista_compras(self):
        return self.model.get_lista_compras()

    def carregar_lista_compras(self):
        a = Arquivo
        self.model.carregar_lista_compras(a.ler_arquivo())

    def exibir_menu(self):
        self.view.exibir_menu()

    def get_lista_comrpas(self):
        return self.model.get_list_compras()

    def gravar_lista_compras(self):
        a = Arquivo()
        a.gravar_arquivo(self.model.get_lista_compras())
