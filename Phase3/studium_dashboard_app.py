from dashboard_controller import DashboardController
from dashboard_cli import DashboardCLI
from json_modul_repository import JsonModulRepository
from studien_service import StudienService

class StudiumDashboardApp:
    def start(self) -> None:
        repository = JsonModulRepository("module.json")
        service = StudienService()
        controller = DashboardController(repository, service)
        cli = DashboardCLI()

        daten = controller.lade_dashboard_daten()
        cli.anzeigen(daten)

if __name__ == "__main__":
    StudiumDashboardApp().start()