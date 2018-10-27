class View:
    def __init__(self):
        self.control = None

    def set_control(self, control):
        self.control = control

    # Metodo de exibição do menu
    def exibir_menu(self):
        resposta = True

        while resposta:
            print('''
            1. Exibir lista
            2. Incluir item
            3. Excluir item
            4. Sair
            ''')

            resposta = input("Digite um número:")

            if resposta == '1':
                print('\n Lista de itens')
                self.exibir_lista_compras(self.control.get_lista_compras())
            elif resposta == '2':
                print('\n Item incluído')

            elif resposta == '3':
                print('\n item excluído')
            elif resposta == '4':
                self.gravar_lista_compras()
                print("\n Tchau!")
                resposta = False
            else:
                print('\n Valor incorreto')

    def exibir_lista_compras(self, lista_compras):
        # A lista de compras é um dicionario
        # Pecorrer o dicionario
        for chave, valor in lista_compras.items():
            print(f'\n- {chave} : {valor}')

    def gravar_lista_compras(self):
        self.control.gravar_lista_compras()



