"""Tests del núcleo de la lógica (correr con: python3 -m pytest)."""

from gestor.modelos import Cliente
from gestor.agenda import agrupar_por_dia, agenda_del_dia, normalizar_dia
from gestor.reportes import pedidos_por_dia, dia_pico
from gestor.mensajes import plantilla_mensaje


def _c(id, dia, zona="Centro", nombre="Ana Pérez"):
    return Cliente(id, nombre, "+54 9 11 0000-0000", dia, zona, "almacén", 5)


def test_agrupar_por_dia_cuenta_bien():
    cs = [_c(1, "lunes"), _c(2, "lunes"), _c(3, "martes")]
    g = agrupar_por_dia(cs)
    assert len(g["lunes"]) == 2
    assert len(g["martes"]) == 1
    assert len(g["sábado"]) == 0


def test_agenda_ordena_por_zona_y_nombre():
    cs = [_c(1, "lunes", zona="Sur", nombre="Zoe Díaz"),
          _c(2, "lunes", zona="Norte", nombre="Ana López")]
    agenda = agenda_del_dia(cs, "lunes")
    assert [c.zona for c in agenda] == ["Norte", "Sur"]


def test_normalizar_dia_acepta_sin_acento():
    assert normalizar_dia("miercoles") == "miércoles"
    assert normalizar_dia("Sábado") == "sábado"


def test_pedidos_por_dia_y_pico():
    cs = [_c(1, "viernes"), _c(2, "viernes"), _c(3, "lunes")]
    assert pedidos_por_dia(cs)["viernes"] == 2
    assert dia_pico(cs) == ("viernes", 2)


def test_mensaje_incluye_primer_nombre_y_zona():
    c = _c(1, "lunes", zona="Costa", nombre="Juan Gómez")
    msg = plantilla_mensaje(c)
    assert "Juan" in msg and "Costa" in msg


def test_dia_invalido_lanza_error():
    try:
        Cliente(1, "Test", "x", "domingo", "Centro", "almacén", 5)
    except ValueError:
        return
    raise AssertionError("Debió rechazar 'domingo'")
