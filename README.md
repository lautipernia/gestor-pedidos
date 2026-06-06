# 📦 Gestor de Pedidos

Herramienta en Python que **organiza una cartera de clientes por día de pedido**,
genera la **agenda diaria de contactos con mensajes personalizados listos para enviar**
y **reporta la carga de trabajo** de cada día de la semana.

> Inspirado en un sistema real que desarrollé para optimizar la gestión de **~300 clientes**
> en una distribuidora de alimentos, donde se llegaban a coordinar **hasta ~70 pedidos en un solo día**.
> Este repositorio es una versión limpia, documentada y testeada de esa idea.

---

## El problema

En una distribuidora con cientos de clientes, cada cuenta pide un día fijo de la semana.
Coordinar a mano (revisar planillas, buscar quién pide hoy, escribir uno por uno el
mensaje de WhatsApp) es **lento y propenso a errores**: se olvidan clientes, se duplica
trabajo y el día pico se vuelve un caos.

## La solución

Un sistema que toma la cartera completa y, para cualquier día:

1. **Filtra** automáticamente los clientes que piden ese día.
2. Los **ordena por zona** para planificar el recorrido de reparto.
3. **Genera el mensaje ya personalizado** de cada cliente (nombre, productos habituales, zona).
4. Permite **exportar la agenda a CSV/Excel** para el equipo.
5. **Mide la carga semanal** e identifica el día pico, para distribuir mejor el trabajo.

Lo que antes era trabajo manual repetitivo, acá se resuelve con un comando.

---

## Uso

Sin dependencias externas (solo Python 3.10+).

```bash
# 1) Generar una cartera de ejemplo (300 clientes reproducibles)
python3 main.py generar-datos --n 300

# 2) Ver la carga de pedidos de la semana
python3 main.py reporte

# 3) Armar la agenda de contactos de un día (con mensajes)
python3 main.py agenda --dia hoy
python3 main.py agenda --dia viernes --exportar agenda_viernes.csv
```

### Ejemplo de salida — reporte de carga

```
Carga de pedidos por día
============================================
Lunes       48  ████████████████████████
Martes      30  ███████████████
Miércoles   68  ██████████████████████████████████
Jueves      38  ███████████████████
Viernes     57  ████████████████████████████
Sábado      59  ██████████████████████████████
============================================
Total de clientes en cartera : 300
Día pico                     : Miércoles (68 pedidos)
Promedio por día             : 50.0
```

### Ejemplo de salida — agenda diaria

```
Agenda de contactos — Viernes (57 clientes)
============================================================
[Centro     ] Iván Rodríguez         +54 9 11 2466-7041
   → Hola Iván, ¿cómo estás? Te escribo de la distribuidora para
     coordinar tu pedido de hoy. ¿Te preparo lo habitual (artículos
     de limpieza)? Confirmame cantidad y horario de entrega en zona
     Centro. ¡Gracias!
```

---

## Estructura

```
gestor-pedidos/
├── main.py              # CLI (argparse): generar-datos · reporte · agenda
├── gestor/
│   ├── modelos.py       # Modelo Cliente (dataclass + validación)
│   ├── datos.py         # Carga/guardado CSV y generador de datos
│   ├── agenda.py        # Agrupar por día y armar la agenda diaria
│   ├── mensajes.py      # Plantillas de mensaje personalizado
│   └── reportes.py      # Métricas de carga + gráfico ASCII
├── tests/
│   └── test_agenda.py   # Tests con pytest
├── datos/clientes.csv   # Cartera de ejemplo
└── requirements.txt
```

## Tests

```bash
python3 -m pytest -q
```

```
......                                                    6 passed
```

---

## Qué demuestra este proyecto

- **Automatización de un proceso comercial real** (de trabajo manual a un comando).
- **Python** con código modular, `dataclasses`, type hints y `argparse`.
- **Manejo de datos** (CSV/Excel) y métricas para la toma de decisiones.
- **Buenas prácticas**: separación de responsabilidades, validación de datos y **tests**.

## Tecnologías

Python 3.10+ · biblioteca estándar (`csv`, `dataclasses`, `argparse`, `datetime`) · pytest

---

Autor: **Lautaro Mendoza** — [github.com/lautipernia](https://github.com/lautipernia)
