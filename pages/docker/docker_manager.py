# pages/docker-manager/docker_manager.py
import docker

# Crear un cliente Docker para interactuar con la API local
client = docker.from_env()

def list_containers(all=False):
    """Devuelve la lista de contenedores activos o todos los contenedores si all=True."""
    containers = client.containers.list(all=all)
    return [
        {
            "containerID": c.id[:12],
            "Name": c.name,
            "Image": c.image.tags[0] if c.image.tags else c.image.id[:12],
            "Created": c.attrs['Created'],
            "Status": c.status,
            "ports": c.ports
        } for c in containers
    ]

def get_container_inspect(container_id):
    """Devuelve el resultado de la inspección de un contenedor específico."""
    try:
        container = client.containers.get(container_id)
        inspect_data = container.attrs
        return inspect_data
    except docker.errors.NotFound:
        return {"error": f"Container with ID {container_id} not found"}
    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}