# pages/docker-manager/docker_ui.py
import npyscreen
from pages.docker.docker_manager import DockerContainers

class DockerManagerForm(npyscreen.FormBaseNew):
    """Menú de gestión de contenedores Docker."""
    def create(self):
        y, x = self.useable_space()
        
        # Crear el box superior con las opciones
        self.menu_box = self.add(npyscreen.BoxTitle, name="Opciones", max_width=x-4, relx=2, max_height=6)
        self.menu_box.values = [
            "1. Listar Contenedores Activos",
            "2. Volver al Menú Principal"
        ]
        self.menu_box.when_value_edited = self.handle_menu_selection

    def handle_menu_selection(self):
        selection = self.menu_box.value
        if selection == 0:
            self.list_containers()
        elif selection == 1:
            self.return_to_main()

    def list_containers(self):
        y, x = self.useable_space()
        
        # Definir los encabezados y anchos de columnas
        headers = ["ID", "Name"]
        max_widths = [12, 50]  # Ajustar según sea necesario

        # Crear el Box de Resultados
        self.results_box = self.add(npyscreen.BoxTitle, name="Resultados", 
                                    max_width=sum(max_widths) + 6, relx=2, rely=8, max_height=y-10)
        
        # Crear el Box de Detalles
        self.details_box = self.add(npyscreen.BoxTitle, name="Detalles", 
                                    max_width=x - (sum(max_widths) + 6) - 5, relx=sum(max_widths) + 9, rely=8, 
                                    max_height=y-10)

        # Obtener y formatear los datos de los contenedores
        containers = DockerContainers().list_containers(all=True)
        header_row = "  ".join(f"{h:<{w}}" for h, w in zip(headers, max_widths))
        container_rows = []
        for c in containers:
            row = [
                c['containerID'],
                c['Name'][:max_widths[1]]
            ]
            container_rows.append("  ".join(f"{col:<{w}}" for col, w in zip(row, max_widths)))
        
        # Asignar los valores al Box de Resultados
        self.results_box.values = ["", header_row] + container_rows
        self.results_box.entry_widget.set_editable(False)
        
        # Personalizar el comportamiento del cursor para evitar seleccionar encabezados
        self.results_box.entry_widget.when_cursor_moved = self.skip_headers
        self.results_box.entry_widget.cursor_line = 2  # Posicionar el cursor en la primera fila de datos sin seleccionarla
        self.results_box.entry_widget.how_exited = npyscreen.wgwidget.EXITED_DOWN
        self.results_box.display()

        # Agregar función para manejar la selección de un contenedor
        def on_selection():
            widget = self.results_box.entry_widget
            selected_index = widget.cursor_line - 2  # Restar 2 para compensar las filas de encabezado
            if selected_index >= 0 and selected_index < len(containers):
                container_id = containers[selected_index]['containerID']
                self.show_container_details(container_id)

        # Conectar la función de selección al widget
        self.results_box.entry_widget.when_cursor_moved = on_selection

    def skip_headers(self, widget=None):
        """Evitar que el cursor seleccione las filas de encabezado o vacías."""
        if not widget:
            widget = self.results_box.entry_widget
        if widget.cursor_line < 2:
            widget.cursor_line = 2  # Mover el cursor a la primera fila de datos
        widget.display()

    def show_container_details(self, container_id):
        """Mostrar detalles del contenedor en el Box de Detalles."""
        # Obtener el archivo inspect del contenedor seleccionado
        # Archivo se guarda en ./tempdata/inspect_<container_id>.txt
        # Leer el archivo y mostrar los detalles en el Box de Detalles
        file_path = f"./tempdata/inspect_{container_id}.txt"
        with open(file_path, 'r') as file:
            inspect_data = file.read()
        self.details_box.values = inspect_data.split('\n')
        self.details_box.display()

    def return_to_main(self):
        """Regresar al menú principal."""
        self.parentApp.switchForm("MAIN")
