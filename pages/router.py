# pages/router.py
from pages.docker.docker_ui import DockerManagerForm
from pages.github.github_ui import GitHubManagerForm
from pages.home import HomePage

router = {
    'MAIN': HomePage,
    'docker': DockerManagerForm,
    'github': GitHubManagerForm
}
