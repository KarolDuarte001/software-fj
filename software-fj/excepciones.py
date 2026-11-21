"""
Módulo de excepciones personalizadas del sistema Software FJ.
Permite categorizar los errores y encadenarlos con 'raise ... from ...'.
"""

class SoftwareFJError(Exception):
    """Excepción base del sistema. Todas heredan de aquí."""
    pass

class ValidacionError(SoftwareFJError):
    """Errores de validación de datos de entrada."""
    pass

class ClienteInvalidoError(ValidacionError):
    """Datos del cliente no cumplen reglas de negocio."""
    pass

class ServicioNoDisponibleError(SoftwareFJError):
    """El servicio solicitado no está disponible."""
    pass

class ReservaInvalidaError(SoftwareFJError):
    """La reserva no cumple las condiciones mínimas."""
    pass

class OperacionNoPermitidaError(SoftwareFJError):
    """Se intenta una transición de estado no permitida."""
    pass

class ParametroFaltanteError(ValidacionError):
    """Falta un parámetro obligatorio."""
    pass

class CalculoInconsistenteError(SoftwareFJError):
    """El cálculo dio un resultado inválido (negativo, NaN, etc.)."""
    pass