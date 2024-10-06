# pages/docker-manager/docker_manager.py
import docker

# Crear un cliente Docker para interactuar con la API local
client = docker.from_env()

def list_containers(all=False):
    """Devuelve la lista de contenedores activos o todos los contenedores si all=True."""
    containers = client.containers.list(all=all)
    return [{"id": c.id[:12], "name": c.name, "status": c.status} for c in containers]
