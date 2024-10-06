# pages/docker-manager/docker_ui.py
import npyscreen
from pages.docker import docker_manager as dm

class DockerManagerForm(npyscreen.Form):
    """Menú de gestión de contenedores Docker."""
    def create(self):
        # Crear el menú de gestión de Docker
        self.add(npyscreen.TitleText, name="Gestión de Contenedores Docker", value="Selecciona una opción:", editable=False)
        self.add(npyscreen.ButtonPress, name="1. Listar Contenedores Activos", when_pressed_function=self.list_containers)
        self.add(npyscreen.ButtonPress, name="2. Volver al Menú Principal", when_pressed_function=self.return_to_main)

    def list_containers(self):
        # Llamar a la función `list_containers` del módulo `docker`
        containers = dm.list_containers()
        output = "\n".join([f"{c['id']} - {c['name']} ({c['status']})" for c in containers])
        npyscreen.notify_confirm(output, title="Contenedores Activos")

    def return_to_main(self):
        """Regresar al menú principal."""
        self.parentApp.setNextForm("MAIN")
