# main.py
import npyscreen
from pages.router import router
from modules.uistyle import CustomTheme

class MyApp(npyscreen.NPSAppManaged):
    """Clase principal de la aplicación."""
    def onStart(self):
        # Aplicar el tema personalizado
        self.setTheme(CustomTheme)

        # Registrar todos los formularios (ventanas) para la navegación
        for route, form in router.items():
            if isinstance(form, str):
                module_path, class_name = form.rsplit('.', 1)
                module = __import__(module_path, fromlist=[class_name])
                form_class = getattr(module, class_name)
                self.addForm(route, form_class)
            else:
                self.addForm(route, form)

        # Establecer la página de inicio como el formulario inicial
        self.setNextForm('MAIN')

if __name__ == '__main__':
    app = MyApp()
    app.run()