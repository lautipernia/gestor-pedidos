#!/usr/bin/env python3
"""CLI del gestor de pedidos.

Ejemplos:
    python3 main.py generar-datos --n 300
    python3 main.py reporte
    python3 main.py agenda --dia hoy
    python3 main.py agenda --dia viernes --exportar agenda_viernes.csv
"""

import argparse
import csv
from pathlib import Path

from gestor.datos import generar_clientes, guardar_clientes, cargar_clientes
from gestor.agenda import agenda_del_dia, normalizar_dia
from gestor.mensajes import plantilla_mensaje
from gestor.reportes import resumen

RAIZ = Path(__file__).parent
DATOS_DEFAULT = RAIZ / "datos" / "clientes.csv"


def _cargar(args):
    if not Path(args.datos).exists():
        raise SystemExit(
            f"No existe {args.datos}. Generá la cartera con:\n"
            f"    python3 main.py generar-datos"
        )
    return cargar_clientes(args.datos)


def cmd_generar(args):
    clientes = generar_clientes(n=args.n, seed=args.seed)
    guardar_clientes(clientes, args.salida)
    print(f"✔ {len(clientes)} clientes generados en {args.salida}")


def cmd_reporte(args):
    print(resumen(_cargar(args)))


def cmd_agenda(args):
    clientes = _cargar(args)
    dia = normalizar_dia(args.dia)
    agenda = agenda_del_dia(clientes, dia)

    print(f"Agenda de contactos — {dia.capitalize()} ({len(agenda)} clientes)")
    print("=" * 60)
    for c in agenda:
        print(f"[{c.zona:<11}] {c.nombre:<22} {c.telefono}")
        print(f"   → {plantilla_mensaje(c)}")

    if args.exportar:
        with open(args.exportar, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["nombre", "telefono", "zona", "productos", "mensaje"])
            for c in agenda:
                w.writerow([c.nombre, c.telefono, c.zona,
                            c.productos_habituales, plantilla_mensaje(c)])
        print("=" * 60)
        print(f"✔ Agenda exportada a {args.exportar}")


def main():
    p = argparse.ArgumentParser(description="Gestor de pedidos por día de cliente.")
    sub = p.add_subparsers(dest="comando", required=True)

    g = sub.add_parser("generar-datos", help="Crea una cartera de clientes de ejemplo.")
    g.add_argument("--n", type=int, default=300, help="Cantidad de clientes (def. 300).")
    g.add_argument("--seed", type=int, default=42, help="Semilla reproducible (def. 42).")
    g.add_argument("--salida", default=str(DATOS_DEFAULT), help="Ruta del CSV de salida.")
    g.set_defaults(func=cmd_generar)

    r = sub.add_parser("reporte", help="Muestra la carga de pedidos por día.")
    r.add_argument("--datos", default=str(DATOS_DEFAULT), help="CSV de clientes.")
    r.set_defaults(func=cmd_reporte)

    a = sub.add_parser("agenda", help="Agenda de contactos de un día, con mensajes.")
    a.add_argument("--dia", default="hoy", help="lunes..sábado u 'hoy' (def. hoy).")
    a.add_argument("--datos", default=str(DATOS_DEFAULT), help="CSV de clientes.")
    a.add_argument("--exportar", help="Ruta opcional para exportar la agenda a CSV.")
    a.set_defaults(func=cmd_agenda)

    args = p.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
