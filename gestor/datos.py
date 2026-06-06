"""Carga, guardado y generación de datos de clientes (CSV, compatible con Excel)."""

import csv
import random
from pathlib import Path

from .modelos import Cliente, DIAS

CAMPOS = ["id", "nombre", "telefono", "dia_pedido", "zona",
          "productos_habituales", "pedido_promedio"]

_NOMBRES = [
    "Juan", "María", "Carlos", "Lucía", "Diego", "Sofía", "Martín", "Valentina",
    "Nicolás", "Camila", "Lautaro", "Julieta", "Mateo", "Florencia", "Tomás",
    "Agustina", "Santiago", "Brenda", "Federico", "Micaela", "Gabriel", "Rocío",
    "Ramiro", "Daniela", "Ezequiel", "Carla", "Facundo", "Paula", "Iván", "Romina",
    "Hernán", "Belén", "Maximiliano", "Antonella", "Leandro", "Melina",
]
_APELLIDOS = [
    "González", "Rodríguez", "Gómez", "Fernández", "López", "Díaz", "Martínez",
    "Pérez", "García", "Sánchez", "Romero", "Sosa", "Torres", "Álvarez", "Ruiz",
    "Ramírez", "Flores", "Acosta", "Benítez", "Medina", "Suárez", "Herrera",
    "Aguirre", "Pereyra", "Gutiérrez", "Molina", "Castro", "Ortiz", "Núñez", "Silva",
]
_ZONAS = ["Centro", "Norte", "Sur", "Oeste", "Costa", "Microcentro"]
_PRODUCTOS = [
    "fiambres y lácteos", "bebidas", "almacén", "panificados",
    "congelados", "artículos de limpieza",
]
# Pesos por día: simula una cartera con picos a mitad y fin de semana,
# como pasa en distribución de alimentos.
_PESO_DIAS = {
    "lunes": 0.15, "martes": 0.13, "miércoles": 0.22,
    "jueves": 0.13, "viernes": 0.22, "sábado": 0.15,
}


def generar_clientes(n: int = 300, seed: int = 42) -> list[Cliente]:
    """Genera una cartera sintética y realista de ``n`` clientes (reproducible)."""
    rng = random.Random(seed)
    dias = list(_PESO_DIAS)
    pesos = list(_PESO_DIAS.values())
    clientes = []
    for i in range(1, n + 1):
        nombre = f"{rng.choice(_NOMBRES)} {rng.choice(_APELLIDOS)}"
        telefono = f"+54 9 11 {rng.randint(2000, 7999)}-{rng.randint(1000, 9999)}"
        clientes.append(Cliente(
            id=i,
            nombre=nombre,
            telefono=telefono,
            dia_pedido=rng.choices(dias, weights=pesos, k=1)[0],
            zona=rng.choice(_ZONAS),
            productos_habituales=rng.choice(_PRODUCTOS),
            pedido_promedio=rng.randint(2, 25),
        ))
    return clientes


def guardar_clientes(clientes: list[Cliente], path) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(CAMPOS)
        for c in clientes:
            w.writerow([c.id, c.nombre, c.telefono, c.dia_pedido,
                        c.zona, c.productos_habituales, c.pedido_promedio])


def cargar_clientes(path) -> list[Cliente]:
    clientes = []
    with open(path, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            clientes.append(Cliente(
                id=int(row["id"]),
                nombre=row["nombre"],
                telefono=row["telefono"],
                dia_pedido=row["dia_pedido"],
                zona=row["zona"],
                productos_habituales=row["productos_habituales"],
                pedido_promedio=int(row["pedido_promedio"]),
            ))
    return clientes
