from django.apps import AppConfig
from typing import Dict, Any

class AnappConfig(AppConfig):
    name = "anapp"
    container: Dict[str, Any]

    def ready(self) -> None:
        from anapp.dependencies_container import build_production_dependencies_container
        self.container = build_production_dependencies_container()

