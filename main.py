from listacompras.view import View
from listacompras.control import Control
from listacompras.modelo import Model

m = Model()
# Instancia a View
v = View()
# Instanciar a Control
c = Control(v, m)
# Guardando a Control na View
v.set_control(c)

#exibir menu
c.exibir_menu()