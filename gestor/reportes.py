"""Reportes de carga de trabajo: pedidos por día, día pico y distribución."""

from .modelos import Cliente, DIAS
from .agenda import agrupar_por_dia


def pedidos_por_dia(clientes: list[Cliente]) -> dict[str, int]:
    grupos = agrupar_por_dia(clientes)
    return {d: len(grupos[d]) for d in DIAS}


def dia_pico(clientes: list[Cliente]) -> tuple[str, int]:
    ppd = pedidos_por_dia(clientes)
    dia = max(ppd, key=ppd.get)
    return dia, ppd[dia]


def resumen(clientes: list[Cliente]) -> str:
    """Reporte de texto con gráfico de barras ASCII de la carga semanal."""
    ppd = pedidos_por_dia(clientes)
    total = sum(ppd.values())
    maximo = max(ppd.values()) or 1

    lineas = ["Carga de pedidos por día", "=" * 44]
    for d in DIAS:
        n = ppd[d]
        barra = "█" * round(34 * n / maximo)
        lineas.append(f"{d.capitalize():<11}{n:>3}  {barra}")

    pico_d, pico_n = dia_pico(clientes)
    lineas += [
        "=" * 44,
        f"Total de clientes en cartera : {total}",
        f"Día pico                     : {pico_d.capitalize()} ({pico_n} pedidos)",
        f"Promedio por día             : {total / len(DIAS):.1f}",
    ]
    return "\n".join(lineas)
