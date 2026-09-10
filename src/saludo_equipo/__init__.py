import logging

from rich.console import Console

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)
console = Console()


def main() -> None:
    logger.info("Entorno reconstruido correctamente.")
    console.print("[bold green]Hola desde el equipo, armado con uv[/bold green]")