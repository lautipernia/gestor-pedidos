"""Lógica de agenda: agrupa clientes por día y arma la agenda diaria de contactos."""

import datetime

from .modelos import Cliente, DIAS

# Permite escribir el día sin acento o con acento.
_ALIAS = {
    "lunes": "lunes", "martes": "martes",
    "miercoles": "miércoles", "miércoles": "miércoles",
    "jueves": "jueves", "viernes": "viernes",
    "sabado": "sábado", "sábado": "sábado",
}


def normalizar_dia(dia: str) -> str:
    """Convierte 'hoy', 'miercoles', 'Sábado', etc. al nombre canónico."""
    dia = dia.strip().lower()
    if dia == "hoy":
        idx = datetime.date.today().weekday()   # 0=lunes ... 6=domingo
        return DIAS[idx] if idx < len(DIAS) else "lunes"   # domingo -> lunes
    if dia not in _ALIAS:
        raise ValueError(
            f"Día no reconocido: {dia!r}. Usá uno de: {', '.join(DIAS)} u 'hoy'."
        )
    return _ALIAS[dia]


def agrupar_por_dia(clientes: list[Cliente]) -> dict[str, list[Cliente]]:
    """Devuelve {día: [clientes]} para los 6 días operativos."""
    grupos = {d: [] for d in DIAS}
    for c in clientes:
        grupos[c.dia_pedido].append(c)
    return grupos


def agenda_del_dia(clientes: list[Cliente], dia: str) -> list[Cliente]:
    """Clientes a contactar en ``dia``, ordenados por zona y nombre
    (así el reparto se planifica por recorrido)."""
    dia = normalizar_dia(dia)
    delx = [c for c in clientes if c.dia_pedido == dia]
    return sorted(delx, key=lambda c: (c.zona, c.nombre))
