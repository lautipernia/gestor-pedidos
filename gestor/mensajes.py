"""Generación de mensajes personalizados listos para enviar al cliente."""

from .modelos import Cliente


def plantilla_mensaje(cliente: Cliente, empresa: str = "la distribuidora") -> str:
    """Arma el mensaje de WhatsApp para coordinar el pedido del día.

    Esto es lo que automatiza el trabajo manual: en vez de escribir uno por uno,
    el sistema genera el texto ya personalizado por cliente.
    """
    return (
        f"Hola {cliente.primer_nombre}, ¿cómo estás? Te escribo de {empresa} "
        f"para coordinar tu pedido de hoy. ¿Te preparo lo habitual "
        f"({cliente.productos_habituales})? Confirmame cantidad y horario de "
        f"entrega en zona {cliente.zona}. ¡Gracias!"
    )
