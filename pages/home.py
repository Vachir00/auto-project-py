import npyscreen

class HomePage(npyscreen.FormBaseNew):        
    def create(self):
        y, x = self.useable_space()
        
        self.name = "Auto-Project-py v0.1"
        
        
        box_width = 40
        box_height = 8
        box_relx = (x - box_width) // 2
        box_rely = (y - box_height) // 2

        self.add_widget(npyscreen.BoxTitle, name="Menu Principal", editable=False, color="STANDOUT", 
                        rely=box_rely, relx=box_relx, max_width=box_width, max_height=box_height)
        
        self.add_widget(npyscreen.ButtonPress, name="1. Gestión de Docker", when_pressed_function=self.goto_docker_manager, 
                        rely=box_rely + 2, relx=box_relx + 2)
        self.add_widget(npyscreen.ButtonPress, name="2. Gestión de GitHub", when_pressed_function=self.goto_github_manager, 
                        rely=box_rely + 4, relx=box_relx + 2)
        self.add_widget(npyscreen.ButtonPress, name="3. Salir", when_pressed_function=self.exit_application, 
                        rely=box_rely + 6, relx=box_relx + 2)

    def afterEditing(self):
        pass
    
    def goto_docker_manager(self):
        """Cambiar a la interfaz de gestión de Docker."""
        self.parentApp.switchForm('DOCKER')

    def goto_github_manager(self):
        """Cambiar a la interfaz de gestión de GitHub."""
        self.parentApp.switchForm('GITHUB')

    def exit_application(self):
        """Cerrar la aplicación."""
        self.parentApp.setNextForm(None)
        self.parentApp.switchForm(None)

    def on_ok(self):
        pass