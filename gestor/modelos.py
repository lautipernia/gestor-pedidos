"""Modelo de datos del dominio."""

from dataclasses import dataclass

# Días en los que la distribuidora toma pedidos / reparte (no opera domingo).
DIAS = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado"]


@dataclass
class Cliente:
    """Una cuenta de la cartera, con su día fijo de pedido."""

    id: int
    nombre: str
    telefono: str
    dia_pedido: str            # uno de DIAS
    zona: str
    productos_habituales: str
    pedido_promedio: int       # bultos/unidades promedio por pedido

    def __post_init__(self):
        if self.dia_pedido not in DIAS:
            raise ValueError(
                f"Día de pedido inválido para {self.nombre!r}: {self.dia_pedido!r}. "
                f"Debe ser uno de: {', '.join(DIAS)}."
            )

    @property
    def primer_nombre(self) -> str:
        return self.nombre.split()[0]
