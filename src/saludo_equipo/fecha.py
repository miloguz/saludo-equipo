import logging
from datetime import datetime

from rich.console import Console

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)
console = Console()


def mostrar_fecha() -> None:
    ahora = datetime.now()
    console.print(
        f"[bold cyan]Fecha:[/bold cyan] {ahora:%d/%m/%Y}  "
        f"[bold cyan]Hora:[/bold cyan] {ahora:%H:%M:%S}"
    )


def main() -> None:
    mostrar_fecha()
