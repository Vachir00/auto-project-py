import npyscreen

class HomePage(npyscreen.Form):
    def create(self):
        self.add(npyscreen.TitleText, name="Bienvenido a Auto-Project-Py", editable=False, color="STANDOUT")
        self.add(npyscreen.MultiLineEdit, 
                 value="""
                 Esta es la página de inicio de Auto-Project-Py.
                 
                 Utilice las teclas de navegación para moverse entre las diferentes secciones:
                 - Docker Manager
                 - GitHub Manager
                 - Otras funcionalidades...
                 
                 Presione 'q' para salir.
                 """, 
                 editable=False,
                 max_height=10,
                 color="CONTROL")

    def afterEditing(self):
        self.parentApp.setNextForm(None)