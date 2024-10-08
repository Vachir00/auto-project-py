# pages/docker-manager/docker_manager.py
import docker
import subprocess
import os

# Crear un cliente Docker para interactuar con la API local
client = docker.from_env()

def list_containers(all=False):
    """ Lista los contenedores y obtiene un inspect de cada contenedor.
    Devuelve la lista de contenedores activos o todos los contenedores si all=True.
    Ejecuta el comando "docker inspect" para obtener información detallada de cada contenedor.
    Almacena el resultado de inpect en un archivo temporal de cada contenedor.
    """
    # Obtencion de contenedores
    containers = client.containers.list(all=all)

    # Almacenamiento en memoria de datos
    container_data = [
        {
            "containerID": c.id[:12],
            "Name": c.name,
            "Image": c.image.tags[0] if c.image.tags else c.image.id[:12],
            "Created": c.attrs['Created'],
            "Status": c.status,
            "ports": c.ports
        } for c in containers
    ]

    # Creacion de un archivo temporal para cada contenedor
    # Archivo se guarda en ./tempdata/inspect_<container_id>.txt
    # Si el archivo existe, lo elimina para evitar duplicados, si no existe, lo crea
    # Ejecuta el comando "docker inspect" y guarda el resultado en el archivo temporal
    for i, c in enumerate(containers):
        container_id = c.id[:12]
        # obtener el path actual
        current_full_path = os.path.abspath(__file__)
        current_path = os.path.dirname(current_full_path)
        file_path = f"{current_path}/tempdata/inspect_{container_id}.txt"

        # Almacena path del archivo temporal en el diccionario de contenedores
        container_data[i]["file_path"] = file_path

        if os.path.exists(file_path):
            os.remove(file_path)

        subprocess.run(["docker", "inspect", container_id], stdout=open(file_path, "w"))
    
    # Retorno de datos
    return container_data

def start_container(container_id):
    """Inicia un contenedor especifico."""
    try:
        container = client.containers.get(container_id)
        container.start()
        return {"message": f"Container {container_id} started successfully"}
    except docker.errors.NotFound:
        return {"error": f"Container with ID {container_id} not found"}

def stop_container(container_id):
    """Detiene un contenedor especifico."""
    try:
        container = client.containers.get(container_id)
        container.stop()
        return {"message": f"Container {container_id} stopped successfully"}
    except docker.errors.NotFound:
        return {"error": f"Container with ID {container_id} not found"}

def remove_container(container_id):
    """Elimina un contenedor especifico."""
    try:
        container = client.containers.get(container_id)
        container.remove(force=True)
        return {"message": f"Container {container_id} removed successfully"}
    except docker.errors.NotFound:
        return {"error": f"Container with ID {container_id} not found"}

