# pages/github/github_ui.py
import npyscreen

class GitHubManagerForm(npyscreen.Form):
    def create(self):
        # Crear el menú de gestión de GitHub
        self.add(npyscreen.TitleText, name="Gestión de Repositorios de GitHub", value="Selecciona una opción:", editable=False)
        self.add(npyscreen.ButtonPress, name="1. Listar Repositorios", when_pressed_function=self.list_repos)
        self.add(npyscreen.ButtonPress, name="2. Crear Issue", when_pressed_function=self.create_issue)
        self.add(npyscreen.ButtonPress, name="3. Volver al Menú Principal", when_pressed_function=self.return_to_main)

    def list_repos(self):
        # Aquí va la lógica para listar repositorios
        npyscreen.notify_confirm("Funcionalidad aún no implementada.", title="Aviso")

    def create_issue(self):
        # Aquí va la lógica para crear issues
        npyscreen.notify_confirm("Funcionalidad aún no implementada.", title="Aviso")

    def return_to_main(self):
        """Regresar al menú principal."""
        self.parentApp.setNextForm("MAIN")
