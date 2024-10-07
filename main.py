# main.py
import npyscreen
from pages.home import HomePage
from pages.docker.docker_ui import DockerManagerForm
from pages.github.github_ui import GitHubManagerForm

from modules.uistyle import CustomTheme


class MyApp(npyscreen.NPSAppManaged):
    """Clase principal de la aplicación."""
    def onStart(self):
        # Aplicar el tema personalizado
        npyscreen.setTheme(CustomTheme)

        # Registrar la página de inicio
        self.addForm('MAIN', HomePage)
        self.addForm('DOCKER', DockerManagerForm)
        self.addForm('GITHUB', GitHubManagerForm)

        # Establecer la página de inicio como el formulario inicial
        self.setNextForm('MAIN')

if __name__ == '__main__':
    app = MyApp()
    app.run()